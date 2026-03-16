---
name: openclaw-continuous-work
description: 鍏ㄩ潰浼樺寲 OpenClaw 瀵硅瘽浣撻獙骞跺己鍖栦换鍔￠棴鐜墽琛屻€俇se when user asks to 浼樺寲, 宸ヤ綔, 椤圭洰, 鎸佺画宸ヤ綔, 涓嶈鍋? 缁х画鍋? 缁х画宸ヤ綔, 鎴栧笇鏈涘姪鎵嬫帴鏀舵寚浠ゅ悗鎸佺画鎺ㄨ繘鐩村埌瀹屾垚銆侫lso use when the user asks for complete optimization tasks rather than partial fixes.
---

# OpenClaw Continuous Work

## Goal
- 杩炵画鎺ㄨ繘锛氭帴鍒版寚浠ゅ悗鎸佺画鎵ц鐩村埌瀹屾垚銆?- 浼樺寲闂幆锛氫紭鍖栦换鍔″繀椤诲叏閾捐矾钀藉湴骞跺洖褰掗獙璇併€?- 绋冲畾鍙嶉锛氶噷绋嬬 + 鏃堕棿瑙﹀彂杩涘害姹囨姤锛岄伩鍏嶆矇榛樻垨鍒峰睆銆?
## Rule Map
- 瑙勫垯鎬昏锛堣嚜鍔ㄧ储寮曪級锛歚References/ReferenceMap.md`
- 妯″潡鍖栬鑼冿細`References/ModuleSystem.md`

## Core Modules
- 閫氱敤杩炵画鎵ц瑙勫垯锛歚References/GeneralRules.md`
- 鎸佺画鎵ц寮虹害鏉燂細`References/ContinuousExecutionDirective.md`
- 浼樺寲浠诲姟涓撻」瑙勫垯锛歚References/OptimizationRules.md`
- 浼樺寲鎸囦护鍘熸枃鍩虹嚎锛歚References/OptimizationDirective.md`
- 姹囨姤妯℃澘锛歚References/ReportingTemplate.md`
- 浼樺寲娓呭崟锛歚References/OptimizationChecklist.md`
- 楠屾敹妯℃澘锛歚References/AcceptanceTemplate.md`
- 璐ㄩ噺璇勫垎锛歚References/QualityRubric.md`

## Scripts
- 鍛藉悕瑙勮寖宸℃锛歚Scripts/NamingAudit.py`
  - 鐢ㄦ硶锛歚python Scripts/NamingAudit.py <target_path> --json`
  - 浣滅敤锛氭壂鎻忓懡鍚嶄笉绗﹀悎鈥滃崟璇嶉瀛楁瘝澶у啓鈥濊鍒欑殑鏂囦欢/鏂囦欢澶瑰苟缁欏嚭寤鸿銆?- 妯″潡绱㈠紩閲嶅缓锛歚Scripts/BuildReferenceMap.py`
  - 鐢ㄦ硶锛歚python Scripts/BuildReferenceMap.py`
  - 浣滅敤锛氳嚜鍔ㄩ噸寤?`References/ReferenceMap.md`锛岃鏂板 MD 妯″潡鍗虫椂绾冲叆绱㈠紩銆?
- 内容去重与链接巡检：Scripts/ContentLinkAudit.py\n  - 用法：python Scripts/ContentLinkAudit.py <target_path> --json\n  - 作用：检测重复段落与失效 Markdown 链接，支持持续精简与联动。\n\n## Maintainer Notes
- 鏂板鍦烘櫙浼樺厛鍐欏叆 `References/`锛屼繚鎸佹湰鏂囦欢绮剧畝銆?- 浼樺厛鎵╁睍锛氳Е鍙戣瘝銆佸け璐ュ崌绾х瓥鐣ャ€佸畬鎴愬垽瀹氫笌楠屾敹妯℃澘銆?
