#!/usr/bin/env python3
"""
NameAudit.py
Scan files/folders and report names not following: PascalCase words joined by separator.
Examples allowed: MyFile, MyFileName, My-File, My_File, My File
"""

from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

TOKEN_RE = re.compile(r"^[A-Z][a-zA-Z0-9]*$")


def is_valid_name(name: str) -> bool:
    if not name or name in {".", ".."}:
        return False
    # keep extension out for file stem checking
    return all(TOKEN_RE.fullmatch(tok) for tok in re.split(r"[\s_-]+", name) if tok)


def suggest(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9\s_-]", " ", name)
    parts = [p for p in re.split(r"[\s_-]+", name) if p]
    if not parts:
        return "Unnamed"
    fixed = []
    for p in parts:
        if p.isupper() and len(p) <= 4:
            fixed.append(p.title())
        else:
            fixed.append(p[:1].upper() + p[1:])
    return "-".join(fixed)


def scan(root: Path, include_hidden: bool = False):
    issues = []
    for p in root.rglob("*"):
        rel = p.relative_to(root)
        if not include_hidden and any(part.startswith(".") for part in rel.parts):
            continue
        target = p.stem if p.is_file() else p.name
        if not is_valid_name(target):
            issues.append({
                "path": str(rel),
                "type": "file" if p.is_file() else "folder",
                "current": p.name,
                "suggested": suggest(p.stem) + (p.suffix if p.is_file() else ""),
            })
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-hidden", action="store_true")
    args = ap.parse_args()

    root = Path(args.target).resolve()
    issues = scan(root, include_hidden=args.include_hidden)

    if args.json:
        print(json.dumps({"root": str(root), "issues": issues, "count": len(issues)}, ensure_ascii=False, indent=2))
        return

    print(f"Root: {root}")
    print(f"Invalid Names: {len(issues)}")
    for i, item in enumerate(issues, 1):
        print(f"{i}. [{item['type']}] {item['path']}")
        print(f"   current:   {item['current']}")
        print(f"   suggested: {item['suggested']}")


if __name__ == "__main__":
    main()
