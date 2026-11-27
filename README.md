# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-27。共 27 期、233 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-27 09:06 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 188,242 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 32,586,689 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-27

**模型文档能力与代理运行时更新**

Patram 1.5 发布 Apache 2.0 权重，下载需登录并接受访问条件；O-RAN 汇报 AI 网络试验，llama.cpp 与 Qwen Code 更新。

每日精选，第 027 期。收录范围：2026-11-26 09:00 至 2026-11-27 09:00（Asia/Singapore）；收录有可核对原始发布时间的独立消息。
实际首次整理：2026-11-27 09:06 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. BharatGen 发布 7B 文档视觉语言模型 Patram 1.5

![Patram 1.5 模型信息。参数量：7.8B，官方模型卡列出的具体参数量；任务：读 · 解析 · 问答 · 抽取，可输出 Markdown、HTML 或 JSON；厂商评测：83 分 / 49 项，BharatGen 公布的综合结果；许可与下载：Apache 2.0 + gated，下载须登录并接受访问条件](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/bharatgen-patram-15-2026-11-26.svg)

模型卡列明 Apache 2.0 与下载访问条件；评测分数及对照为 BharatGen 自报。

印度 AI 团队 BharatGen 于 11 月 26 日发布 Patram 1.5 文档视觉语言模型。正确的 Hugging Face 官方模型卡将其列为 Patram1.5-7B，具体参数量为 7.8B，许可为 Apache 2.0；仓库设有访问门槛，下载前需登录 Hugging Face 并接受访问条件。模型支持页面解析、问答和字段抽取，可输出 Markdown、HTML 或 JSON，也可通过 BharatGen Playground 试用。

BharatGen 称 Patram 1.5 在其 49 项测试中综合得分为 83，并表示模型参数规模约为最大对照模型的九十七分之一；这是厂商公布的评测结果，适用任务和条件应结合逐项结果查看。模型卡另列 OCR 3.0 与不确定时拒答能力；BharatGen 的使用说明建议运行 Patram 时准备约 24 GB GPU 显存。

分类：模型；状态：Apache 2.0 权重已发布；下载须登录并接受访问条件；原文日期：2026-11-26。

