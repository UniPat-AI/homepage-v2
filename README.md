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
git switch -c feature/website-update
git add <changed-files>
git commit -m "Update website"
git push -u origin feature/website-update
```

Repository: **https://github.com/UniPat-AI/homepage-v2**.
Every non-`main` branch push runs checks and deploys a complete, independent
preview on the test server. Open the **Branch previews** Actions run and find
the **Branch preview** link in its summary. Subsequent pushes update that same
URL; deleting the branch removes its preview. No PR is needed to get a preview.

Open a PR targeting `main` after reviewing the preview. Only `zhonggang-dev`
and `hahongbong` in the `homepage-v2-maintainers` team may merge, and the required
`check` must pass on an up-to-date branch. Direct pushes, force pushes and deletion
of `main` are blocked. A successful merge automatically publishes to
**https://unipat.ai**. Production can also be redeployed manually from `main`.

Previews temporarily use public HTTP addresses under
`*.unipat.43.106.60.226.sslip.io`. They contain the website's public content;
do not put confidential content or production credentials in a preview branch.

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
3.11 before pushing. A deployment administrator must also rebuild the fixed
preview runtime image after dependency changes. No credentials belong in the repository.
