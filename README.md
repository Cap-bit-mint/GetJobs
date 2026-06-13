# GetJobs Skill

> 求职全流程助手 - JD 抓取、简历匹配、简历优化、投递追踪、求职信生成

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/AI%20Skill-GetJobs-6f42c1)](SKILL.md)

[English](README.en.md) · [安装指南](docs/installation.md) · [平台指南](docs/platform_guide.md)

---

## 这个 Skill 解决什么问题

| 痛点 | GetJobs 如何处理 |
|------|-----------------|
| JD 信息分散在多个平台 | 一站式搜索和抓取 |
| 不知道 JD 与简历的匹配度 | 量化匹配分析 |
| 简历与 JD 不匹配 | 基于真实经历优化定制简历 |
| 投递后忘记跟进 | 投递状态追踪 |
| 每个 JD 都要写求职信 | 基于简历生成定制求职信 |

---

## 核心功能

### 1. JD 抓取

- 搜索目标公司/岗位
- 自动抓取 JD 内容
- 支持国内外主流招聘平台
- API 优先，降级到浏览器自动化

### 2. 简历匹配

- JD 要求解析
- 简历匹配度计算
- 多 JD 横向对比
- 竞争力分析

### 3. 简历优化（内置）

- JD 解析与证据映射
- 缺口诊断与素材追问
- 定制简历重写（保留真实经历）
- ATS 纯文本版生成
- 面试追问生成
- 五维评分：JD 匹配 / ATS / HR 吸引力 / 面试准备 / 可信度

### 4. 投递追踪

- 投递记录管理
- 状态自动更新
- 跟进提醒
- 周报/月报统计

### 5. 求职信生成

- 基于简历生成定制求职信
- 支持多种格式（标准/精简/BOSS直聘）
- 自动关联投递记录

---

## Quick Start

### 安装

```bash
git clone https://github.com/Cap-bit-mint/GetJobs.git \
  ~/.codex/skills/getjobs
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

**优化简历：**
```
为这个 JD 优化我的简历。
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

**生成求职信：**
```
为这个 JD 生成一封求职信。
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
│   ├── cover_letter.md        # 求职信生成
│   └── resume/                 # 简历优化模块
│       ├── resume_optimizer.md    # 核心工作流
│       ├── jd_parser.md          # JD 解析
│       ├── resume_parser.md        # 简历解析
│       ├── gap_analyzer.md        # 缺口分析
│       ├── experience_interviewer.md # 素材追问
│       ├── resume_rewriter.md      # 简历重写
│       ├── ats_checker.md         # ATS 检查
│       ├── hr_reviewer.md         # HR 视角检查
│       ├── interview_question_generator.md # 面试追问
│       ├── risk_checker.md       # 风险检查
│       ├── final_report_generator.md # 最终报告
│       └── truthfulness_policy.md  # 真实性政策
├── rubrics/
│   ├── match_score.md         # JD-简历匹配分
│   └── resume/                # 简历评分
│       ├── jd_match_score.md
│       ├── ats_score.md
│       ├── hr_score.md
│       ├── interview_readiness_score.md
│       └── credibility_score.md
├── templates/
│   ├── job_tracking_template.md
│   ├── cover_letter_template.md
│   └── resume/                # 简历模板
│       ├── jd_match_report_template.md
│       ├── optimized_resume_template.md
│       └── ats_plain_text_template.md
├── docs/
│   ├── installation.md         # 安装指南
│   ├── platform_guide.md        # 平台使用指南
│   ├── storage_format.md        # 存储格式
│   └── privacy.md             # 隐私政策
├── tools/
│   ├── browser_automation.md   # 浏览器自动化
│   └── api_services.md         # API 配置
└── examples/
    ├── sample_tracking.md     # 追踪示例
    └── resume/                 # 简历优化示例
        └── sample_optimization.md
```

---

## 支持的平台

### 国内平台
- 官网招聘页（最高优先级）
- Boss 直聘、拉勾、猎聘、智联招聘、前程无忧

### 海外平台
- LinkedIn、Indeed、Glassdoor、RemoteOK、Wellfound

---

## 数据存储

所有数据本地存储，保护用户隐私：

```
~/.getjobs/
├── applications.json      # 投递记录
├── config.json         # 配置文件
├── cache/jds/          # JD 缓存
└── output/
    ├── resumes/       # 生成的简历
    └── cover_letters/  # 生成的求职信
```

详见 [隐私政策](docs/privacy.md)。

---

## License

MIT License - 详见 [LICENSE](../LICENSE)
