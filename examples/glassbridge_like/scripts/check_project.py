#!/usr/bin/env python3
from pathlib import Path

for required in ["workflow.md", "sources/source_registry.csv", "technical_points/ledger.csv"]:
    if not Path(required).exists():
        raise SystemExit(f"missing {required}")
print("example project check passed")
