#!/usr/bin/env python3
"""Lightweight project-template sanity check."""

from pathlib import Path

REQUIRED = [
    "workflow.md",
    "docs_graph/docs_graph.md",
    "sources/source_registry.csv",
    "technical_points/ledger.csv",
    "integration",
    "drafts",
]

missing = [p for p in REQUIRED if not Path(p).exists()]
if missing:
    raise SystemExit("missing: " + ", ".join(missing))
print("project template check passed")
