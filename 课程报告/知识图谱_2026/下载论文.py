#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载知识图谱课程的五篇论文原文（无需第三方依赖）。
在本文件所在目录执行: python 下载论文.py
PDF 保存到旁边的“原文PDF”目录；如下载受限可使用 README 中的链接手动下载。
"""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import time

OUT = Path(__file__).resolve().parent / "原文PDF"
OUT.mkdir(parents=True, exist_ok=True)
PAPERS = [
    ("01_SAC-KG_ACL2024.pdf", [
        "https://aclanthology.org/2024.acl-long.238.pdf",
    ]),
    ("02_KGP_AAAI2024.pdf", [
        "https://ojs.aaai.org/index.php/AAAI/article/download/29889/31552",
        "https://arxiv.org/pdf/2308.11730",
    ]),
    ("03_G-Retriever_NeurIPS2024.pdf", [
        "https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf",
    ]),
    ("04_FastToG_AAAI2025.pdf", [
        "https://arxiv.org/pdf/2501.14300",
    ]),
    ("05_HippoRAG2_ICML2025.pdf", [
        "https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf",
    ]),
]
for name, urls in PAPERS:
    target = OUT / name
    if target.exists() and target.stat().st_size > 10240:
        with target.open("rb") as f:
            if f.read(5) == b"%PDF-":
                print(f"[已有] {name}")
                continue
    success = False
    for url in urls:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Academic research PDF download)"})
            with urlopen(req, timeout=50) as res:
                data = res.read()
            if len(data) < 10240 or not data.startswith(b"%PDF-"):
                raise ValueError("返回内容不是有效 PDF")
            target.write_bytes(data)
            print(f"[成功] {name} | {len(data):,} bytes | sha256 {hashlib.sha256(data).hexdigest()[:16]}")
            success = True
            break
        except Exception as e:
            print(f"[重试其他来源] {name}: {type(e).__name__}: {e}")
            time.sleep(1)
    if not success:
        print(f"[下载失败] {name}，请参考 原文PDF/README.md 手动上传")
