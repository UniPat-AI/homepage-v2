# UniPat official website

Source for [unipat.ai](https://unipat.ai). This repository contains the published
homepage, Blog, Benchmarks, Join us, shared visual assets and ScienceVision
viewers. Design galleries and unpublished blog drafts remain in the separate
preview project.

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
5. **`Preview:` 后面的蓝色网址就是网站预览地址。** 点击即可打开，也可以复制给同事。
   同一区域的 **`Commit:`** 是这次部署的代码版本，可用它确认是否对应自己的提交。

页面里要找的是这一块：

```text
preview summary

Branch preview
• Preview: http://……unipat.43.106.60.226.sslip.io
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
| 打开以前保存的预览链接出现 404 | 分支删除后预览会自动回收；请查看该分支是否还存在。 |

- **同一分支再次 push：地址不变，部署成功后内容更新。**
- **不同分支：各自独立，不会覆盖其他分支的预览。**
- **合并到 `main`：检查与生产部署成功后，更新 [正式官网 unipat.ai](https://unipat.ai)。**
- 当前预览为公网 HTTP，暂不需要飞连。飞书私信和邮件自动通知尚未接入，请通过上述 Actions 入口取链接。

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
preview on the test server. Follow [获取分支预览地址](#获取分支预览地址) above to
find and share its URL. Subsequent pushes update that same URL; deleting the
branch removes its preview. No PR is needed to get a preview.

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
