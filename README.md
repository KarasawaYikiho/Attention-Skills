# Attention-Skills

A modular repository for building, validating, and maintaining OpenClaw-compatible Agent Skills.

## What This Repo Provides

- A production-ready Skill: `OpenclawContinuousWork`
- A modular `References/` system for rule expansion via Markdown files
- A script-based optimization pipeline for quality and consistency checks

## Repository Layout

- `Skills/` — Skill source folders (each contains `SKILL.md`)
- `Dist/` — Packaged `.skill` outputs (build artifacts)
- `Scripts/` — Repository-level helper scripts (optional)

## Included Skill

### `Skills/OpenclawContinuousWork`

Purpose: improve OpenClaw conversation execution quality with continuous-work discipline and optimization-oriented workflows.

Key capabilities:
- Continuous execution constraints
- Optimization rule baseline integration
- Extensible Markdown module system
- Automated audits for naming, links, conflicts, ordering, and encoding

## Module Extension Workflow

Inside `Skills/OpenclawContinuousWork`:

1. Add a new module file in `References/` (recommended: copy `ModuleTemplate.md`)
2. (Optional) adjust load priority in `References/ModuleOrder.json`
3. Run pipeline:
   - `python Scripts/RunOptimizationPipeline.py Skills/OpenclawContinuousWork`
4. Review generated reports under `References/`
5. Commit and push

## Quality & Maintenance Scripts (Skill Level)

- `NamingAudit.py` — naming convention audit
- `ContentLinkAudit.py` — duplicate paragraph + broken markdown link scan
- `ValidateModuleOrder.py` — `ModuleOrder.json` validation
- `BuildReferenceMap.py` — auto-generate module index
- `BuildModuleGraph.py` — generate module dependency graph
- `DetectRuleConflicts.py` — heuristic rule conflict detection
- `NormalizeEncoding.py` — normalize text to UTF-8 (no BOM) + LF
- `RunOptimizationPipeline.py` — one-command orchestration of the above

## Naming Convention

Use single words or word groups with each word capitalized for regular files/folders.
Keep tool-required special names (for example `.gitignore`) unchanged.

## License

This repository is licensed under the MIT License.
See [LICENSE](LICENSE) for details.
