# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-10-26。共 2 期、12 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-10-27 01:54 UTC+8；OpenRouter 日榜另截至 2026-10-25 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.002 · Claude Haiku 5.5 | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 5.77T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-25 UTC 公开日榜 |
| 开源关注 | 184,869 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 23,729,057 · Qwen/Qwen3-0.6B | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-10-26

**AI 正在进入工具、数据与日常工作**

Hugging Face 共享缓存、Oracle 信任架构与南北阁权重，把关注点拉回到可用性。

回溯样刊，第 002 期。收录范围：2026-10-24 至 2026-10-26；含两条项目观察。
实际首次整理：2026-10-27 01:57 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Hugging Face 更新工具链：共享缓存减少重复下载

Hugging Face 汇总 hf CLI 与 huggingface_hub 的近期更新。共享缓存让不同仓库中的同一份 Xet 文件可以复用，Jobs 也加入重试与重跑等改进。

- 官方示例中的三个模型共用同一个 9.5 GB 编码器，缓存复用后无需分别存储。
- 更新还覆盖 Jobs、Storage Buckets、Sandboxes 与上传下载体验。

这是一篇近期功能汇总，不能把全部功能都视为当天首次上线。共享缓存例子也不是所有下载任务的通用节省比例。

分类：开源；状态：工具更新；原文日期：2026-10-26。

来源：[Hugging Face](https://huggingface.co/blog/huggingface/whats-new-in-the-hf-cli-and-huggingface-hub-librar)

## 2. Oracle 发布 Deep Trust AI 架构，将规则放入数据与执行层

Oracle 在 AI World 公布 Deep Trust AI 架构，围绕软件平台、数据、数据访问和应用开发四层组织企业 AI 的安全与业务约束。

- 公告提出受控数据 API 与数据库内访问规则，减少 Agent 绕过应用层约束的风险。
- 架构结合 Oracle AI Database、Autonomous AI Database 和 APEX 等产品能力。

这是厂商公布的架构蓝图。具体功能交付、部署条件和效果，应按产品文档与实际环境分别核实。

分类：基础设施；状态：架构公布；原文日期：2026-10-26。

来源：[Oracle](https://www.oracle.com/news/announcement/ai-world-oracle-announces-deep-trust-ai-architecture-to-help-enterprises-innovate-with-confidence-2026-10-26/)

## 3. 南北阁 4.3-33B 公开权重，定位 Agent 教师模型

南北阁团队公开 Nanbeige4.3-33B，定位编程与办公 Agent 的教师模型，并计划以此支持后续小模型蒸馏。

- 官方模型卡标为 Apache 2.0，说明支持最高 512K 上下文。
- 模型卡列出编程、工具使用与推理结果；这些成绩属于团队自报。

仓库创建时间为 10 月 24 日，不能直接当作正式发布时间。此条以 10 月 26 日观察收录，原始发布日暂未确认。

分类：模型；状态：权重可得 · 发布日待确认；原文日期：待确认。

来源：[Nanbeige](https://huggingface.co/Nanbeige/Nanbeige4.3-33B)

## 4. 微软发布 Learning Curves，讨论 AI 如何改变学习与就业起点

微软 AI Economy Institute 推出研究文集 Learning Curves，围绕基础教育、职业教育、从学校到工作的转变讨论 AI 的机会与分配问题。

- 文集汇集该机构第二届 Senior Fellows 的研究文章。
- 讨论覆盖教师培训、语言与数字能力、学徒制和初级工作等议题。

这是一份研究与观点文集，不是对教育成效或就业变化的因果证明。

分类：产业；状态：研究文集；原文日期：2026-10-26。

来源：[Microsoft](https://blogs.microsoft.com/on-the-issues/2026/10/26/learning-curves-the-future-of-education-from-classrooms-to-careers-in-an-ai-driven-world/)

## 5. 项目观察：Moli 为 Agent 提供按需渲染的无头浏览器

Lexmount 的 Moli 将页面结构读取与视觉渲染分开，提供 CLI、CDP 和 WebDriver 等入口，面向网页提取与浏览器自动化。

- 项目 README 说明支持 Linux、macOS 和 Windows，并采用按需布局与截图设计。
- 项目提供开源版本，默认许可为 Apache 2.0 或 MIT，第三方组件另有说明。

此条为本期项目发现，未确认最初发布日。速度、兼容性和内存表现尚未由本站独立测试，不将项目宣传作为实测结论。

分类：产品；状态：项目观察 · 发布日待确认；原文日期：待确认。

来源：[Lexmount](https://github.com/lexmount/moli)

**历史归档**

- [2026-10-26 · AI 正在进入工具、数据与日常工作](archive/2026-10-26.md)
- [2026-10-23 · 模型能力向前一步，工具与证据也要跟上](archive/2026-10-23.md)
