# [17] An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection：定向核验笔记

核验日期：2026-11-17。用途：研究辅助，不是课程综述正文。

## 身份与来源

- paper_id：usenix:security24/yan
- 正式出处：33rd USENIX Security Symposium 2024；1795–1812。
- [正式记录](https://www.usenix.org/conference/usenixsecurity24/presentation/yan)；[本次阅读来源](https://www.usenix.org/system/files/usenixsecurity24-yan.pdf)。
- 本次进度：全文已取得，定向阅读方法、关键实验及局限；未完成所有附录逐项核查或独立复现实验。PDF/text位于同级sources/paper_17.pdf、paper_17.txt。

## 研究定位

- 问题：生成后静态和LLM审查能否识别经过伪装但保留危险行为的补全？
- 意义：将检测规避从训练数据延伸到实际生成输出，适合检验单一检测器的盲区。
- 方法：CODEBREAKER用LLM辅助变换危险载荷，对不同触发形式、静态分析及LLM检测器开展评估。
- 已核数值：Table3（PDF p.10，正文1804）：jinja2/text/epoch1下CB-GPT有23/40个提示出现危险补全、185/400份补全危险；SIMPLE154/400危险补全经所测后置检测变为0。
- 边界：所测工具、规则、版本和漏洞实例上的规避；不能声称绕过所有安全工具，也不能将23/40和185/400混为同一指标。

## 表格与可用性说明

- 官方PDF共19页（含封面），正文从PDF p.2开始，定位时须避免偏移一页。正式URL提供出版记录。
- Table4（PDF p.10、正文1804）：Case1中CB-SA/CB-GPT/CB-ChatGPT的相关恶意输出可正常执行比例分别97.2%/98.2%/84.6%，对应相关输出集合1291/1368/1007，不能当检测召回率。
- Table6（PDF p.12、正文1806）覆盖15种漏洞，报告Semgrep、Bandit、Snyk Code、CodeQL、SonarCloud和GPT检测。部分格为不适用；“100%通过”必须带具体工具与漏洞条件，例如direct-use-of-jinja2对CodeQL为92%，不是全工具100%。
- 论文是攻击评估而非完整防御方案；代码模型后门与源程序人为后门是不同对象（正文脚注2）。
- 本研究只需记录威胁机制及验证盲点，不需要重现攻击操作。

## Word摘要卡

- 研究问题：生成后静态和LLM审查能否识别经过伪装但保留危险行为的补全？
- 意义：将检测规避从训练数据延伸到实际生成输出，适合检验单一检测器的盲区。
- 方法：CODEBREAKER用LLM辅助变换危险载荷，对不同触发形式、静态分析及LLM检测器开展评估。
- 实验与页码：Table3（PDF p.10，正文1804）：jinja2/text/epoch1下CB-GPT有23/40个提示出现危险补全、185/400份补全危险；SIMPLE154/400危险补全经所测后置检测变为0。
- 局限：所测工具、规则、版本和漏洞实例上的规避；不能声称绕过所有安全工具，也不能将23/40和185/400混为同一指标。
- 作者写作任务：比较TrojanPuzzle的训练期规避与CODEBREAKER的双阶段规避，提出独立验证证据要求。
