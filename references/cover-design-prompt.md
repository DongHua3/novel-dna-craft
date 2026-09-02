# 网文封面视觉设计与 AI 提示词规范（Cover Design Reference）

本规范用于根据小说书名、题材、人设与目标平台，生成专业级 AI 封面提示词（支持 Midjourney / DALL-E / GPT-Image / SD）或直接生成封面。

---

## 一、 平台尺寸与视觉风格矩阵

| 目标平台 | 上传比例 | 像素规格 | 核心视觉特征 | 平台风格关键词（英文提示词） |
| :--- | :---: | :---: | :--- | :--- |
| **番茄小说** | **3:4** | 600×800 | 人物特写占 60%+，面部清晰，书名超大粗体带发光/金属光效，高对比高饱和冲击力 | `vibrant saturated colors, eye-catching bold design, character portrait dominating frame, mass-market novel cover style, high contrast` |
| **起点中文网** | **2:3** | 600×900 | 细腻厚重写实插画，电影级光影构图，书名偏传统毛笔书法楷体，人物与场景均衡 | `polished refined illustration, detailed cinematic composition, epic atmospheric, mature sophisticated style, premium quality` |
| **晋江文学城** | **2:3** | 600×900 | 柔和粉紫/浅蓝唯美色调，五官精致，花瓣光斑丝绸点缀，居中对称，书名优雅行书 | `dreamy ethereal aesthetic, soft pastel tones, elegant romantic, delicate beauty, flower petals and bokeh` |
| **知乎盐言** | **2:3** | 600×900 | 极简留白，冷淡色调（暗灰/藏蓝），氛围感重于人物细节，独立电影海报质感，现代无衬线体 | `minimalist literary style, clean composition with negative space, subtle moody atmosphere, independent film poster aesthetic` |
| **七猫中文网** | **3:4** | 600×800 | 极度饱和，火焰/雷电/金光等华丽战力特效，海报级视觉冲击力 | `striking high-impact design, vivid dramatic colors, spectacular visual effects, attention-grabbing poster style` |
| **刺猬猫** | **2:3** | 600×900 | 日系二次元轻小说插画，明亮线稿，Q版/萌系元素，书名卡通手绘风 | `anime illustration style, vibrant colorful, detailed character art, Japanese light novel aesthetic` |

---

## 二、 题材视觉与字体设计映射表

### 1. 书名字体风格设计
- **玄幻 / 仙侠**：`bold golden brush calligraphy with metallic glow and sharp strokes`（金色霸气毛笔书法，带金属锐利光晕）
- **都市 / 爽文**：`modern bold sans-serif with metallic silver finish`（现代银色高光无衬线粗体）
- **古言 / 宫斗**：`elegant golden traditional Kai script with ornate decoration`（典雅烫金传统楷体）
- **现言 / 甜宠**：`soft rounded handwritten style in white with pink glow`（柔和圆润白粉手写体）
- **悬疑 / 惊悚**：`distorted bold cracked letters in blood red`（血色斑驳破碎裂纹字体）
- **科幻 / 末世**：`neon glowing futuristic font in electric blue`（电光蓝霓虹未来科技字体）
- **西幻 / 史诗**：`metallic embossed fantasy lettering with glow effect`（浮雕金属奇幻风格字体）

### 2. 作者名（署名）精致排版规则
> **铁律**：作者名必须与书名呼应，位置固定在 `bottom center`，必须带有精致装饰元素（横线/边框/小图标），保持安全距离不被平台裁切。

- **玄幻/仙侠**：`small refined white serif text with faint golden glow, flanked by delicate cloud-scroll ornaments on both sides, resting on a thin horizontal gold line`
- **都市/科幻**：`small clean white modern text with subtle drop shadow, positioned above a thin silver horizontal divider line`
- **古言/宫斗**：`small elegant dark red traditional text inside a thin golden rectangular border frame with corner decorations`
- **知乎/悬疑**：`small pale grey text with slight blur effect, almost hidden in the shadows, a thin cracked line underneath`

---

## 三、 完整 AI 封面提示词三层构建公式

```text
Prompt = [平台风格层] + [文字排版层] + [画面三层景深: 前景人物 + 中景场景 + 远景氛围] + [色彩与光效] + [安全区与画质参数]
```

### 标准提示词模板（英文输出）：

```text
Chinese web novel cover design, [平台风格描述].
Title text '{中文书名}' at top center in [书名字体风格描述].
Author name '{作者笔名}' at bottom center in [作者名字体风格描述].
[题材标签]: [主角人物特写：服饰材质、发型、眼神、动作姿势、武器道具].
[场景细节]: Foreground [前景细节], midground [中景建筑/山峦/战场], background [远景云海/星空/天光].
[色彩与光影]: [主色调与对比色], [光源方向，如 dramatic golden backlight from top / cold rim light from side].
Professional digital painting, highly detailed, sharp focus, 8k resolution, portrait [3:4 或 2:3] aspect ratio, keep all text within the central 85% safe area, no watermark.
```

---

## 四、 封面生成质量自检清单

1. **书名与笔名完整性**：中文文字是否清晰无乱码，位置是否在上下安全区内（避免被平台缩略图裁掉）；
2. **题材辨识度**：读者能否在 0.5 秒内通过主色调与主角武器/装束识别题材（如仙侠配飞剑流光，科幻配机械蓝光）；
3. **平台调性契合度**：番茄封面是否足够抓眼、起点封面是否足够有厚重感、知乎封面是否足够有电影故事感。
