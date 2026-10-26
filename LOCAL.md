# Seven Tech Newsroom · 本地样刊使用说明

这是一个可以完整本地预览的静态站，共两期回溯样刊、12 条新闻、4 类数据观察、RSS 和 Atom。正式发布与定时任务见 [运行说明](OPERATIONS.md)。

需要 Python 3.10 或更新版本。构建、预览与采集均使用 Python 标准库，无需安装 npm 包或启动数据库。

**启动**

在本目录运行：

```sh
python3 preview.py
```

浏览器会打开本地首页。默认地址为 `http://127.0.0.1:4173/`；用 Ctrl+C 停止。仅监听本机回环地址。

也可以双击本目录的 `启动预览.command`。预览响应禁用缓存；修改后已打开的页面仍需刷新一次。

端口被占用时可以运行：

```sh
python3 preview.py --port 4180
```

RSS 中的本地地址会按选定端口同步重新生成。阅读器需要在能够访问该本机地址的环境中运行。

**只构建**

```sh
python3 scripts/build.py --base-url http://127.0.0.1:4173
```

静态文件生成到 `dist/`。也可直接打开 `dist/index.html` 查看新闻、筛选和图表；RSS 阅读器访问、复制权限与完整检查建议使用本地 HTTP 预览。

**文件位置**

- `content/edition.json`：两期内容和稳定事件标识，每条包含原始来源和核实时间。
- `data/snapshot.json`：本轮真实采集的价格、GitHub 和 HF 元数据。包含来源、HTTP 状态、观测时间与响应哈希。
- `data/usage.json`：核对 OpenRouter 公开页面后保存的单日用量摘录及署名，非带 Key 的 API 调用结果。
- `archive/`：按日期归档的两期 Markdown。
- `src/`：本站样式和交互；插图由构建脚本根据新闻事实生成 SVG。
- `scripts/build.py`：生成网页、README、归档、RSS 和 Atom。
- `scripts/collect.py`：只读采集公开元数据，手动执行；不生成或核实新闻。
- `build-manifest.json`：内容批次、基础地址与构建清单。
- `REVIEW.md`：本轮验证与已知边界。

**刷新指标**

```sh
python3 scripts/collect.py
python3 scripts/build.py
```

刷新会保存原有指标快照到 `data/observations/`，然后采集新快照。当前界面仍只展示横截面，不自动将两次手动调用包装成每日趋势。`usage.json` 为人工核对摘录，collect 不会更新它。两期新闻也不会随采集脚本自动改写。

**真实内容与时间边界**

10 月 23 日与 26 日是内容期号。两期均于 10 月 27 日整理，RSS 的 pubDate 使用实际首次整理时刻。原文日期独立保存；南北阁和 Moli 的正式首次发布日未确认，作为项目观察收录。不存在过去已运行过自动日报的主张。

当前指标快照于 10 月 27 日采集；OpenRouter 日榜统计日期是 10 月 25 日 UTC。两期没有伪造各自历史指标。价格是聚合路由的标示基本费，下载是滚动 30 日量，Stars 是跟踪池项目总量。

原始网页材料只用于本轮核对，没有将第三方全文或图片打包到站内。本站新闻插图为原创事实示意。OpenRouter 用量摘录按 CC BY 4.0 署名；第三方新闻、数据与标识保留原有权利。

正式发布默认使用 config/site.json 的公共基础地址；本地预览会单独生成本机地址。
