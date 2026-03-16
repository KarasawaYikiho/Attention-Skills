#!/usr/bin/env python3
"""
BuildReferenceMap.py
Auto-generate References/ReferenceMap.md so users can add new .md modules anytime.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF_DIR = ROOT / "References"
MAP_FILE = REF_DIR / "ReferenceMap.md"

EXCLUDE = {"ReferenceMap.md", "ModuleGraph.md", "ConflictReport.md"}
PRIORITY = [
    "GeneralRules.md",
    "ContinuousExecutionDirective.md",
    "OptimizationRules.md",
    "OptimizationDirective.md",
    "OptimizationChecklist.md",
    "ReportingTemplate.md",
    "AcceptanceTemplate.md",
    "QualityRubric.md",
    "ModuleSystem.md",
]


def collect_modules() -> list[str]:
    mods = [p.name for p in REF_DIR.glob("*.md") if p.name not in EXCLUDE]
    mods_sorted = sorted(mods)
    ordered = [m for m in PRIORITY if m in mods_sorted]
    rest = [m for m in mods_sorted if m not in ordered]
    return ordered + rest


def build_content(mods: list[str]) -> str:
    lines: list[str] = []
    lines.append("# Reference Map")
    lines.append("")
    lines.append("Auto-generated module index. New `References/*.md` files are included after running `python Scripts/BuildReferenceMap.py`.")
    lines.append("")
    lines.append("## Canonical Flow")
    lines.append("1. Read `GeneralRules.md` for baseline continuous execution behavior.")
    lines.append("2. Apply `ContinuousExecutionDirective.md` when user enforces strong continuous-work constraints.")
    lines.append("3. For optimization tasks, apply `OptimizationRules.md` + `OptimizationDirective.md`.")
    lines.append("4. Use `OptimizationChecklist.md` during execution.")
    lines.append("5. Use `ReportingTemplate.md` for updates.")
    lines.append("6. Use `AcceptanceTemplate.md` + `QualityRubric.md` for closure.")
    lines.append("")
    lines.append("## Available Modules")
    for m in mods:
        lines.append(f"- `{m}`")
    lines.append("")
    lines.append("## Extending")
    lines.append("- Add a new `.md` file into `References/`.")
    lines.append("- Run `python Scripts/BuildReferenceMap.py`.")
    lines.append("- Commit and push.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    mods = collect_modules()
    MAP_FILE.write_text(build_content(mods), encoding="utf-8")
    print(f"Updated: {MAP_FILE}")
    print(f"Modules: {len(mods)}")


if __name__ == "__main__":
    main()
