# [12] We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs

paper_id: usenix:security25:spracklen。Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala；USENIX Security2025。[正式页](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)；[正式PDF](https://www.usenix.org/system/files/usenixsecurity25-spracklen.pdf)；[工件](https://github.com/Spracks/PackageHallucination)。本地21页，2026-11-17定向全文核验方法、主要结果与局限，未复现。

## 方法和结果

p6–7：16个LLM、Python/JavaScript、两类提示数据，总576,000代码样本；部分Python专用模型不测JS。通过安装命令、让模型列依赖等启发式抽取分发包名，避免把模块名直接当包名；之后对PyPI/npm和时间条件核验。

p8 §5.1：2.23百万包名出现中440,445（19.7%）被判幻觉，205,474个独特不存在包名；商业模型平均5.2%、开放模型21.7%。分母是推荐包名的出现计数，不能写成19.7%代码片段有漏洞，也不同于HFuzzer响应级PHR。

p10图5：确认幻觉的原始提示重复10次，43%在全部10次重现，58%至少重现多于一次。条件抽样为已发现幻觉的提示，不是全任务58%会重复幻觉。

p14表5：微调后DeepSeek pass@1由51.4%到25.3%，CodeLlama由19.6%到16.4%；缓解幻觉也可能损害功能。不能用摘要“maintaining code quality”笼统覆盖所有缓解方式。

## 局限与可信性

p14讨论模型时效与商业模型覆盖有限；p15伦理声明作者未向PyPI发布幻觉包以制造真实下载攻击，因此该研究说明潜在供应链攻击面，不表示观测到真实受害事件。独立判断：包名存在不保证安全，注册时间条件和抽取启发式会改变标签；不要把所有不存在模块都当作可劫持分发包。重复性、可注册性、安装行为和恶意内容仍是不同证据环节。

## Word摘要卡

- 研究问题：代码生成模型会多频繁地推荐不存在依赖，幻觉是否稳定重现？
- 意义：把代码内容安全延伸到依赖解析与安装供应链。
- 方法：生成代码、启发式提取分发包名、查询包仓库及时间信息并比较缓解措施。
- 实验与页码：p8报告576,000代码样本的2.23百万包名出现中19.7%为幻觉；p14表5微调使DeepSeek pass@1由51.4%降到25.3%。
- 局限：启发式包名判定和模型时效有限，未测真实恶意包下载安装受害率。
- 作者写作任务：自行对比响应级PHR和包名出现级幻觉率，并讨论缓解的功能代价。
