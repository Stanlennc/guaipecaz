#!/usr/bin/env python3
"""Gera schedules-data.js a partir de automation/schedules.json."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "automation" / "schedules.json"
OUT = ROOT / "schedules-data.js"


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    OUT.write_text(
        "window.GUISCHEDULES_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    print(f"Gerado {OUT.name}", file=sys.stderr)


if __name__ == "__main__":
    main()
