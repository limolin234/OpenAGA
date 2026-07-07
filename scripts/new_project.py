#!/usr/bin/env python3
"""Create a new research-audit project from this template."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__"}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists() and any(dst.iterdir()):
        raise SystemExit(f"target exists and is not empty: {dst}")
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.name in SKIP_DIRS:
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        else:
            shutil.copy2(item, target)


def rewrite_placeholders(root: Path, name: str) -> None:
    for path in root.rglob("*"):
        if path.is_dir() or path.suffix not in {".md", ".csv", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("Research Project Template", name)
        text = text.replace("research-audit template", f"{name} research-audit project")
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="new project directory")
    parser.add_argument("--name", help="project display name")
    parser.add_argument("--git", action="store_true", help="initialize a fresh git repository")
    args = parser.parse_args()

    src = Path(__file__).resolve().parents[1]
    dst = Path(args.target).resolve()
    name = args.name or dst.name
    copy_tree(src, dst)
    rewrite_placeholders(dst, name)
    if args.git:
        subprocess.run(["git", "init"], cwd=dst, check=True)
        subprocess.run(["git", "add", "."], cwd=dst, check=True)
        subprocess.run(["git", "commit", "-m", "Initialize research project"], cwd=dst, check=False)
    print(f"created {dst}")


if __name__ == "__main__":
    main()
