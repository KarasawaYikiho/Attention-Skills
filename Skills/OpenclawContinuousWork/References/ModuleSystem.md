# Module System

## Purpose
浣胯 Skill 鏀寔鈥滈殢鏃舵柊澧?MD 妯″潡鏂囦欢鈥濅笖鏃犻渶鏀瑰姩鏍稿績瑙勫垯銆?
## Module Convention
- 鎵€鏈夊彲鎵╁睍妯″潡鏀惧湪 `References/` 鐩綍涓嬨€?- 鏂囦欢鍛藉悕閬靛惊棣栧瓧姣嶅ぇ鍐欒鑼冿紙渚嬪锛歚RiskControl.md`銆乣DeliveryPolicy.md`锛夈€?- 姣忎釜妯″潡鏂囦欢寤鸿鍖呭惈锛?  - `# <Title>`
  - `## Purpose`
  - `## Rules` 鎴?`## Checklist`
  - 锛堝彲閫夛級`## Examples`

## Loading Rule
- 鏍稿績鍏ュ彛濮嬬粓浠?`ReferenceMap.md` 璇诲彇銆?- 鏂板妯″潡鍚庯紝鎵ц鑴氭湰 `Scripts/BuildReferenceMap.py` 鑷姩鏇存柊 `ReferenceMap.md`銆?
## User Workflow (Add New MD Anytime)
1. 鍦?`References/` 鏂板缓妯″潡 MD 鏂囦欢銆?2. 濉啓妯″潡瑙勫垯鍐呭銆?3. 杩愯锛歚python Scripts/BuildReferenceMap.py`
4. 鎻愪氦骞舵帹閫併€?
## Notes
- 涓嶈鏀瑰姩 `SKILL.md` 鐨勪富缁撴瀯锛岄櫎闈炲叆鍙ｉ€昏緫鍙樺寲銆?- 妯″潡涔嬮棿濡傛湁渚濊禆锛岀洿鎺ュ湪妯″潡鍐呭鍔犫€淪ee also: <OtherModule.md>鈥濄€?
## Recommended Starter
- Copy ModuleTemplate.md when creating a new module to keep structure consistent.

## Quality Check
- Run python Scripts/ContentLinkAudit.py . --json to detect repeated paragraphs and missing markdown links.

