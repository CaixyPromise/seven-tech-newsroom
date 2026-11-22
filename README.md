# Seven Tech Newsroom

每天五分钟，读有来源的 AI / 科技新闻，查看独立标时的数据观察。

[访问网站](https://caixypromise.github.io/seven-tech-newsroom/) · [RSS](https://caixypromise.github.io/seven-tech-newsroom/feed.xml) · [源码仓库](https://github.com/CaixyPromise/seven-tech-newsroom) · [作者主页](https://github.com/CaixyPromise) · [运行说明](OPERATIONS.md)

最近一期：2026-11-22。共 25 期、215 条独立记录；按实际发布状态与来源标时。

**最新数据快照**：2026-11-22 08:59 UTC+8；OpenRouter 日榜另截至 2026-10-31 UTC。

| 观察项 | 最新观测 | 范围 |
| --- | --- | --- |
| 模型基本费估算 | $0.00135 · MiniMax M3.1 Flash | 7 个选定模型，10K 输入 + 2K 输出 Token |
| 平台单日用量 | 约 7.09T Token · DeepSeek V4.1 Flash 1017 | OpenRouter 2026-10-31 UTC 公开日榜 |
| 开源关注 | 187,792 Stars · ollama/ollama | 本站固定跟踪的 6 个项目 |
| 文本模型下载 | 34,152,708 · openai-community/gpt2 | HF 文本生成类，近 30 日滚动量 |

来源：[OpenRouter 模型目录](https://openrouter.ai/api/v1/models)、[OpenRouter 日榜](https://openrouter.ai/rankings)、[GitHub Repository API](https://docs.github.com/en/rest/repos/repos#get-a-repository)、[Hugging Face Hub](https://huggingface.co/docs/hub/en/api)。OpenRouter 日榜数据按 CC BY 4.0 署名。

## 最新一期 · 2026-11-22

**自主武器规则、AI 数学验证与提示数据披露**

Lean 社群确认一项 AI 协助的黎曼猜想形式化证明；OpenRouter 提醒部分用户检查 MiniMax 请求的隐私风险；联合国自主武器谈判结果仍待正式文本完整呈现。

每日精选，第 025 期。收录范围：2026-11-21 09:00 至 2026-11-22 09:00（Asia/Singapore）；按来源原始发布时间换算核对。
实际首次整理：2026-11-22 09:24 UTC+8。
指标按实际保存的批次与采集时间查看。

## 1. Lean 与 Mathlib 社群确认黎曼猜想形式化证明

![黎曼猜想证明的核验链。定理表述：与 Mathlib 一致，比较工具核对命题内容；形式化代码：约 1,700 万行，社区成员复现编译；检查器：多种工具通过，Lean 内核及独立检查器](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/riemann-hypothesis-lean-confirmation-2026-11-21.svg)

依据 Lean 与 Mathlib 社群 11 月 21 日联署声明；论证的学术理解仍在继续。

Lean 与 Mathlib 社群 11 月 21 日发布联署声明，确认 Levent Alpöge 与 Claude 协作完成的 Lean 形式化文件，所证明的命题确为黎曼猜想，且证明通过了多种检查器验证。文件约有 1,700 万行代码；社群称多名成员已复现编译结果。

Alpöge 于前一日公布这项结果，形式化代码随后接受社群审查。声明称，比较工具确认代码定理与 Mathlib 中经过审查的黎曼猜想表述一致；Lean 内核及其他独立检查器也接受了证明。

简评：形式化检查让证明的复核路径更可重复，但数学界仍需理解其论证结构；机器验证、同行审读与学术机构认定是不同环节。

分类：研究；状态：Lean 与 Mathlib 社群联署确认形式化证明正确；原文日期：2026-11-21。

来源：[Lean 与 Mathlib 社群](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
来源：[滑铁卢大学 Michael Rubinstein](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
来源：[Associated Press](https://apnews.com/article/anthropic-claude-math-solution-ai-4fe8b69a891f160f9e7f0c85af8c55c8)

## 2. OpenRouter 提醒用户：部分 MiniMax 请求可能被读取

![从研究测试到客户提醒。2026 年 7—11 月：约 200 万条测试提示，Dragos 植入唯一标记并追踪访问；2026 年 11 月 21 日：部分客户收到提醒，MiniMax 相关请求可能被读取；后续处置：移除相关留存标记，OpenRouter 称受影响端点已调整](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/openrouter-minimax-prompt-notice-2026-11-21.svg)

客户邮件经公开转贴；研究与邮件均指向特定请求路径，不代表全部对话泄露。

OpenRouter 于 11 月 21 日开始向部分客户发送邮件，称用户在 2026 年 7 月至 10 月间发给 MiniMax 模型的部分请求可能被第三方读取。邮件内容由客户公开转贴；OpenRouter 表示风险涉及 MiniMax 及将请求转发给该模型的服务商，并已移除相关端点的“零数据留存”标记。

该提醒源于 Dragos 团队的测试：研究人员称，他们在 2026 年 7 月至 11 月向 AI 服务提交约 200 万条含唯一网址或测试凭据的提示，并追踪之后是否有人访问。团队报告了提示被转售、服务商遭入侵和隐私设置未落实等不同情形；这些结果不代表所有 MiniMax 对话均被读取。

简评：多层路由让每个转发环节都可能接触提示内容；采购服务时，除了查看留存标签，也应确认请求会经过哪些提供商。

分类：治理；状态：供应商邮件提醒；受影响请求范围仍需按账户核对；原文日期：2026-11-21。

来源：[Hacker News 用户公开转贴的 OpenRouter 邮件](https://news.ycombinator.com/item?id=50585962)
来源：[Ars Technica](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/)
来源：[Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

## 3. 联合国自主武器规则谈判未启动，媒体称工作延至 2028 年

![自主武器规则谈判进展。会议时间：11 月 16—20 日，联合国会议文件所载会期；会议结果：未启动正式谈判，尚未形成具约束力规则；后续时限：2028 年前拟订，据 AP 报道，正式文本待核](https://caixypromise.github.io/seven-tech-newsroom/assets/visuals/ccw-autonomous-weapons-talks-2026-11-21.svg)

联合国修订文件仍有条款占位；2028 年安排依 AP 报道，后续以完整正式文本为准。

联合国《特定常规武器公约》第七次审议会议于 11 月 20 日在日内瓦结束。Associated Press 于 11 月 21 日报道，各国同意推动在 2028 年前拟订关于致命自主武器系统的可能协议，但没有启动具约束力规则的谈判。

奥地利、比利时、巴西、爱尔兰、墨西哥、新西兰和巴拿马此前提出启动正式谈判。联合国公开的会议文件确认会期为 11 月 16 日至 20 日，但当前修订版本仍将自主武器相关条款留作占位；因此，2028 年时间表目前以 AP 对会议结果的报道为依据，完整正式文本尚待核对。

简评：现阶段可以确认的是，会议没有形成新的约束性规则；后续是否出现正式谈判授权，还要看联合国最终公布的完整文件。

分类：治理；状态：正式谈判未启动；2028 年安排据 AP 报道，联合国完整文本待核；原文日期：2026-11-21。

来源：[Associated Press](https://apnews.com/article/un-drones-robots-un-lethal-ai-weapons-ebe057d2a47cde53100970c8f648e7fa)
来源：[联合国裁军事务厅](https://docs-library.unoda.org/Convention_on_Certain_Conventional_Weapons_-SeventhReview_Conference_%282026%29/CCW-CONF.VII-CRP.1-Rev.2.pdf)
来源：[Asia-Pacific Institute for Law and Security](https://apils.org/2026/11/21/ccw-seventh-review-conference-a-new-mandate-on-autonomous-weapons-but-no-review/)

**历史归档**

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
