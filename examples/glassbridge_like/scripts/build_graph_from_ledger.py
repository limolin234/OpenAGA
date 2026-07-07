#!/usr/bin/env python3
import runpy
from pathlib import Path

template_script = Path(__file__).resolve().parents[2] / "scripts" / "build_graph_from_ledger.py"
runpy.run_path(str(template_script), run_name="__main__")
