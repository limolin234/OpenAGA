# Research Project Template

Template for evidence-led technical feasibility reports.

## Structure

```text
.
├── AGENT.md
├── README.md
├── workflow.md
├── manual.md
├── data/
├── sources/
├── technical_points/
│   ├── ledger.csv
│   └── graph/
├── integration/
├── figures/
├── drafts/
├── docs_graph/
│   └── docs_graph.md
└── scripts/
    └── check_project.py
```

## Use

- `manual.md`: human-maintained working manuscript.
- `sources/`: evidence notes, registries, search logs, rejected-source notes.
- `technical_points/ledger.csv`: machine-readable claim/technical-point ledger.
- `technical_points/graph/`: derived graph artifacts from the ledger.
- `integration/`: formulas, calculations, sensitivity models, figures.
- `drafts/`: active report source and rendered outputs.
- `docs_graph/`: durable navigation and project status.

Copy this folder, then replace placeholders with the project-specific source document and claim ledger.

## Bootstrap A New Project

From this template directory:

```bash
python3 scripts/new_project.py ../my_new_research_project --name "My New Research Project" --git
```

The script copies the template, rewrites the display name in text files, and optionally initializes a fresh Git repo.

## Generate A Local Graph

After filling `technical_points/ledger.csv`:

```bash
python3 scripts/build_graph_from_ledger.py
```

This creates `technical_points/graph/nodes.jsonl`, `edges.jsonl`, `chunks.jsonl`, and `manifest.json`.

## Example

See `examples/glassbridge_like/` for a minimal photonic-packaging style project:

```bash
cd examples/glassbridge_like
python3 scripts/check_project.py
python3 integration/offset_model.py
```
