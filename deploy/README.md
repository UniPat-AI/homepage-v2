# Deployment operations

## GitHub Actions

Repository: `UniPat-AI/homepage-v2`; production branch: `main`.

Secrets in the `production` environment (not repository-level secrets):

- `DEPLOY_SSH_KEY`: dedicated Ed25519 private key for the `unipat-deploy` account.
- `DEPLOY_KNOWN_HOSTS`: independently verified SSH host key entry for the server.

Repository variables:

- `DEPLOY_HOST`: `47.236.21.40`.
- `DEPLOY_USER`: `unipat-deploy`.

Environment: `production`, URL `https://unipat.ai`. Its deployment branch policy
allows only the branch `main`. The SSH secrets must never be copied into repository
secrets: branch authors can change their own workflow files.

`main` 使用标准分支保护：必须经过 PR，分支保持最新，GitHub Actions 的 `check`
检查通过，且讨论全部解决。这些要求也适用于管理员；禁止强制推送和删除。
写入允许名单为 `zhonggang-dev` 和 `hahongbong`，普通协作者不能合并到 `main`。
组织所有者仍有 GitHub 的管理员合并权限，这是当前明确保留的权限安排。
额外的 `Only website maintainers may merge main` 更新限制规则已停用并保留配置，
因此满足检查要求后，授权人员可直接使用绿色合并按钮，无需勾选 bypass。
不要重新启用这条额外规则，除非明确要恢复严格两人限制及其手动 bypass 操作。

Actions holds read-only repository permissions. The SSH user cannot log in with
the server administrator password; its only sudo entry runs the root-owned
activation helper for this website. Root never runs repository Python scripts.
The helpers under `deploy/server` are installed by an administrator, so changing
them in Git alone does not change the privileged server configuration.

## Server layout

- Service: `unipat-homepage-v2.service`, running as `unipat-web` on `127.0.0.1:5003`.
- Active symlink: `/opt/unipat-official/current`.
- CI releases: `/opt/unipat-official/releases/ci/<full-commit-sha>/`.
- Each CI release has a `.venv/` and a checksummed `release.json`.
- Uploads: `/opt/unipat-official/incoming/`.
- Activation history: `/opt/unipat-official/deployment-history/`.
- Public health check: `https://unipat.ai/_health`, returning the active commit.
- Existing Nginx continues to terminate HTTPS and serve `current/static/`.

Each workflow waits for checks, uploads a complete runtime archive and invokes
`/usr/local/bin/unipat-deploy-release COMMIT`. Preparation runs as `unipat-deploy`;
the narrow sudo helper atomically changes `current`, restarts only the v2 service,
checks its actual commit and verifies Nginx-served CSS/JS. It restores the prior
release if activation fails. Concurrent releases are serialized on the server.

## Roll back a new-site update

The usual source-based rollback is `git revert <bad-commit>` followed by a push to
`main`; it is checked and published by the same workflow. To activate a retained
release immediately, an administrator may run:

```sh
sudo /usr/local/sbin/unipat-activate-release <retained-full-commit-sha>
```

## Restore the original website

The original `/home/application/UniPat_Prod` and `unipat-prod.service` on port 5002
are separate and remain intact. Its source and configuration backup is:
`/opt/unipat-official/backups/20261030-170519-official/`.

After checking for subsequent Nginx changes, an administrator can restore the
original route:

```sh
cp /opt/unipat-official/backups/20261030-170519-official/unipat.conf /etc/nginx/conf.d/unipat.conf
nginx -t && systemctl reload nginx
```

The old repository's CI still targets the original service; this repository
exclusively publishes the new service. It does not modify staging or Echo.

## Existing page issues

The initial import preserves the current published UI. The source still has
lowercased sitemap slugs that do not match case-sensitive content filenames.
ScienceVision's mobile overflow and axis alignment were fixed in PR #2.

## Independent branch previews

The `Branch previews` workflow deploys non-main branch pushes after checks pass.
It never deploys code from fork PRs. The branch name becomes a readable prefix
plus a 12-character SHA-256 suffix, so names such as `feature/a` and `feature-a`
cannot collide. The Actions summary contains the stable preview URL. Branch
deletion uses the workflow on the default branch to remove its container and route.

Environment `preview`:

- Variables: `PREVIEW_HOST=43.106.60.226`, `PREVIEW_USER=unipat-preview`,
  `PREVIEW_DOMAIN=unipat.43.106.60.226.sslip.io`.
- Secrets: `PREVIEW_SSH_KEY`, `PREVIEW_KNOWN_HOSTS`; separate from production.
- Temporary public HTTP access. Nginx adds `X-Robots-Tag: noindex, nofollow,
  noarchive`; the app also returns `Disallow: /` on non-production hosts.

Server layout:

- Root-owned configuration: `/etc/unipat-preview.json`.
- Root-owned deployment entrypoint: `/usr/local/sbin/unipat-preview`, accepting
  **no command-line arguments** and only a bounded JSON request on stdin.
- Forced SSH command: `/usr/local/bin/unipat-preview-ssh`, allowing SFTP and the
  `preview` API only. Root owns the account's SSH authorization files; the account
  has no Docker-group membership, interactive shell access via its key, or general sudo.
- Uploads: `/opt/unipat-previews/incoming`, owned by `unipat-preview`.
- Releases and state: `/opt/unipat-previews/releases/<branch-key>/` and `state/`.
- Nginx routes: `/opt/unipat-previews/nginx/*.conf` on the internal Docker network.
  The existing Caddy proxies only the dedicated preview suffix. Activation health
  checks traverse that complete route through Caddy on host loopback port 80.
- Root-owned `bundle.py` and `client.py` in `/usr/local/lib/unipat-preview`.

Each branch runs as UID 65532 with a read-only filesystem, read-only source mount,
a 128MB temporary filesystem, 512MB memory, one CPU, 128 PIDs, no Linux capabilities,
no Docker socket or production credentials, and an internal Docker network without
general outbound Internet access. External browser assets still load in the visitor's
browser. New dependency locks require an administrator to rebuild the trusted runtime
image; branch-controlled install scripts never execute on the host.

The server validates upload paths, ownership, archive contents and checksums. It
starts a new container and checks its exact release before switching Nginx. Failed
health checks restore the previous route. A server lock and workflow generation
ordering prevent older completed runs from replacing newer deployments; deletion
leaves a tombstone to prevent a cancelled older run from recreating a deleted preview.
At most ten branches run concurrently; delete unused branches to free capacity.

Infrastructure source is in `deploy/preview/`. These host helpers are installed
by an administrator, so updating them in Git does not silently update the host.
The Caddy change is backed up in `/opt/unipat-previews/Caddyfile.before-preview`.
If the existing Caddy container is recreated by another site's deployment, preserve
its `unipat-preview` network attachment and the dedicated preview host block.

To move previews to intranet-only access later, replace the public Caddy route
with an internal/VPN-facing gateway and update `PREVIEW_DOMAIN`. Merely hiding
DNS or using robots.txt is not an access restriction.
