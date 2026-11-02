# UniPat official website

Source for [unipat.ai](https://unipat.ai). This repository contains the published
homepage, Blog, Benchmarks, Join us, shared visual assets and ScienceVision
viewers. Design galleries and unpublished blog drafts remain in the separate
preview project.

## Develop

Use Python 3.11:

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-production.txt
flask --app wsgi:app run --port 5589
```

## Publish

```sh
git add <changed-files>
git commit -m "Update website"
git push origin main
```

GitHub Actions checks every push and pull request. A successful push to `main`
automatically publishes to **https://unipat.ai**. Other branches only run checks.
The workflow can also be run manually on `main` from the Actions tab.

The deployment uses a dedicated SSH account, validates a checksummed release,
installs its own Python environment, checks public pages and assets, then switches
the active release. If server or HTTPS checks fail during activation, the previous
release is restored. The current, previous and five most recent CI releases are
retained. The original website service and its separate backup are preserved.

See [deployment operations](deploy/README.md) for configuration and rollback.

## Check locally

```sh
python -m unittest discover -s tests -v
python deploy/validate.py
```

Runtime versions are pinned in `requirements.lock`. When dependencies change,
update the lock file as well as `requirements.txt` and run the checks with Python
3.11 before pushing. No credentials belong in the repository.

## OTS catalog

Edit `static/data/ots.json` to update the Training & Validation OTS page.
This data is public and ships through the existing `static/` packaging rule.
Branch previews use the trusted packager from `main`, so adding a new content
directory only to a feature branch's allowlist does not include it in previews.
