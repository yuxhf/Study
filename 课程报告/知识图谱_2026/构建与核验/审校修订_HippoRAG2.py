from pathlib import Path
b=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026');p=b/'翻译源稿/05_HippoRAG2.md';s=p.read_text(encoding='utf8')
pairs=[
('简单问答：从NaturalQuestions','简单问答：这类常见任务主要围绕单一实体提问，因此特别适合嵌入模型直接检索相关上下文。从NaturalQuestions'),
('问答方面，HippoRAG 2平均F1最高，跨设置稳健。','问答方面，表2以Llama-3.3-70B-Instruct为问答阅读器，HippoRAG 2平均F1最高，跨设置稳健。'),
('支持神经心理学启发设计的有效性。附录表8','支持神经心理学启发设计的有效性。这些结果表明，HippoRAG 2是一套先进RAG系统，能够由开源模型有效驱动，同时提高检索与问答性能。附录表8'),
('各方法token、时间、内存分析见附录F。检索方面，','各方法token、时间、内存分析见附录F。检索方面，表3只报告拥有支持文段标注的数据集，以及显式检索文段的模型结果。'),
('(I.P. Paul,from,Thrissur)、(I.P. Paul,was mayor of,Thrissur municipal corporation)','(I.P. Paul，来自，Thrissur)、(I.P. Paul，曾任其市长，Thrissur municipal corporation特里苏尔市政机构)'),
('并在图搜索把其文段排第二。','并在随后图搜索把该实体对应文段排第二，作者称之为“完美的检索结果”。'),
('(Erik Hort,born in,Montebello)、(Erik Hort,born in,New York)','(Erik Hort，出生于，Montebello)、(Erik Hort，出生于，New York)'),
('图搜索前三为Erik Hort、Horton Park、Montebello,New York。','图搜索前三为Erik Hort、Horton Park、Monstebello,New York（原表6拼写；正文及图5作Montebello）。'),
('正文称识别了Philippe不一致','正文称识别了Philippe不一致')
]
miss=[]
for a,z in pairs:
 if a not in s:miss.append(a)
 else:s=s.replace(a,z,1)
# Source Table 6 titles remain proper names, with natural-language title fragments translated.
s=s.replace('Yinka Ayefele—Early life、Paul Parker(singer)','Yinka Ayefele—Early life（早年生活）、Paul Parker(singer，歌手)')
s=s.replace('Monstebello,New York（原表6拼写；正文及图5作Montebello）。Montebello文段含暗示答案的地理信息。','Monstebello,New York（原表6拼写；正文及图5作Montebello）。在查询到三元组阶段检索到的Montebello文段含暗示答案的地理信息，随后图搜索也将其排在前列。')
s=s.replace('“7点关联性改善”','“7点关联性改善”')
# Clarify that the abstract and introduction use different improvement wording, without changing either.
s=s.replace('## 2 相关工作','译注：摘要原文使用“7% improvement”，引言使用“an average 7 point improvement”。两处分别保留为“提高7%”和“平均提高7点”，不将其擅自统一为某一相对增幅或百分点计算。\n\n## 2 相关工作',1)
# Preserve the original inconsistent table values, with explicit location-specific annotations.
s=s.replace('全部数值保留原表，不因个别加总疑点修改。','全部数值保留原表，不因个别加总疑点修改。译注：GPT-4o-mini的PopQA“总边数”原值为494,082，但该列三类边数108,989、901,528、127,568之和为1,138,085；原文未解释这一差异，本译稿保留原值。')
s=s.replace('完整原表保留于影印件。\n\n|资源|','完整原表保留于影印件。译注：LightRAG每查询13.3秒旁原比例为1008.3%，与HippoRAG 2的1.2秒直接相除不一致；其他个别舍入／比例也按原表保留，未重算覆盖。\n\n|资源|',1)
p.write_text(s,encoding='utf8');print('unmatched',miss)
