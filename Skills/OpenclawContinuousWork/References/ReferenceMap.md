# Reference Map

## Canonical Flow
1. Read `GeneralRules.md` for baseline continuous execution behavior.
2. If user gives explicit continuous-execution prompt constraints, apply `ContinuousExecutionDirective.md`.
3. If task type is optimization, apply `OptimizationRules.md` + `OptimizationDirective.md`.
4. Use `OptimizationChecklist.md` during execution.
5. Use `ReportingTemplate.md` for progress updates.
6. Use `AcceptanceTemplate.md` + `QualityRubric.md` for closure.

## Purpose Split
- `GeneralRules.md`: generic always-on behavior
- `ContinuousExecutionDirective.md`: user-asserted strong constraints
- `OptimizationRules.md`: optimization execution workflow
- `OptimizationDirective.md`: user prompt baseline for optimization
- `OptimizationChecklist.md`: quick execution checklist
- `ReportingTemplate.md`: output format for milestones/blockers/completion
- `AcceptanceTemplate.md`: objective acceptance closure
- `QualityRubric.md`: measurable quality gate
