# Agent Guide

This project follows the research-audit template.

## Workflow

1. Read `workflow.md`, `docs_graph/docs_graph.md`, and the active `manual.md` if present.
2. Preserve source technical details in `technical_points/ledger.csv` before rewriting.
3. Keep evidence status separate from source-draft labels.
4. Compare alternatives at the same layer: interface, package, module, system, cost, reliability.
5. Put stable project context in `docs_graph/`, detailed sources in `sources/`, models in `integration/`, and deliverables in `drafts/`.
6. Compile or render deliverables before reporting completion.

## Commands

```bash
python3 scripts/check_project.py
python3 scripts/build_graph_from_ledger.py
python3 scripts/new_project.py ../my_new_project --name "My New Project" --git
```
