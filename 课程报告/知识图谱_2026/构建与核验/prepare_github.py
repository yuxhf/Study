from pathlib import Path
import re,json,hashlib,subprocess
root=Path(__file__).resolve().parents[1]
repo=root.parents[1]
for f in sorted((root/'翻译源稿').glob('0[1-5]_*.md')):
 t=f.read_text(encoding='utf-8')
 t=t.replace('\\[\n','$$\n').replace('\n\\]','\n$$')
 t=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m[1]+'$',t,flags=re.S)
 f.write_text(t,encoding='utf-8')
readme='''# 知识图谱课程报告

**面向大语言模型的知识图谱构建、检索与推理技术研究——以 GraphRAG 与长期记忆为例**

当前版本：二轮模型辅助审校版。报告和五篇译稿以 Markdown 阅读、修订，插图随正文存放。研究设想尚未开展新实验；原文内部矛盾已作译注。

## 阅读入口

|材料|入口|
|---|---|
|课程报告正文|[知识图谱课程报告](报告成稿/知识图谱课程报告.md)|
|第1篇全文翻译|[SAC-KG](翻译源稿/01_SAC-KG.md)|
|第2篇全文翻译|[KGP](翻译源稿/02_KGP.md)|
|第3篇全文翻译|[G-Retriever](翻译源稿/03_G-Retriever.md)|
|第4篇全文翻译|[FastToG](翻译源稿/04_FastToG.md)|
|第5篇全文翻译|[HippoRAG 2](翻译源稿/05_HippoRAG2.md)|
|版本与审校边界|[交付说明](交付说明_20261117.md)|
|原始文献|[五份PDF底本](原文PDF/)|

## 审校记录

[SAC-KG](构建与核验/终审_SAC-KG.md) · [KGP](构建与核验/终审_KGP.md) · [G-Retriever](构建与核验/终审_G-Retriever.md) · [FastToG](构建与核验/终审_FastToG.md) · [HippoRAG 2](构建与核验/终审_HippoRAG2.md) · [综述](构建与核验/终审_综述.md)

## 范围与提交

四篇知识图谱核心论文加一篇HippoRAG 2。区分实体关系知识图谱、文段结构图、文本属性图与短语—文段联合图。五篇翻译包含正文及非参考文献附录，参考文献保留英文；原图保持原版并配中文图注/对照，部分数值大表保留完整原表结构。

2026年11月27日课堂要求提交双面纸质报告。当前GitHub交付以Markdown为主，PDF排版脚本保存在构建与核验目录，按需生成打印版。未进行实际打印、装订或课堂提交，也未由外部人工独立终审。

## 先期材料

[文献清单](文献清单.md) · [报告框架](报告框架.md) · [详细执行计划](详细执行计划_20261117.md) · [精读矩阵](论文精读矩阵.md)
'''
(root/'README.md').write_text(readme,encoding='utf-8')
(root/'中文翻译PDF'/'README.md').write_text('''# 中文译稿的阅读与打印

当前交付以Markdown为主，五篇译稿和插图已放在[翻译源稿目录](../翻译源稿/)，综合报告见[报告正文](../报告成稿/知识图谱课程报告.md)。

按需运行[PDF构建脚本](../构建与核验/build_pdfs.py)，可在本目录生成独立打印PDF。GitHub当前不重复上传生成的五份PDF、总册和ZIP，全文内容均以Markdown及配套图片提供。
''',encoding='utf-8')
p=root/'交付说明_20261117.md';t=p.read_text(encoding='utf-8')
begin=t.index('## 文件入口');end=t.index('## 覆盖及版本边界')
t=t[:begin]+'''## 文件入口

- [综合报告](报告成稿/知识图谱课程报告.md)：五篇方法分析、实验口径、比较矩阵、研究框架、基线、消融和评价方案。
- [五篇完整译稿](翻译源稿/)：可编辑Markdown、配套原图、逐页覆盖与精读记录。
- [原文PDF](原文PDF/)：仓库中五份翻译底本，文件未修改。
- [构建与核验](构建与核验/)：原文校验、交叉审校、逐页第二轮审校、公式映射与可重复构建脚本。

GitHub以Markdown及其插图作为正式阅读入口。生成的PDF、总册、预览图片和ZIP不重复上传；需要纸质版时可以从这些源稿生成。

'''+t[end:]
t=t.replace('正式文件保存在本地工作目录，本次没有推送到GitHub。','正式阅读版本存放在GitHub仓库 yuxhf/Study 的课程报告/知识图谱_2026目录。')
t=t.replace('## 打印\n','## 按需生成打印版\n')
t=t.replace('总册按A4编排，可选择双面长边翻转、实际大小打印。总册目录使用整份PDF页序；各分册页脚独立编号。预计95张纸。若仅阅读综述，可单独打开11页正文。','构建脚本可生成A4总册及独立PDF，支持双面长边翻转、实际大小打印；总册目录使用整份PDF页序，各分册独立编号。上次排版结果为190页（含原图核对页与分册间空白页），后续编辑后以新构建结果为准。')
p.write_text(t,encoding='utf-8')
audit=root/'构建与核验'/'final_coverage_audit.json'
records=json.loads(audit.read_text(encoding='utf-8'))
for entry in records:
 f=root/'翻译源稿'/(entry['paper']+'.md');t=f.read_text(encoding='utf-8')
 entry.update(chars=len(t),sha256=hashlib.sha256(f.read_bytes()).hexdigest())
audit.write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
selected=[]
for f in sorted(root.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(root)
 if any(part in {'预览','__pycache__','原文提取'} for part in rel.parts):continue
 if rel.name=='GitHub上传清单.json':continue
 if f.suffix.lower() in {'.md','.json','.py'} or (f.suffix.lower()=='.png' and 'assets' in rel.parts):selected.append(f)
for f in selected:
 if f.suffix=='.py':f.write_text(f.read_text(encoding='utf-8').rstrip()+'\n',encoding='utf-8')
# 已入库底本不重复添加；仅上传本次材料。
references=[]
for f in [root/'报告成稿'/'知识图谱课程报告.md']+[root/'翻译源稿'/n for n in ['01_SAC-KG.md','02_KGP.md','03_G-Retriever.md','04_FastToG.md','05_HippoRAG2.md']]:
 for target in re.findall(r'!\[.*?\]\((.*?)\)',f.read_text(encoding='utf-8')):
  p=(f.parent/target).resolve();assert p.exists(),p;assert p in selected,p;references.append(str(p.relative_to(root)))
records=[dict(path=f.relative_to(repo).as_posix(),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in selected]
manifest=root/'构建与核验'/'GitHub上传清单.json'
manifest.write_text(json.dumps(dict(files=records,image_links_checked=len(references),new_generated_pdfs_uploaded=False),ensure_ascii=False,indent=2),encoding='utf-8')
selected.append(manifest)
for f in selected:subprocess.run(['git','-C',str(repo),'add','--',f.relative_to(repo).as_posix()],check=True,capture_output=True)
print(json.dumps(dict(files=len(selected),megabytes=round(sum(f.stat().st_size for f in selected)/1024**2,2),image_links_checked=len(references)),ensure_ascii=True))
