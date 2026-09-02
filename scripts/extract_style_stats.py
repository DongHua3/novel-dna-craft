#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_style_stats.py - 语料文风与句法特征快速提取脚本 (Zero-Dependency)
用法:
    python extract_style_stats.py <语料目录或文件路径>
功能:
    1. 统计总字数、总句数、总段落数
    2. 计算平均句长、短句(<=15字)占比、长句(>=45字)占比
    3. 统计标点使用习惯 (逗号密度、破折号、省略号、感叹号、问号)
    4. 统计对白占比 (引号内字符比例)
"""

import sys
import re
from pathlib import Path
from collections import Counter

# 确保在 Windows 控制台也能安全输出 UTF-8
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def analyze_text(text: str):
    if not text.strip():
        return None

    # 剔除 markdown 标记
    clean_text = re.sub(r'#+\s+.*', '', text)
    clean_text = re.sub(r'```.*?```', '', clean_text, flags=re.DOTALL)
    
    char_count = len(re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]', clean_text))
    if char_count == 0:
        return None

    # 段落
    paragraphs = [p.strip() for p in clean_text.split('\n') if len(p.strip()) > 0]
    
    # 句子切分 (按 。！？…)
    raw_sentences = re.split(r'[。！？\n]+', clean_text)
    sentences = [s.strip() for s in raw_sentences if len(s.strip()) >= 2]
    
    if not sentences:
        return None

    sent_lengths = [len(re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]', s)) for s in sentences]
    avg_sent_len = sum(sent_lengths) / len(sent_lengths)
    short_sents = sum(1 for l in sent_lengths if l <= 15)
    long_sents = sum(1 for l in sent_lengths if l >= 45)
    
    # 对话提取 (「」、“”)
    dialogues = re.findall(r'[“「](.*?)[”」]', clean_text)
    dialogue_chars = sum(len(d) for d in dialogues)
    dialogue_ratio = (dialogue_chars / char_count) * 100 if char_count > 0 else 0

    # 标点符号统计
    commas = len(re.findall(r'[，,]', clean_text))
    dashes = len(re.findall(r'——|--', clean_text))
    ellipses = len(re.findall(r'……|\.\.\.', clean_text))
    questions = len(re.findall(r'[？?]', clean_text))
    exclamations = len(re.findall(r'[！!]', clean_text))

    return {
        "char_count": char_count,
        "para_count": len(paragraphs),
        "sent_count": len(sentences),
        "avg_sent_len": round(avg_sent_len, 2),
        "short_sent_pct": round((short_sents / len(sentences)) * 100, 2),
        "long_sent_pct": round((long_sents / len(sentences)) * 100, 2),
        "dialogue_ratio_pct": round(dialogue_ratio, 2),
        "comma_per_1k": round((commas / char_count) * 1000, 2),
        "dash_per_1k": round((dashes / char_count) * 1000, 2),
        "ellipsis_per_1k": round((ellipses / char_count) * 1000, 2),
        "question_per_1k": round((questions / char_count) * 1000, 2),
        "exclamation_per_1k": round((exclamations / char_count) * 1000, 2),
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_style_stats.py <path_to_file_or_directory>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    texts = []
    
    if target_path.is_file():
        texts.append(target_path.read_text(encoding='utf-8', errors='ignore'))
    elif target_path.is_dir():
        for f in target_path.glob("**/*"):
            if f.suffix.lower() in ['.txt', '.md']:
                texts.append(f.read_text(encoding='utf-8', errors='ignore'))
    else:
        print(f"Error: Path {target_path} not found.")
        sys.exit(1)

    all_content = "\n".join(texts)
    stats = analyze_text(all_content)
    
    if not stats:
        print("No valid text found to analyze.")
        sys.exit(1)

    print("=" * 55)
    print("       【novel-dna-craft】语料文风统计报告")
    print("=" * 55)
    print(f"- 语料总汉字数:   {stats['char_count']:,} 字")
    print(f"- 总段落数:       {stats['para_count']} 段 (平均每段 {round(stats['sent_count']/stats['para_count'], 1)} 句)")
    print(f"- 平均单句字数:   {stats['avg_sent_len']} 字")
    print(f"- 短句(<=15字)比: {stats['short_sent_pct']}% (节奏紧张度指标)")
    print(f"- 长句(>=45字)比: {stats['long_sent_pct']}% (氛围铺垫指标)")
    print(f"- 对白占比:       {stats['dialogue_ratio_pct']}%")
    print("-" * 55)
    print("【标点与呼吸感指纹 (每千字出现频次)】")
    print(f"- 逗号密度:       {stats['comma_per_1k']} 次/千字")
    print(f"- 破折号密度:     {stats['dash_per_1k']} 次/千字")
    print(f"- 省略号密度:     {stats['ellipsis_per_1k']} 次/千字")
    print(f"- 问号密度:       {stats['question_per_1k']} 次/千字")
    print(f"- 感叹号密度:     {stats['exclamation_per_1k']} 次/千字")
    print("=" * 55)


if __name__ == "__main__":
    main()
