"""Build and safely unpack a self-contained, checksummed public-site release."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import tarfile

ROOT_FILES = {"app.py", "wsgi.py", "requirements.txt", "requirements-production.txt", "requirements.lock"}
PREFIXES = ("templates/", "content/blog/", "content/benchmarks/", "static/")
EXCLUDED = ("templates/designs/", "static/designs/", "static/studio/", "static/visions/")


def allowed(name):
    path = PurePosixPath(name)
    return (not path.is_absolute() and all(part not in ("..", "__pycache__") and not part.startswith(".") for part in path.parts)
            and not name.endswith((".pyc", ".pyo")) and not name.startswith(EXCLUDED)
            and (name in ROOT_FILES or name == "deploy/validate.py" or name.startswith(PREFIXES)))


def build(source, output, commit):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a full commit SHA")
    source, output = Path(source), Path(output)
    files = {}
    for path in sorted(source.rglob("*")):
        name = path.relative_to(source).as_posix()
        if allowed(name) and path.is_file():
            if path.is_symlink():
                raise ValueError("Symlink is not allowed: " + name)
            files[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    for name in ROOT_FILES | {"deploy/validate.py"}:
        if name not in files:
            raise ValueError("Missing runtime file: " + name)
    with tarfile.open(output, "w:gz") as archive:
        for name in files:
            archive.add(source / name, arcname=name, recursive=False)
        data = json.dumps({"commit": commit, "files": files}, sort_keys=True, indent=2).encode()
        info = tarfile.TarInfo("release.json")
        info.size, info.mode = len(data), 0o644
        archive.addfile(info, io.BytesIO(data))
    return len(files)


def unpack(archive_path, destination, commit):
    destination = Path(destination)
    if not destination.is_dir() or any(destination.iterdir()):
        raise ValueError("Release destination must be an empty directory")
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        names = [m.name for m in members]
        if len(names) != len(set(names)) or len(names) > 10000 or sum(m.size for m in members) > 800 * 1024 * 1024:
            raise ValueError("Invalid archive size or duplicate members")
        for member in members:
            if not member.isfile() or (member.name != "release.json" and not allowed(member.name)):
                raise ValueError("Unsafe archive member: " + member.name)
        for member in members:
            target = destination / member.name
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as src, target.open("xb") as dst:
                while chunk := src.read(1024 * 1024):
                    dst.write(chunk)
            target.chmod(0o644)
    manifest = json.loads((destination / "release.json").read_text())
    if manifest["commit"] != commit or set(manifest["files"]) != set(names) - {"release.json"}:
        raise ValueError("Release manifest mismatch")
    for name, digest in manifest["files"].items():
        if hashlib.sha256((destination / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Checksum mismatch: " + name)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=".")
    parser.add_argument("--output", required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    print("Packaged", build(args.source, args.output, args.commit), "runtime files")
