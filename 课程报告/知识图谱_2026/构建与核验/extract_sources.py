from pathlib import Path
import pdfplumber,hashlib,json
root=Path(__file__).resolve().parents[1]
out=root/'构建与核验'/'原文提取';out.mkdir(exist_ok=True)
records=[]
for f in sorted((root/'原文PDF').glob('*.pdf')):
    with pdfplumber.open(f) as pdf:
        texts=[p.extract_text(x_tolerance=2) or '' for p in pdf.pages]
        (out/(f.stem+'.txt')).write_text('\n\n'.join(f'=== PAGE {i+1} ===\n{t}' for i,t in enumerate(texts)),encoding='utf-8')
        records.append(dict(file=f.name,pages=len(pdf.pages),size=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(out/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(records,ensure_ascii=False,indent=2))
