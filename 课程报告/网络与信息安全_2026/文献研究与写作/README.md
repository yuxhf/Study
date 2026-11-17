# 20篇全文证据与阅读状态

## 完整正文初稿

[打开课程报告完整初稿](第29题_课程报告完整初稿.md)：含摘要、约500字选题综述、20篇各300–500汉字的连续段落剖析、约2500字深度评述、方法比较表与参考文献。[核查记录](完整初稿_核查记录.md)说明证据、数据冲突与审校范围。

本稿依用户授权由主agent与三位子agent协作起草，已进行独立交叉审阅；如实标明AI辅助完整初稿、未经作者审定，未声称符合课程独立写作要求。旧工作稿保留为证据入口。


## Markdown工作稿

[打开单文件研究与写作工作稿](第29题_文献研究与写作工作稿.md)：整合20篇详细证据笔记、章节提纲、横向比较、指标定义、研究问题、数据冲突与参考来源。按后续要求提供Markdown工作格式；独立综述主体仍待作者完成。

生成脚本：`tools/build_markdown_workbook.py`。本次续接仅整合本地已有证据，没有重新核验外部书目或复现实验。

2026-11-17。三篇核心完成方法、结果、局限核查；其余17篇为定向全文阅读，不代表全附录复核、作者本人完成精读或实验复现。

|ID|论文|笔记|阅读范围|
|---|---|---|---|
|01|Security Weaknesses of Copilot-Generated Code in GitHub Projects: An Empirical Study|[阅读卡](core/paper_01.md)|方法/关键表格/局限定向阅读|
|02|Rethinking the Evaluation of Secure Code Generation|[阅读卡](core/rethinking.md)|核心核查|
|03|Can You Really Trust Code Copilot? Evaluating Large Language Models from a Code Security Perspective|[阅读卡](core/copilot.md)|核心核查|
|04|SecCoder: Towards Generalizable and Robust Secure Code Generation|[阅读卡](core/paper_04.md)|方法/关键表格/局限定向阅读|
|05|Teaching an Old LLM Secure Coding: Localized Preference Optimization on Distilled Preferences|[阅读卡](core/paper_05.md)|方法/关键表格/局限定向阅读|
|06|SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-Aware Fine-Tuning|[阅读卡](core/securereviewer.md)|核心核查|
|07|Repairing LLM Executions for Secure Automatic Programming|[阅读卡](core/paper_07.md)|方法/关键表格/局限定向阅读|
|08|GoodVibe: Security-by-Vibe for LLM-Based Code Generation|[阅读卡](core/paper_08.md)|方法/关键表格/局限定向阅读|
|09|Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection|[阅读卡](core/paper_09.md)|方法/关键表格/局限定向阅读|
|10|Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications|[阅读卡](core/paper_10.md)|方法/关键表格/局限定向阅读|
|11|Beyond Functional Correctness: Exploring Hallucinations in LLM-Generated Code|[阅读卡](core/paper_11.md)|方法/关键表格/局限定向阅读|
|12|We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs|[阅读卡](core/paper_12.md)|方法/关键表格/局限定向阅读|
|13|HFuzzer: Testing Large Language Models for Package Hallucinations via Phrase-based Fuzzing|[阅读卡](core/paper_13.md)|方法/关键表格/局限定向阅读|
|14|Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories|[阅读卡](core/paper_14.md)|方法/关键表格/局限定向阅读|
|15|Insecure Coding Preferences in Long-Term Memory: Security Risks for LLM-based Code Generation|[阅读卡](core/paper_15.md)|方法/关键表格/局限定向阅读|
|16|TrojanPuzzle: Covertly Poisoning Code-Suggestion Models|[阅读卡](core/paper_16.md)|方法/关键表格/局限定向阅读|
|17|An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection|[阅读卡](core/paper_17.md)|方法/关键表格/局限定向阅读|
|18|Stealthy Backdoor Attack for Code Models|[阅读卡](core/paper_18.md)|方法/关键表格/局限定向阅读|
|19|Generalized Adversarial Code-Suggestions: Exploiting Contexts of LLM-based Code-Completion|[阅读卡](core/paper_19.md)|方法/关键表格/局限定向阅读|
|20|Poisoned ChatGPT Finds Work for Idle Hands: Exploring Developers' Coding Practices with Insecure Suggestions from Poisoned AI Models|[阅读卡](core/paper_20.md)|方法/关键表格/局限定向阅读|

## 需要保留的纠偏

- [01]733份代码是三工具混合，Copilot为672份。
- [02]表3合计42与正文44不一致；SAFE降幅表值复算14.29%，正文28%。
- [03]检测分类集477漏洞/54无漏洞，需考虑类别偏斜；VC-Judge不是金标准。
- [06]RAG保持安全类型预测不变；微调后评论质量增益不一致。
- [07]分项结果正文与表格冲突；优先保留总告警576→489的边界。
- [10]78.41%包含正确的API/版本安全警告，不是无漏洞可运行代码比例。
- [13]2.60倍为独特幻觉包数量，2.36倍为任务多样性，二者不是同一指标。
- [14]文件数7703/7117/7696冲突，整体安全率暂不采用。
- [15]正式摘要和四模型扩展作者稿有版本差异；不混作正式版本结果。
- [18]可访问旧稿含占位内容，不能冒充正式出版PDF。

## 完成与剩余

- 已完成：20篇全文获取、结构化笔记、关键证据定位、三篇核心深入核查、两张比较表、Crossref元数据核验。
- 未完成：用户独立阅读与取舍、综述主体写作、全部附录复核、工件复现、冲突数据裁决、正式报告最终验收。
- CCF分级沿用既有清单，本轮没有再次核验2026目录；引用年份依Crossref正式出版记录，会议年份和在线/卷期年份可能不同。

## Word交付

- [文献研究与写作工作册](第29题_文献研究与写作工作册.docx)：20张证据卡、两张比较表、研究问题和参考文献。
- [作者独立写作模板](第29题_作者独立写作模板.docx)：保留原始封面，正文宋体小四、1.3倍行距、首行缩进2字符，留待作者独立填写。

原文PDF、原始指南和提取文本保存在本地sources/；仓库保留笔记、来源链接、哈希及核验元数据。本文档是研究辅助资料，不是可提交综述。


## 仓库与本地来源

本目录同步研究笔记、书目、来源哈希及作者模板。论文PDF、提取全文和原始课程指南保存在本地，来源URL见逐篇笔记；sources/evidence_manifest.json中的source_pdf是本地相对路径，不表示该PDF已上传仓库。课程要求参见[要求摘录](课程要求摘录.md)。
