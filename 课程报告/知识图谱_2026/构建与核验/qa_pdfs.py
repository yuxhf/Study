from pathlib import Path
import json,re
import pypdfium2 as p
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1];out=root/'构建与核验'/'预览';out.mkdir(exist_ok=True)
manifest=json.loads((root/'构建与核验'/'pdf_manifest.json').read_text(encoding='utf-8'))
stats=[]
for item in manifest[:-1]:
 path=root/item['file'];doc=p.PdfDocument(str(path));reader=PdfReader(path)
 tiles=[];key=path.stem[:2] if path.stem[:2].isdigit() else 'report'
 for i in range(len(doc)):
  im=doc[i].render(scale=.5).to_pil();im.thumbnail((230,325));tile=Image.new('RGB',(246,350),'#d8d8d8');tile.paste(im,((246-im.width)//2,5));ImageDraw.Draw(tile).text((10,332),f'{key} / {i+1}',fill='black');tiles.append(tile)
 for n in range(0,len(tiles),20):
  canvas=Image.new('RGB',(246*4,350*5),'white')
  for j,t in enumerate(tiles[n:n+20]):canvas.paste(t,((j%4)*246,(j//4)*350))
  canvas.save(out/f'{key}-sheet-{n//20+1:02}.png')
 texts=[page.extract_text() or '' for page in reader.pages]
 stats.append(dict(file=item['file'],pages=len(doc),empty_text_pages=[i+1 for i,t in enumerate(texts) if len(t.strip())<30],replacement_char_pages=[i+1 for i,t in enumerate(texts) if '\ufffd' in t],latex_command_pages=[i+1 for i,t in enumerate(texts) if re.search(r'\\(?:frac|begin|operatorname|mathrm|tag)',t)]))
(root/'构建与核验'/'pdf_qa.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
