# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-20。共 23 期、206 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-20 09:02 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.00135 · MiniMax M3.1 Flash | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 187,672 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 34,336,215 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-20

**AI 开始接手桌面操作，模型工具链与算力合作同步扩展**

本期聚焦桌面电脑操作、生成式世界 API、按需加载工具、量子处理器实验，以及 AI 基础设施和健康功能的新进展。

每日精选，第 023 期。收录范围：2026-11-19 09:00 至 2026-11-20 09:00（Asia/Singapore）；按原始来源发布日期核对。。
实际首次整理：2026-11-20 09:03 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Google 在 Gemini Mac 应用中推出电脑操作功能

![从指令到桌面任务。输入：描述多步骤任务，涵盖本地文件、应用与网站；执行：后台窗口操作，点击、输入与填写表单；控制：预览并确认，可暂停，关键操作前审批](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-gemini-mac-computer-use-2026-11-19.svg)

美国英语版逐步开放；关键操作仍需用户确认。

Google 于 11 月 19 日在 Gemini Mac 应用中推出电脑操作功能，可根据用户指令在本地文件、桌面应用和网站间点击、输入及填写表单，处理多步骤任务。功能在独立后台窗口运行，用户可以查看实时预览、随时暂停，并在关键操作前确认。

该功能目前以英语向美国地区逐步开放，适用于年满 18 岁的个人 Google 账号及 Google AI Plus、Pro、Ultra 用户；设备需使用 Apple Silicon 芯片并运行 macOS Sequoia 15.0 或更新版本。Google 将其定位为减少重复操作的助手，实际执行仍受用户授予的应用权限和确认步骤约束。

分类：产品；状态：美国英语用户逐步开放；原文日期：2026-11-19。

来源：[Google](https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/)

更正：2026-11-20T01:07:43.492611+00:00 · 补充原始页面结构化元数据中的精确发布时间；发布日期与正文未变。

## 2. Genie 4 开放 Gemini API 与 AI Studio 开发者试用

![可实时操控的生成场景。输入：文字或参考图，也可同时提供两者；画面：720p · 24fps，连续生成场景；交互：键盘与文字提示，运行中调整天气、物件或事件；声音：同步原生音频，含环境声、音效和对白](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-genie4-gemini-api-2026-11-19.svg)

分辨率、帧率和音频规格据 Google 公告。

Google 于 11 月 19 日宣布，开发者可通过 Gemini API 的 Interactions API 和 Google AI Studio 使用 Genie 4。模型可从文字提示、参考图或两者生成连续的 720p 场景，输出为每秒 24 帧并带同步原生音频，开发者也能在运行中用键盘和文字提示改变环境。

Google 表示，场景可包含环境声、音效和角色对白，输出带有 SynthID 水印；公司列出的用途包括互动体验原型、空间概念展示和机器人及 AI agent 训练。前一天推出的 Project Genie 面向部分 Google AI Ultra 用户，此次 API 开放则扩展到开发者渠道；公告未在该文中给出价格或一般可用时间表。

分类：产品；状态：开发者可试用；原文日期：2026-11-19。

来源：[Google](https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/)

更正：2026-11-20T01:07:43.492611+00:00 · 补充原始页面结构化元数据中的精确发布时间；发布日期与正文未变。

## 3. Gemini API 预览按需加载工具参数方案

![工具参数改为按需载入。工具库：名称与描述可见，完整参数 schema 暂缓载入；选择：模型发起搜索，通过 tool_search 请求所需工具；调用：载入参数后执行，本次请求中继续函数调用](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-gemini-api-tool-retrieval-2026-11-19.svg)

预览功能；token 按所用模型标准费率计费。

Google 于 11 月 19 日在 Gemini Interactions API 预览 Tool Retrieval。过去，agent 调用大量工具时，通常要在每次请求中附上完整参数 schema；新机制允许开发者将工具标记为延迟加载，模型先看到工具名称和描述，需要调用时再由 API 载入完整参数。

开发者需加入 tool_search 并为相应工具设置 defer_loading；此功能也支持 Gemini API 中的远程 MCP server。Google 称其可减少不必要的输入 token、延迟及工具选择干扰，但实际节省取决于会话中未被调用的工具比例；功能目前处于预览阶段，token 仍按所用模型的标准费率计费。

