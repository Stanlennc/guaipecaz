#!/usr/bin/env python3
"""Regenera emergencia-data.js a partir de emergencia.json."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "emergencia.json"
OUTPUT = ROOT / "emergencia-data.js"


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    js = "window.GUIEMERGENCIA_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"
    OUTPUT.write_text(js, encoding="utf-8")
    print(f"Salvo {len(data.get('pontos', []))} pontos em {OUTPUT.name}", file=sys.stderr)


if __name__ == "__main__":
    main()
