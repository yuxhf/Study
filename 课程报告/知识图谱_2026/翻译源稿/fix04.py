from pathlib import Path
p=Path('E:/GroupMT/study-report/课程报告/知识图谱_2026/翻译源稿/04_FastToG.md')
s=p.read_text(encoding='utf-8-sig')
a=s.index('表7 微调样例：');b=s.index('## 附录C 提示设计',a)
s=s[:a]+'''表7 Graph2Text微调数据样例。输入与生成文本逐项如下。

样例1输入：(Acharya Institute of Technology，昵称，“AIT”)。生成文本：“Acharya Institute of Technology称为AIT。”

样例2输入：(United States，领导人姓名，Barack Obama)；(United States，首都，Washington, D.C.)；(1634: The Ram Rebellion，国家，United States)；(United States，族群，Asian Americans)。生成文本：“《1634 The Ram Rebellion》在美国写成，Native Americans是美国的一个族群。该国首都为Washington DC，总统为Barack Obama。”译注：输入Asian Americans与输出Native Americans不一致，保留原例。

样例3输入：(A.E Dimitra Efxeinoupolis，位置，Greece)；(Greece，货币，Euro)；(Greece，领导人，Alexis Tsipras)；(Greece，领导人，Prokopis Pavlopoulos)；(Greece，语言，Greek language)。生成文本：“Alexis Tsipras领导希腊，Prokopis Pavlopoulos也是该国领导人。希腊的货币为欧元，使用希腊语。A.E Dimitra Efxeinoupolis俱乐部位于希腊。”

表8 Graph2Text幻觉类型样例，逐栏翻译如下。

样例1输入三元组：(The Gentlemen，演员，Charlie Hunnam)；(The Gentlemen，类型，action film动作片)；(The Gentlemen，发行方，Netflix)；(Go，类型，action film动作片)。生成文本：“Charlie Hunnam是The Gentlemen的演员。The Gentlemen是Netflix发行的动作片，也称为Go。”幻觉类型：逻辑不一致。原因栏：“LoGentlemen和Go都是动作片。”译注：LoGentlemen为原表字样，不能从两个作品同类型推出二者同名。

样例2输入三元组：(Charlie Hunnam，就读于，University of Cumbria)；(Peter Strike，雇主，University of Cumbria)；(Portrait, Interior II* (triptych, centre panel)，位置，University of Cumbria)；(Still Life Fruit，收藏机构，University of Cumbria)。生成文本：“Charlie Hunnam曾就读于University of Cumbria。Peter Strike受雇于University of Cumbria，并拥有Still Life Fruit藏品。肖像Portrait, Interior II*是University of Cumbria的一幅三角形图像。”幻觉类型：事实不一致。原因栏：“Portrait, Interior II*是一个地点。”译注：作品名、三联画中间幅描述及原表原因存在可疑之处，逐项保留，不将该理由视为另行核实的事实。

调查后，我们将幻觉概括为事实不一致和逻辑不一致两类。前者为实体表示中的不准确或捏造，后者为实体关系错误。调查中标为错误的文本，意味着该文本确含幻觉，但并非所有语句都有幻觉。这解释了正文图4中社区增大时准确率并未急剧下降。

''' +s[b:]
s += '''

图8图内文字逐项译注：Start Community=起始社区；Community-Edge Chains=社区—边链；current community=当前社区；candidate communities=候选社区；pruning prompt=剪枝提示；Premise=前提；Question: xxx ?=问题：xxx？；Selection=选项；Your selection=你的选择。其提示结构为“前提：T2T/G2T(S)+…+T2T/G2T(P3)；问题：xxx？；选项：A. T2T/G2T(A)，B. T2T/G2T(B)，C. T2T/G2T(C)，…；你的选择：”。S、P1、P2、P3、A、B、C为节点或社区标识，不翻译。

图9图内文字逐项译注：Start Community=起始社区；Community-Edge Chains=社区—边链；reasoning prompt=推理提示；Context=上下文；Question: xxx ?=问题：xxx？；Your Answer=你的回答。提示结构为“上下文：1. T2T/G2T(S)；2. T2T/G2T(A1)+…+T2T/G2T(A3)；3. T2T/G2T(B1)+…+T2T/G2T(B3)；4. T2T/G2T(C1)+…+T2T/G2T(C3)；问题：xxx？；你的回答：”。S与A1—C3为原图标识。
'''
p.write_text(s,encoding='utf-8')
