#!/usr/bin/env python3
"""Build a small research graph from technical_points/ledger.csv."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path.cwd()
LEDGER = ROOT / "technical_points" / "ledger.csv"
GRAPH = ROOT / "technical_points" / "graph"


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> None:
    if not LEDGER.exists():
        raise SystemExit("missing technical_points/ledger.csv")
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8")))
    nodes: list[dict] = []
    edges: list[dict] = []
    chunks: list[dict] = []
    for row in rows:
        item_id = row["item_id"]
        nodes.append(
            {
                "id": item_id,
                "type": "technical_point",
                "label": row.get("original_item", item_id),
                "properties": row,
            }
        )
        for field in ["evidence_status", "verification_status", "rewritten_location"]:
            value = row.get(field, "")
            if not value:
                continue
            node_id = f"{field}:{value}"
            nodes.append({"id": node_id, "type": field, "label": value, "properties": {}})
            edges.append({"source": item_id, "target": node_id, "relation": f"has_{field}"})
        chunks.append(
            {
                "id": f"chunk:{item_id}",
                "node_id": item_id,
                "text": " | ".join(
                    str(row.get(key, ""))
                    for key in [
                        "original_item",
                        "mechanism",
                        "impact",
                        "evidence_status",
                        "verification_status",
                        "action",
                    ]
                ),
                "metadata": {"source": "technical_points/ledger.csv"},
            }
        )
    seen = {}
    for node in nodes:
        seen[node["id"]] = node
    nodes = list(seen.values())
    write_jsonl(GRAPH / "nodes.jsonl", nodes)
    write_jsonl(GRAPH / "edges.jsonl", edges)
    write_jsonl(GRAPH / "chunks.jsonl", chunks)
    (GRAPH / "manifest.json").write_text(
        json.dumps(
            {
                "schema": "research-property-graph-v1",
                "nodes": "nodes.jsonl",
                "edges": "edges.jsonl",
                "chunks": "chunks.jsonl",
                "node_count": len(nodes),
                "edge_count": len(edges),
                "chunk_count": len(chunks),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (GRAPH / "schema.md").write_text(
        "# Research Graph Schema\n\nNodes and edges are generated from `technical_points/ledger.csv`.\n",
        encoding="utf-8",
    )
    print(f"wrote {len(nodes)} nodes, {len(edges)} edges, {len(chunks)} chunks")


if __name__ == "__main__":
    main()
