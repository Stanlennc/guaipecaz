#!/usr/bin/env python3
"""Atualiza a faixa de emergência em todas as páginas HTML públicas."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

STRIP = """<div class="emergency-strip">
  <div class="wrap">
    <span class="label">Contatos de emergência</span>
    <a href="mulher.html">Delegacia da Mulher</a>
    <a href="contatos-emergencia.html#samu">SAMU 192</a>
    <a href="contatos-emergencia.html#bombeiros">Bombeiros 193</a>
    <a href="contatos-emergencia.html#policia">Polícia 190</a>
    <a href="contatos-emergencia.html#defesa-civil">Defesa Civil 199</a>
    <a href="ajude-um-pet.html">Ajude um pet</a>
  </div>
</div>"""

PAGES = [
    "index.html",
    "guibanews.html",
    "noticia.html",
    "servicos.html",
    "participe.html",
    "saude.html",
    "diario-oficial.html",
    "contatos.html",
    "contatos-emergencia.html",
    "mulher.html",
    "ajude-um-pet.html",
]

for name in PAGES:
    path = ROOT / name
    if not path.exists():
        print(f"pular {name}")
        continue
    html = path.read_text(encoding="utf-8")
    if '<div class="emergency-strip">' in html:
        html = re.sub(
            r'<div class="emergency-strip">.*?</div>\s*</div>',
            STRIP,
            html,
            count=1,
            flags=re.DOTALL,
        )
    else:
        html = html.replace("</header>\n\n<main>", "</header>\n\n" + STRIP + "\n\n<main>")
    path.write_text(html, encoding="utf-8")
    print(f"ok {name}")
