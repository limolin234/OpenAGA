# Technical Points

`ledger.csv` is the source of truth for claim and technical-point tracking.

Each row should represent one claim, mechanism, parameter, process step, failure mode, figure, formula, or validation question.

Derived graph files can be generated with:

```bash
python3 scripts/build_graph_from_ledger.py
```
