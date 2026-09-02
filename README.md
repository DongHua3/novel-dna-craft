# novel-dna-craft：网文灵肉合一 AI 创作引擎

[![Novel DNA Craft](https://img.shields.io/badge/Skill-Novel%20DNA%20Craft-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **取其精华，去其糟粕**：深度融合 `writing-dna-skill` 的 **6 层名家文风蒸馏方法论** 与 `oh-story-claudecode` 的 **商业网文工业化架构（大纲/伏笔/正文/去AI/审稿/封面/老书接续）**，打造让 AI 兼具“商业爽点骨架”与“名家文风灵魂”的新一代小说创作引擎。

---

## 一、 为什么做这个整合？（取精华 · 补短板）

| 来源项目 | 汲取的【核心精华】 | 解决的【原项目缺陷/短板】 |
| :--- | :--- | :--- |
| **`writing-dna-skill`** | 6 层文风深度蒸馏体系（L1 句长呼吸感 ~ L5 认知模型）、前置 5 篇原文语感校准机制、文风豁免权原则、信息守恒铁律。 | 解决其**“仅支持单篇短文、缺乏长篇大纲与长程伏笔状态系统”**的致命局限性。 |
| **`oh-story-claudecode`** | 起点/番茄/知乎商业网文大纲法、黄金三章节奏、**全书长程伏笔与状态追踪矩阵 (`FB-xxx`)**、7-Gate 网文去 AI 味、4 视角审稿体系、三层上下文架构、对白权力博弈法则、六大情绪弧线、老书逆向接续、平台封面设计。 | 解决其**“13 个 Skill 过度分散繁琐、正文自带平庸通识 AI 腔、强依赖 Node.js/CLI”**的工程与文风缺陷。 |

---

## 二、 目录结构与权威规范库

```text
novel-dna-craft/
├── SKILL.md                          # 统一入口与 8 大模式调度中心
├── README.md                         # 架构说明与快速上手手册
├── LICENSE                           # MIT 开源许可证与致谢
├── .gitignore                        # 保护私有语料与草稿
├── references/                       # 核心规范与知识库
│   ├── dna-distillation.md           # 6 层文风蒸馏方法论 (L1-L6) & 元数据 Schema
│   ├── commercial-outlining.md       # 商业网文大纲与黄金三章设计标准
│   ├── scene-functional-writing.md   # 场景功能化正文生成协议 (三层上下文架构)
│   ├── dialogue-and-emotional-arc.md # 对白权力博弈法则 (压制/反转/心死) 与六大情绪弧线
│   ├── legacy-book-import.md         # 老书与断更草稿逆向接续协议
│   ├── market-and-publishing.md      # 四大主流平台 (起点/番茄/知乎/晋江) 过签指南与受众偏好
│   ├── fiction-deslop-7gates.md      # 7-Gate 网文去AI味规范 (带DNA豁免权与信息守恒)
│   ├── banned-words.md               # 完整 AI 味禁用词与最毒句式清单
│   ├── multi-agent-review.md         # 4-Agent 多视角审稿标准与四维评分矩阵
│   └── cover-design-prompt.md        # 平台级小说封面设计与 AI 提示词规范 (番茄/起点/知乎等)
├── templates/                        # 模版库
│   ├── author-dna/                   # 文风蒸馏模版 (语言DNA, Writing-DNA)
│   │   ├── 语言DNA.template.md
│   │   ├── 文章结构模板.template.md
│   │   ├── 写作视角与认知框架.template.md
│   │   └── Writing-DNA.template.md
│   └── novel-project/                # 小说项目骨架模版
│       ├── 00_作品总览与设定.md
│       ├── 01_世界观与战力体系.md
│       ├── 02_核心角色档案与声纹表.md
│       ├── 03_分卷主线与黄金三章细纲.md
│       ├── 04_伏笔与状态追踪表.md
│       └── 短篇_故事核与反转架构.md
└── scripts/                          # 辅助分析 Python 脚本 (零依赖极速运行，跨平台兼容)
    ├── extract_style_stats.py        # 语料句长、标点、词频与对话比快速统计
    └── deslop_linter.py              # 7-Gate 网文套路词与违规句式快速质检
```

---

## 三、 指令矩阵一览

| 指令 | 模式 | 一句话描述 |
| :--- | :--- | :--- |
| `/novel-dna distill` | **文风蒸馏** | 从名家 20+ 章节中提取 L1~L5 规则，生成专属 `Writing-DNA.md` |
| `/novel-dna scan` | **扫榜洞察** | 扫描各大平台风口题材与爆款金手指趋势 |
| `/novel-dna outline` | **商业大纲** | 自动构思世界观、角色声纹表、分卷主线与黄金三章（或短篇反转） |
| `/novel-dna import` | **老书接续** | 导入已有断更章节，逆向还原人物快照与伏笔，无缝续写下一章 |
| `/novel-dna write` | **正文推进** | 融合文风 DNA + 权力博弈对白 + 情绪弧线，生成沉浸正文并自动更新伏笔状态 |
| `/novel-dna deslop` | **网文去AI** | 执行 7-Gate 门禁（清除套路词/僵硬对话/监控式流水账，遵循信息守恒） |
| `/novel-dna review` | **4视角审稿** | 读者留存、战力一致、网文主编、文风质检四维量化打分（S/A/B 级） |
| `/novel-dna cover` | **封面设计** | 依据平台特性自动生成 Midjourney / SD 提示词与专业排版封面 |

---

## 四、 致谢与开源协议（License & Acknowledgements）

本项目基于 **MIT License** 开源。感谢以下开源项目奠定的开创性探索与坚实基础：

1. **[oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)** (by @zenstory-ai) - 商业网文工业化大纲、黄金三章节奏、7-Gate 去AI味与多视角审稿矩阵。
2. **[writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill)** & **[lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)** (by @larashero3) - 6 层文风深度蒸馏方法论、语言学信息守恒与去AI味实证研究。
