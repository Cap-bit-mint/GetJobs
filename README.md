# GetJobs Skill

> 求职全流程助手 - JD 抓取、简历匹配、投递追踪、简历联动

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/AI%20Skill-GetJobs-6f42c1)](SKILL.md)

[English](README.en.md) · [安装指南](docs/installation.md) · [平台指南](docs/platform_guide.md)

---

## 这个 Skill 解决什么问题

| 痛点 | GetJobs 如何处理 |
|------|-----------------|
| JD 信息分散在多个平台 | 一站式搜索和抓取 |
| 不知道 JD 与简历的匹配度 | 量化匹配分析 |
| 投递后忘记跟进 | 投递状态追踪 |
| 每个 JD 都要手动优化简历 | 与简历 Skill 联动生成定制简历 |

---

## 核心功能

### 1. JD 抓取

- 搜索目标公司/岗位
- 自动抓取 JD 内容
- 支持国内外主流招聘平台
- API 优先，降级到浏览器自动化

### 2. 匹配分析

- JD 要求解析
- 简历匹配度计算
- 多 JD 横向对比
- 竞争力分析

### 3. 投递追踪

- 投递记录管理
- 状态自动更新
- 跟进提醒
- 周报/月报统计

### 4. 简历联动

- 调用 `resume-jd-optimizer-cn` 生成定制简历
- 生成配套求职信
- 追踪记录关联

---

## Quick Start

### 安装

```bash
git clone https://github.com/your-repo/getjobs-skill.git \
  ~/.codex/skills/getjobs-skill
```

### 基本使用

**搜索 JD：**
```
帮我搜索腾讯的产品经理 JD。
```

**分析匹配度：**
```
分析我的简历与这个 JD 的匹配度。
JD：[粘贴 JD]
简历：[粘贴简历]
```

**追踪投递：**
```
添加投递记录：
公司：字节跳动
岗位：高级产品经理
匹配分：85
```

**生成定制简历：**
```
为这个 JD 生成定制简历和求职信。
```

---

## 文件结构

```
getjobs-skill/
├── SKILL.md                    # 核心规则与工作流
├── prompts/
│   ├── job_search.md           # JD 搜索与抓取
│   ├── matcher.md              # JD-简历匹配
│   ├── tracker.md             # 投递追踪
│   └── cover_letter.md         # 求职信生成
├── rubrics/
│   └── match_score.md         # 匹配度评分规则
├── templates/
│   ├── job_tracking_template.md
│   └── cover_letter_template.md
├── docs/
│   ├── installation.md         # 安装指南
│   ├── platform_guide.md        # 平台使用指南
│   ├── storage_format.md        # 存储格式
│   └── privacy.md             # 隐私政策
├── tools/
│   ├── browser_automation.md   # 浏览器自动化
│   └── api_services.md         # API 配置
└── examples/
    └── sample_tracking.md     # 追踪示例
```

---

## 支持的平台

### 国内平台
- 官网招聘页（最高优先级）
- Boss 直聘
- 拉勾
- 猎聘
- 智联招聘
- 前程无忧

### 海外平台
- LinkedIn
- Indeed
- Glassdoor
- RemoteOK
- Wellfound (AngelList)

---

## 数据存储

所有数据本地存储，保护用户隐私：

```
~/.getjobs/
├── applications.json      # 投递记录
├── config.json           # 配置文件
├── cache/jds/          # JD 缓存
└── output/              # 生成的简历/求职信
```

详见 [隐私政策](docs/privacy.md)。

---

## 与 resume-jd-optimizer-cn 联动

GetJobs 专注于职位管理和 JD 分析，在需要生成定制简历时，可调用 `resume-jd-optimizer-cn`：

```markdown
我想投递这个岗位，请调用简历优化 Skill。
```

联动流程：
1. 用户选择目标 JD
2. 调用简历 Skill 生成定制简历
3. 可选生成求职信
4. 更新投递追踪记录

---

## License

MIT License - 详见 [LICENSE](../LICENSE)
