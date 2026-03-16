# Module System

## Purpose
使该 Skill 支持“随时新增 MD 模块文件”且无需改动核心规则。

## Module Convention
- 所有可扩展模块放在 `References/` 目录下。
- 文件命名遵循首字母大写规范（例如：`RiskControl.md`、`DeliveryPolicy.md`）。
- 每个模块文件建议包含：
  - `# <Title>`
  - `## Purpose`
  - `## Rules` 或 `## Checklist`
  - （可选）`## Examples`

## Loading Rule
- 核心入口始终从 `ReferenceMap.md` 读取。
- 新增模块后，执行脚本 `Scripts/BuildReferenceMap.py` 自动更新 `ReferenceMap.md`。

## User Workflow (Add New MD Anytime)
1. 在 `References/` 新建模块 MD 文件。
2. 填写模块规则内容。
3. 运行：`python Scripts/BuildReferenceMap.py`
4. 提交并推送。

## Notes
- 不要改动 `SKILL.md` 的主结构，除非入口逻辑变化。
- 模块之间如有依赖，直接在模块内增加“See also: <OtherModule.md>”。
