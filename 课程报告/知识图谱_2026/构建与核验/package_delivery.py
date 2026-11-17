from pathlib import Path
import zipfile,json,hashlib,re
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]
names=['01_SAC-KG','02_KGP','03_G-Retriever','04_FastToG','05_HippoRAG2'];source_pages=[16,22,32,11,19];coverage=[]
for n,count in zip(names,source_pages):
 f=root/'翻译源稿'/(n+'.md');t=f.read_text(encoding='utf-8');markers=[int(v) for v in re.findall(r'<!-- source-page: (\d+) -->',t)]
 missing=sorted(set(range(1,count+1))-set(markers));links=re.findall(r'!\[.*?\]\((.*?)\)',t);broken=[v for v in links if not (f.parent/v).exists()]
 assert not missing and not broken,(n,missing,broken)
 coverage.append(dict(paper=n,expected_pages=count,source_markers=len(markers),missing_pages=missing,broken_images=broken,chars=len(t),sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(root/'构建与核验'/'final_coverage_audit.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
outputs=list((root/'报告成稿').glob('*.pdf'))+list((root/'中文翻译PDF').glob('0*.pdf'))
hashes=[dict(file=str(f.relative_to(root)),pages=len(PdfReader(f).pages),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in outputs]
(root/'构建与核验'/'交付文件校验.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2),encoding='utf-8')
total=len(PdfReader(root/'报告成稿'/'知识图谱课程报告_含五篇译稿.pdf').pages)
readme=root/'交付说明_20261117.md';t=readme.read_text(encoding='utf-8')
t=re.sub(r'：\d+页总册',f'：{total}页总册',t);t=re.sub(r'预计\d+张纸',f'预计{(total+1)//2}张纸',t)
t=t.replace('完整内容初译与综述审阅版','二轮审校版').replace('不将定向抽核表述为独立逐句终审通过。','已完成逐页第二轮内容对照与直接修订，审校过程属于模型辅助审校，未由外部人工独立审校。')
t=t.replace('这些检查不能替代对100页原文的独立逐句语言审校。译文有句法合并、部分术语仍可润色；','第二轮已补齐长案例、重复干扰提示、检查表条目及发现的误译，逐页修订记录见“终审”文件。图像仍保留原版英文并配中文对照；')
readme.write_text(t,encoding='utf-8')
target=root.parent/'知识图谱课程报告_20261117_完整交付包.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in root.rglob('*'):
  if not f.is_file():continue
  rel=f.relative_to(root)
  if '预览' in rel.parts or '__pycache__' in rel.parts:continue
  if rel.parts[0]=='构建与核验' and rel.name=='总册目录.pdf':continue
  if f.suffix.lower() not in {'.pdf','.png','.md','.json','.py'}:continue
  z.write(f,str(Path('知识图谱_2026')/rel))
print(json.dumps({'zip':str(target),'megabytes':round(target.stat().st_size/1024**2,2),'pdfs':len(outputs)},ensure_ascii=True))
