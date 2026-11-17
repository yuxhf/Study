from pathlib import Path
b=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026/翻译源稿');p=b/'04_FastToG.md';s=p.read_text(encoding='utf8')
a=s.index('初始阶段：1 从x提取实体');z=s.index('## 附录B Graph2Text细节',a)
s=s[:a]+'''初始阶段：

1. c₀ ← 从x提取实体。
2. C* ← LCS(x,c₀,π,Ω,Rmax,W)。
3. 将C*中每个c*分别追加到P中对应pᵢ。

推理阶段（行号按原文重起）：

1. I ← 0。
2. 当I<Imax时循环。
3. 对P中的每条pᵢ。
4. cᵢᴵ ← 获取pᵢ的最后一个社区。
5. c* ← LCS(x,cᵢᴵ,π,Ω,Rmax,1)。
6. 将c*追加到pᵢ。
7. 将c*加入H。
8. 结束逐链循环。
9. Ptext ← Community2Text(P)。
10. 若reasoning(π,x,Ptext)为真。
11. 跳出。
12. 结束条件分支。
13. I加1。
14. 结束循环。
15. 若I≤Imax。
16. reasoning(π,x)，使用IO、CoT。
17. 结束条件分支。

译注：第15行条件照录原文，与正文“耗尽后回退”可能不一致，不擅自修正。

算法2 局部社区搜索LCS。输入查询x、当前社区c、LLM π、图谱Ω、子图最大半径Rmax、候选社区数N。

1. g ← subgraph(c,Ω,Rmax)。
2. C ← community_detection(g)。
3. C′ ← coarse_pruning(C−H,c)，基于模块度。
4. gtext ← Community2Text(g)。
5. C″ ← fine_pruning(C′,x,π,N)。
6. 返回C″。

''' +s[z:]
s=s.replace('社区C描述“Piaroa属首次记录来自中美洲；巴拿马作者Carlos Vásquez写过……”','社区C描述“Piaroa Villarreal, Giupponi & Tourinho, 2008属的首次记录来自中美洲；Carlos Vásquez是一位巴拿马作者，他曾写过……”')
s=s.replace('图7：Graph2Text在不同社区最大大小下的幻觉率。','图7：Graph2Text在不同社区最大大小下的幻觉率。图中Max Size为社区最大大小，Hallucination Ratio为幻觉比例；CWQ和WebQSP为数据集名。')
p.write_text(s,encoding='utf8')
import re,json
out={}
for name,n in [('04_FastToG',11),('05_HippoRAG2',19)]:
 t=(b/(name+'.md')).read_text(encoding='utf8'); pages=[int(x) for x in re.findall(r'<!-- source-page: (\d+) -->',t)]
 out[name]={'pages_expected':n,'pages_marked':pages,'missing_page_markers':sorted(set(range(1,n+1))-set(pages)),'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',t)),'broken_image_links':[x for x in re.findall(r'!\[[^]]*\]\(([^)]+)\)',t) if not (b/x).exists()]}
(b/'04_05_覆盖核验.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(out,ensure_ascii=False,indent=2))