来源：[BharatGen](https://bharatgen.com/blogs/introducing-patram-1-5/)
来源：[BharatGen / Hugging Face](https://huggingface.co/bharatgenai/Patram1.5-7B)
来源：[BharatGen](https://bharatgen.com/models/vision/)

更正：2026-11-27T17:12:50.000+08:00 · 更正 Hugging Face 链接为 BharatGen 官方 Patram1.5-7B 模型卡；按模型卡补充 7.8B 参数、Apache 2.0 许可及下载需登录并接受访问条件。

## 2. O-RAN PlugFest 展示 AI 节能、故障检测与链路调节试验

![PlugFest 测试覆盖面。实验环境：16 个实验室，由 20 个主办方支持；网络运维：节能与故障检测，包括 AI 辅助硬件故障发现；链路测试：15 km Open Fronthaul，多厂商互操作场景；无线系统：64×64 mMIMO，开展检测与性能测试](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/oran-plugfest-fall-2026-results.svg)

规模与测试场景依据 O-RAN ALLIANCE 对 PlugFest 的公告；属于测试展示。

O-RAN ALLIANCE 于 11 月 26 日公布 2026 年秋季 Global PlugFest 结果。该轮活动有 47 家组织参与，在 16 个实验室开展测试，并由 20 个主办方支持；展示方向包括网络节能、硬件故障检测、远程驾驶场景的上行链路调节、AI 感知与物理 AI 应用。

联盟还列出多厂商互操作测试：包括多运营商共享无线单元、15 公里 Open Fronthaul 链路，以及完整规模的 64×64 大规模 MIMO 系统。公告总结的是 PlugFest 测试和演示，不等同于相关能力已在运营商网络规模部署。

分类：基础设施；状态：PlugFest 测试结果公告；原文日期：2026-11-26。

来源：[O-RAN ALLIANCE](https://www.o-ran.org/press-releases/o-ran-global-plugfest-fall-2026-showcased-ai-driven-solutions-that-improve-network-operations-and-enable-new-use-cases)
来源：[O-RAN ALLIANCE](https://mediastorage.o-ran.org/o-ran-pr/pr-on-o-ran-global-plugfest-fall-2026-results/o-ran-ec-2026-11-26-pr-o-ran-global-plugfest-fall-2026-results-v02.pdf)

## 3. llama.cpp v1.1.0 扩展模型、音频能力与量化选项

![版本更新的三个层面。模型支持：Inkling 2 · Hy4 flash 等，新增多款模型加载支持；多模态：语音与音频扩展，加入多种 TTS 与实时语音模型；推理与量化：DFlash · target_bpw，新增草稿模式及目标量化参数；API 迁移：llama_batch 弃用，建议关注 llama_batch_ext 与 llama_process](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/llama-cpp-v1-1-0-2026-11-26.svg)

功能与 API 变更依据 llama.cpp v1.1.0 发布说明。

开源推理项目 llama.cpp 于 11 月 26 日发布 v1.1.0。版本加入 Inkling 2、Domyn Edge 4B、Zaya1 8B、RAON-1-mini 和 Hy4 flash 等模型支持，并扩展 Kokoro、Zonos3-Mini、MiniMax-Music3、Fish S2、VoxCPM2 等语音或音频处理能力。

开发者还拆分了 DFlash 推测解码的草稿方法，增加按目标 bpw 或模型大小选择逐张量量化的参数，并改进服务端 slot 调度与聊天界面。旧的 `llama_batch` API 被标记弃用，迁移方向为 `llama_batch_ext` 与 `llama_process`；项目更新说明列出的兼容调整值得集成方在升级前核对。

分类：开源；状态：开源项目 v1.1.0 已发布；原文日期：2026-11-26。

来源：[ggml-org / llama.cpp](https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0)

## 4. Qwen Code 更新托管会话暂停恢复与崩溃恢复

![托管会话的暂停与恢复。等待：审批 · 问答 · 后台任务，托管会话可暂停等待；发生崩溃：Harness 重启，会话支持冷恢复；恢复执行：延续原会话，工具审批状态可继续处理；语言显示：简中 / 英语 / 关闭，原始回复与思考仍保留](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/qwen-code-v0-28-6-2026-11-26.svg)

会话状态和语言设置依据 Qwen Code v0.28.6 发布说明。

Qwen Code 于 11 月 26 日发布 v0.28.6，为托管会话增加等待工具审批、用户答复或后台工作时暂停，并在 Harness 崩溃或重启后恢复的能力。无头会话和 Ink 终端界面默认切换到事件总线内核；发布说明称取消的运行会在 10 秒内结束。

新版还增加 `general.displayLanguage`，可在关闭、简体中文和英语之间选择终端与 Web Shell 的回复显示语言，同时保留原始内容。用户发送新提示时，正在执行的 shell 命令会转入后台继续运行，并把任务编号、输出位置和状态交回模型。该版本同时移除了旧的 MessageRewriteMiddleware，使用 hook 路径处理回复改写。

分类：开源；状态：开源项目 v0.28.6 已发布；原文日期：2026-11-26。

来源：[QwenLM / qwen-code](https://github.com/QwenLM/qwen-code/releases/tag/v0.28.6)

**历史归档**

- [2026-11-27 · 模型文档能力与代理运行时更新](archive/2026-11-27.md)
- [2026-11-26 · 模型可靠性、企业代理与轨道算力的新进展](archive/2026-11-26.md)
- [2026-11-22 · 自主武器规则、AI 数学验证与提示数据披露](archive/2026-11-22.md)
- [2026-11-21 · AI 安全、研究评测与市场信号更新](archive/2026-11-21.md)
- [2026-11-20 · AI 开始接手桌面操作，模型工具链与算力合作同步扩展](archive/2026-11-20.md)
- [2026-11-19 · AI 产品扩展与企业基础设施更新](archive/2026-11-19.md)
- [2026-11-18 · 模型、企业 AI 与算力更新](archive/2026-11-18.md)
- [2026-11-17 · 模型发布、Agent 产品与 AI 基建治理](archive/2026-11-17.md)
- [2026-11-16 · 平台治理、云服务恢复与芯片出口审查](archive/2026-11-16.md)
- [2026-11-14 · AI 数据、代理支付与基础设施的新进展](archive/2026-11-14.md)
- [2026-11-13 · 模型进入产品，AI 基础设施继续扩张](archive/2026-11-13.md)
- [2026-11-12 · 本地智能体、机器人模型与多模态决策工具更新](archive/2026-11-12.md)
- [2026-11-11 · 前沿模型、企业智能体与 AI 芯片更新](archive/2026-11-11.md)
- [2026-11-10 · 模型、算力与 AI 工具迎来新一轮更新](archive/2026-11-10.md)
- [2026-11-09 · AI 供电、监管与芯片治理出现新进展](archive/2026-11-09.md)
- [2026-11-08 · 助手工作区、折叠屏应用与 AI 算力项目](archive/2026-11-08.md)
- [2026-11-07 · AI 走进实验室、助手与制造现场](archive/2026-11-07.md)
- [2026-11-06 · AI 安全、机器人与算力建设迎来新进展](archive/2026-11-06.md)
- [2026-11-05 · AI 工具走向工程、研究与企业系统](archive/2026-11-05.md)
- [2026-11-04 · AI 进入工程、教育与企业工作流](archive/2026-11-04.md)
- [2026-11-03 · 模型、算力基础设施与企业 AI 应用继续推进](archive/2026-11-03.md)
- [2026-11-01 · 开放模型、智能体与安全机制迎来新进展](archive/2026-11-01.md)
- [2026-10-29 · 前沿模型、智能体工具与企业部署继续扩展](archive/2026-10-29.md)
- [2026-10-28 · 模型研究、企业代理与 AI 基础设施的多线推进](archive/2026-10-28.md)
- [2026-10-27 · 企业 AI 加入流程与数据层，终端和资本市场出现新动作](archive/2026-10-27.md)
- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
