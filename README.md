# UniPat 官网

[UniPat 官网](https://unipat.ai)的源代码仓库，包含已发布的首页、Blog、Benchmarks、
Join us、共用图片与样式，以及 ScienceVision 查看器。
设计方案展示和未发布的博客草稿保留在单独的预览项目中。

## 获取分支预览地址

**把代码 push 到本仓库的非 `main` 分支，检查通过后就会自动部署预览，
不需要先创建 PR。每个分支是一套独立网站，包括首页、Blog 等页面。**

1. Push 后，先等 [Check and deploy official website](https://github.com/UniPat-AI/homepage-v2/actions/workflows/deploy.yml)
   中本次提交的 `check` 检查通过。
2. 打开 [Actions → Branch previews](https://github.com/UniPat-AI/homepage-v2/actions/workflows/preview.yml)。
3. 找到标题为 **`Preview 你的分支名`** 的记录。例如，分支 `feature/mobile`
   对应 **`Preview feature/mobile`**。按分支名和 push 时间查找，等待部署成功（绿色勾号）。
4. 点击这条记录，进入 **Summary（摘要）**。向下滚动到任务流程图下方的
   **`preview summary` → `Branch preview`** 区域。
5. **`Preview:` 后面的蓝色网址就是网站预览地址。先连接飞连，再点击打开。** 也可以复制给已连接飞连的同事。
   同一区域的 **`Commit:`** 是这次部署的代码版本，可用它确认是否对应自己的提交。

页面里要找的是这一块：

```text
preview summary

Branch preview
• Preview: http://……unipat.10.0.0.214.sslip.io
• Commit:  本次部署的提交 SHA
```

请复制 **`Preview:` 后的网站地址**；浏览器地址栏中的 `github.com/.../actions/runs/...`
只是部署记录页面。预览地址由系统生成，不需要自己拼接分支名。

### 找不到链接时

| 看到的情况 | 说明与处理方式 |
| --- | --- |
| 刚 push，列表里还没有预览任务 | 先等代码检查通过，再刷新 `Branch previews` 列表。 |
| 检查或部署失败（红色叉号） | 本次更新没有成功发布；打开失败步骤查看日志，修复后再次 push。 |
| `Preview main` 显示 `Skipped` | 正常：`main` 发布正式官网，不生成分支预览。 |
| 绿色任务里没有 `Branch preview` 区域 | 可能是删除分支后的清理任务；查看是否执行了 `Remove deleted branch preview`。清理成功不会生成访问链接。 |
| 旧记录只叫 `Branch previews #数字` | 这是任务命名调整前的历史记录；部署成功的旧记录也可在同一摘要位置找到链接。 |
| 预览链接打不开或连接超时 | 先连接飞连，确认有访问 `10.0.0.214:80` 的权限；仍失败时联系飞连管理员。 |
| 打开以前保存的预览链接出现 404 | 分支删除后预览会自动回收；请查看该分支是否还存在。 |

- **同一分支再次 push：地址不变，部署成功后内容更新。**
- **不同分支：各自独立，不会覆盖其他分支的预览。**
- **合并到 `main`：检查与生产部署成功后，更新 [正式官网 unipat.ai](https://unipat.ai)。**
- **当前预览已迁到公司内网测试服务器 `10.0.0.214`，需要连接飞连后访问。** 旧的公网预览入口已关闭；请以迁移后最新成功任务中的链接为准。
- 飞书私信和邮件自动通知尚未接入，请通过上述 Actions 入口取链接。

## 本地开发

使用 Python 3.11，执行以下命令：

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-production.txt
flask --app wsgi:app run --port 5589
```

启动后访问 [本地网站](http://127.0.0.1:5589)。

## 提交与发布

在自己的分支上提交代码并推送：

```sh
git switch -c feature/website-update
git add <changed-files>
git commit -m "更新官网内容"
git push -u origin feature/website-update
```

仓库地址：[UniPat-AI/homepage-v2](https://github.com/UniPat-AI/homepage-v2)。
每次向非 `main` 分支 push，都会先执行检查，通过后在测试服务器部署独立的完整网站。
按照上面的[获取分支预览地址](#获取分支预览地址)步骤查看和分享链接，无需先创建 PR。

确认预览效果后，创建目标分支为 `main` 的 PR（合并请求）。
官网维护者 `zhonggang-dev` 和 `hahongbong` 可以合并；组织所有者也保留 GitHub 的管理员合并权限，
普通协作者不能合并到 `main`。所有合并都须经过 PR，分支与最新 `main` 保持同步，
必需的 `check` 检查通过，且 PR 中的讨论已解决。
满足这些条件后，有权限的人会看到正常的绿色 **`Merge pull request`** 按钮，无需勾选 bypass。
`main` 禁止直接 push、强制推送和删除。
合并后会自动触发检查和正式部署，成功后更新 [unipat.ai](https://unipat.ai)。
也可以从 `main` 手动触发重新部署。

预览使用 `*.unipat.10.0.0.214.sslip.io` 下的内网 HTTP 地址，解析到 `10.0.0.214`。
飞连管理员需要允许网站使用者访问该地址的 TCP 80；若公司 DNS 拦截公网域名解析到内网地址，
请管理员为该预览域名配置内网解析。正式官网 `unipat.ai` 的公网访问保持不变。
不要将任何生产环境凭据提交到预览分支。

正式部署使用专用 SSH 账号，校验发布包、安装独立 Python 环境并检查页面和静态资源，
然后切换到新版本。切换过程中若服务器或 HTTPS 检查失败，会恢复上一版本。
服务器保留当前版本、上一版本及最近五次 CI 发布版本；原官网服务及其独立备份也保留，供回滚使用。

部署配置与回滚操作详见[部署运维说明](deploy/README.md)。

## 本地检查

提交前可以运行以下检查：

```sh
python -m unittest discover -s tests -v
python deploy/validate.py
```

运行时依赖版本固定在 `requirements.lock` 中。修改依赖时，同时更新该锁文件和
`requirements.txt`，并在 push 前使用 Python 3.11 完成检查。
依赖变更后，还需要部署管理员重新构建预览环境的固定运行镜像。
不要将任何密钥或密码提交到仓库。