分类：基础设施；状态：Interactions API 预览；原文日期：2026-11-19。

来源：[Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)

更正：2026-11-20T01:07:43.492611+00:00 · 补充原始页面结构化元数据中的精确发布时间；发布日期与正文未变。

## 4. Google 在最多 105 量子比特任务中测量量子情境性

![实验胜率高于经典上限。经典上限：88.89%，Google Research 所述最佳经典策略；Willow 实验：98.30%，100,000 轮 × 9 种设置；±0.01%](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/google-quantum-contextuality-2026-11-19.svg)

Google 报告的实验结果；非通用计算基准。

Google Quantum AI 研究团队 11 月 19 日在《Science》发表关于量子情境性的实验，并称在 Willow 超导处理器上运行的魔方游戏胜率为 98.3%，高于其列出的经典策略上限 88.89%。团队称，该实验也能用于检测传统随机电路测试可能忽略的硬件误差。

研究还在最多 105 个量子比特的问题上比较量子电路与受约束的经典策略，并报告实验结果超过经典界限。团队将结果解释为量子情境性可在较大处理器任务中测量；这属于特定实验设置下的研究结果，不能直接等同于通用计算优势或已达实用容错计算。

分类：研究；状态：研究论文发表；原文日期：2026-11-19。

来源：[Google Research](https://research.google/blog/a-game-you-cannot-win-unless-you-have-a-quantum-computer/)
来源：[Science](https://www.science.org/doi/10.1126/science.aec3042)

## 5. NVIDIA 与微软扩展 Azure 和本地 AI 部署合作

![从 Azure 延伸到本地部署。云基础设施：Vera Rubin NVL72，在 Azure 数据中心运行；服务预览；模型平台：Microsoft Foundry，扩展 NVIDIA 开放模型与定制能力；本地部署：Windows PC 与工业系统，新增边缘运行选项；数据保护：机密计算与能效，双方称将扩展验证与能效合作](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/nvidia-microsoft-ai-infrastructure-2026-11-19.svg)

双方公告称 Azure Vera Rubin 服务处于预览。

NVIDIA 与微软 11 月 19 日在 Microsoft Ignite 期间公布扩大 AI 基础设施合作：搭载 NVIDIA Vera Rubin NVL72 的 Azure 虚拟机已在数据中心运行；双方还计划把 NVIDIA 开放模型和定制能力扩展至 Microsoft Foundry，并提供将 AI 工作负载部署到 Windows PC 和工业系统的选项。

两家公司同时称将把机密计算与验证能力扩展至裸金属及整机架 AI 基础设施，并合作提升数据中心能效。公告中的 Azure Vera Rubin 仍属预览，合作方也引用了自家产品和 MLPerf 测试数据；这些信息说明部署方向与厂商报告结果，不构成独立的跨平台性能比较。

分类：基础设施；状态：部分能力预览与扩展中；原文日期：2026-11-19。

来源：[NVIDIA](https://blogs.nvidia.com/blog/microsoft-ignite-accelerated-computing-azure-windows-pcs/)

更正：2026-11-20T01:07:43.492611+00:00 · 补充原始页面结构化元数据中的精确发布时间；发布日期与正文未变。

## 6. ChatGPT Health 扩展到 Android、桌面端与 Sites

![Health 扩展到更多终端。Android：Health Connect，连接健康与健身信息；桌面端：追踪训练计划，可创建 Sites 记录进展；适用账号：美国 Free 至 Pro，dots 当前仅限 Pro 用户](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openai-health-android-desktop-2026-11-19.svg)

美国账号逐步开放；连接健康数据需用户授权。

OpenAI 11 月 19 日宣布，将 ChatGPT Health 扩展至 Android、桌面应用、dots 和 Sites，并支持连接 Android Health Connect。用户可选择连接健康与健身信息，查看睡眠、活动等模式；桌面端也可创建用于追踪训练计划的网站。

该更新正逐步推出，暂面向美国的 Free、Go、Plus 和 Pro 用户；dots 当前仅对 Pro 用户开放，账号可能尚未获得入口。连接健康数据需用户授权，产品说明将其定位为帮助理解健康信息的工具，并非替代医疗服务。

分类：产品；状态：美国用户逐步开放；原文日期：2026-11-19。

来源：[OpenAI](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)

**历史归档**

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
