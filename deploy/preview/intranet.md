# 内网预览运维

预览运行在 `10.0.0.214`，访问者先连接飞连。域名为
`<分支标识>.unipat.10.0.0.214.sslip.io`，由 Actions Summary 提供。
飞连管理员需给使用者授权 TCP `10.0.0.214:80`，并保证该域名可解析。
这属于飞连/VPC 网络访问控制；网站自身未增加飞书登录或用户身份验证。

## 部署通道

```text
GitHub Actions
  └─ SSH：unipat-ci-relay@43.106.60.226
      └─ 仅允许 127.0.0.1:22022
          └─ 由新服务器主动建立的反向 SSH 隧道
              └─ unipat-preview@10.0.0.214:22（强制命令）
                  └─ SFTP 上传 + deploy/remove/health API
```

原服务器保留作部署中继，不再提供预览网页。不要删除它或关闭 SSH，
否则自动部署会失败，但内网已发布页面仍可访问。

- 原服务器 `/etc/ssh/sshd_config.d/80-unipat-preview-relay.conf` 对应
  [`intranet/relay-sshd.conf`](intranet/relay-sshd.conf)。修改后先 `sshd -t` 再 reload。
- 两个账户的 home、`.ssh` 和 `authorized_keys` 均由 root 管理。
  `unipat-ci-relay` 的 key 使用 `restrict,port-forwarding,permitopen="127.0.0.1:22022"`；
  `unipat-ci-tunnel` 使用 `restrict,port-forwarding,permitlisten="127.0.0.1:22022"`。
  配合 Match 规则分别限制 local/remote forwarding，禁止 shell 和其他转发。
- 新服务器 `/etc/systemd/system/unipat-preview-tunnel.service` 对应
  [`intranet/tunnel.service`](intranet/tunnel.service)，以无登录权限的
  `unipat-tunnel` 系统账户运行，断线自动重连，开机自动启动。
- 隧道私钥位于 `/etc/unipat-preview-tunnel/id_ed25519`，目录 root:unipat-tunnel 750、
  私钥 root:unipat-tunnel 640；`known_hosts` 固定原服务器主机密钥。
- CI 的两套私钥分别放在 GitHub `preview` 环境的
  `PREVIEW_SSH_KEY` / `PREVIEW_RELAY_SSH_KEY`，主机密钥使用对应 `KNOWN_HOSTS` secrets。
  任何私钥和密码均不得进入 Git。

## 容器与访问限制

- `unipat-preview` 是 `--internal` Docker 网络，仅连接应用容器和 Nginx。
- `unipat-preview-ingress` 只给 Nginx 提供入站连接。
- Nginx 端口绑定为 `10.0.0.214:80:8080`、`127.0.0.1:80:8080`，
  不发布到 `0.0.0.0` 或 IPv6；采用 [`nginx-intranet.conf`](nginx-intranet.conf)。
- Nginx 允许私网及回环源 IP，其他来源 403。不要增加公网 HTTP 反向代理，
  也不要把 `$http_x_forwarded_for` 当成受信任的客户端地址。
- 固定运行镜像 `unipat-preview-runtime:20261102`；分支依赖锁改变时需管理员重建。
  新机首次镜像从原测试服务器使用 `docker save` / `docker load` 迁入，
  因为新机直接拉取 Docker Hub 超时。镜像内容需按 Config/RootFS 校验，
  不要把不同 Docker 镜像存储后端显示的 manifest ID 当作内容不一致。

## 排障与恢复

在新服务器检查：

```sh
systemctl status unipat-preview-tunnel
docker ps --filter name=up-
docker exec unipat-preview-gateway nginx -t
journalctl -u unipat-preview-tunnel -n 50 --no-pager
curl -H 'Host: <分支预览完整域名>' http://127.0.0.1/_health
```

在中继服务器检查 `ss -lntp sport = :22022`，必须只监听 `127.0.0.1`。
隧道故障可在新服务器 `systemctl restart unipat-preview-tunnel`。
网页能打开但 CI 失败时先查隧道；CI 成功但同事打不开时先查飞连授权和 DNS。

旧预览发布文件与停用的路由留存用于回滚，旧 Caddy 配置备份为
`/opt/unipat-previews/Caddyfile.before-intranet`；恢复此配置会重新公开网页，
必须重新获得用户授权。原服务器上其他网站的 Caddy 路由和服务不受迁移影响。
