---
name: openclaw-continuous-work
description: 全面优化 OpenClaw 对话体验并强化任务闭环执行。Use when user asks to 优化, 工作, 项目, 持续工作, 不要停, 继续做, 继续工作, 或希望助手接收指令后持续推进直到完成。Also use when the user asks for complete optimization tasks rather than partial fixes.
---

# OpenClaw Continuous Work

## Goal
- 连续推进：接到指令后持续执行直到完成。
- 优化闭环：优化任务必须全链路落地并回归验证。
- 稳定反馈：里程碑 + 时间触发进度汇报，避免沉默或刷屏。

## Rule Map
- 规则总览：`References/ReferenceMap.md`
- 通用连续执行规则：`References/GeneralRules.md`
- 持续执行强约束：`References/ContinuousExecutionDirective.md`
- 优化任务专项规则：`References/OptimizationRules.md`
- 优化指令原文基线：`References/OptimizationDirective.md`
- 汇报模板：`References/ReportingTemplate.md`
- 优化清单：`References/OptimizationChecklist.md`
- 验收模板：`References/AcceptanceTemplate.md`
- 质量评分：`References/QualityRubric.md`

## Script
- 命名规范巡检：`Scripts/NamingAudit.py`
  - 用法：`python Scripts/NamingAudit.py <target_path> --json`
  - 作用：扫描命名不符合“单词首字母大写”规则的文件/文件夹并给出建议。

## Maintainer Notes
- 新增场景优先写入 `References/`，保持本文件精简。
- 优先扩展：触发词、失败升级策略、完成判定与验收模板。
