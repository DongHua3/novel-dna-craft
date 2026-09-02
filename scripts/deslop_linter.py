#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deslop_linter.py - 网文去AI味快速质检脚本 (Zero-Dependency)
用法:
    python deslop_linter.py <章节文本或目录路径> [--whitelist 白名单文件]
功能:
    1. Gate A: 扫描一级禁用套路词 (眼中闪过、嘴角勾起、深吸一口气、不容置疑等)
    2. Gate B: 扫描翻案腔与过度对仗 (不是...而是...、并非...而是...、带着一丝)
    3. Gate C: 扫描情绪直接告知 (感到一丝、心中涌起一股、眼里淬了毒等)
    4. Gate E: 扫描公式化对话标签 (冷笑道、缓缓开口道、淡淡说道等)
    5. Gate F/G: 扫描章末总结升华与上帝视角 (他不知道的是、命运的齿轮、反击才刚刚开始等)
    6. 标点门禁: 扫描正文中违规出现的破折号与省略号 (排除了 Markdown 的 --- 分隔线)
    7. 支持 .deslop-whitelist 项目专有词白名单豁免
"""

import sys
import re
from pathlib import Path

# 确保在 Windows 控制台也能安全输出 UTF-8
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 7-Gate 违规模式清单
RULES = [
    {
        "gate": "Gate A (一级禁用套路词)",
        "pattern": r"(眼中闪过一[丝抹道冷]|嘴角[勾浮扬]起一[抹丝分弧]|深吸了一口气|深吸一口气|不禁[微微感到心中]|不由得[感到心中微]|仿佛化作了|不容[置疑置喙]|指节泛白|瞳孔[微骤一]?缩|心下了然|心中一[震凛动]|几不可闻|微不可察|自然而然|话锋一转)",
        "tip": "典型网文 AI 高频套路词，建议用具体白描、人物行动或直接删除。"
    },
    {
        "gate": "Gate B (翻案腔/万能状语)",
        "pattern": r"(不是.{1,15}而是|并非.{1,15}而是|与其说.{1,15}不如说|表面上.{1,15}实际上|看似.{1,15}实则|带着一[丝抹分](?:不易察觉的|冰冷的|嘲讽的|无奈的))",
        "tip": "逻辑翻案腔或万能状语，破坏沉浸感，建议直接正面下结论或写具体动作。"
    },
    {
        "gate": "Gate C (情绪直接告知)",
        "pattern": r"(感到一[丝抹点份][绝恐丧慌喜伤痛]|心中涌起一股|眼里淬了|心里某个地方软得|散发着一股.{1,8}(?:气息|气场))",
        "tip": "告诉而非展示(Show, Don't Tell)，建议将抽象情绪转化为生理反应、环境互动或台词。"
    },
    {
        "gate": "Gate E (公式化对话标签)",
        "pattern": r"([”」][，。、]?(?:他|她|众人|对方)?(?:冷笑道|缓缓开口道|淡淡说道|惊呼出声道|沉声开口道|冷冷开口道))",
        "tip": "对话标签过于刻板，建议用角色动作引出或直接无标签呈现对话。"
    },
    {
        "gate": "Gate F/G (上帝视角与章末升华)",
        "pattern": r"(他不知[道晓]的是|殊不知|命运的齿轮|这一刻，?他终于明白|属于.{1,10}的反击才刚刚开始|反击才刚刚开始|从这一刻开始|冥冥之中|演得真好|不得不说)",
        "tip": "叙述者越权跳出角色视角剧透或过早升华，建议收束在具体物理动作或悬念处。"
    },
    {
        "gate": "标点门禁 (破折号/省略号)",
        "pattern": r"(——|……|--\s*[\u4e00-\u9fa5]|[\u4e00-\u9fa5]\s*--)",
        "tip": "正文禁用破折号与省略号停顿，改用逗号、句号或动作分句以保持行文呼吸感。"
    }
]


def load_whitelist(target_path: Path):
    whitelist = set()
    candidates = [
        target_path / ".deslop-whitelist" if target_path.is_dir() else target_path.parent / ".deslop-whitelist",
        Path(".deslop-whitelist")
    ]
    for c in candidates:
        if c.is_file():
            for line in c.read_text(encoding='utf-8', errors='ignore').splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    whitelist.add(line)
            break
    return whitelist


def lint_text(file_path: Path, content: str, whitelist: set):
    lines = content.split('\n')
    findings = []
    
    for line_idx, line in enumerate(lines, 1):
        line_clean = line.strip()
        # 跳过空行、Markdown 标题、表格行、代码块、引用块及水平分隔线 (--- / ***)
        if not line_clean or line_clean.startswith(('#', '|', '```', '>')) or set(line_clean) <= {'-', '*', '_'}:
            continue
            
        for rule in RULES:
            matches = list(re.finditer(rule["pattern"], line_clean))
            for m in matches:
                matched_str = m.group(0)
                # 白名单检查
                if any(w in matched_str for w in whitelist):
                    continue
                findings.append({
                    "line": line_idx,
                    "gate": rule["gate"],
                    "matched": matched_str,
                    "snippet": line_clean[:60] + ("..." if len(line_clean) > 60 else ""),
                    "tip": rule["tip"]
                })
    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python deslop_linter.py <path_to_chapter_file_or_dir>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    files = []
    
    if target_path.is_file():
        files.append(target_path)
    elif target_path.is_dir():
        files.extend([f for f in target_path.glob("**/*") if f.suffix.lower() in ['.txt', '.md']])
    else:
        print(f"Error: Path {target_path} not found.")
        sys.exit(1)

    whitelist = load_whitelist(target_path)
    total_issues = 0
    print("=" * 65)
    print("         [novel-dna-craft] 7-Gate 去AI味快速扫描报告")
    if whitelist:
        print(f"         (已加载 {len(whitelist)} 条白名单豁免词)")
    print("=" * 65)

    for f in files:
        content = f.read_text(encoding='utf-8', errors='ignore')
        findings = lint_text(f, content, whitelist)
        if findings:
            print(f"\n[文件]: {f.name} (共发现 {len(findings)} 处待优化项)")
            print("-" * 65)
            for item in findings:
                total_issues += 1
                print(f"  * [第 {item['line']} 行] [{item['gate']}] 命中: \"{item['matched']}\"")
                print(f"    上下文: {item['snippet']}")
                print(f"    建议: {item['tip']}\n")

    if total_issues == 0:
        print("[OK] 扫描完成：未发现明显的网文 AI 套路词与违规句式，成稿质量优良！")
    else:
        print(f"[WARN] 扫描完成：累计发现 {total_issues} 处疑似 AI 味标记，请对照优化。")
    print("=" * 65)


if __name__ == "__main__":
    main()
