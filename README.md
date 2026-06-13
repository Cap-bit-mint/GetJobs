# GetJobs Skill

> 求职全流程助手 - JD 抓取、简历匹配、简历优化、投递追踪、求职信生成

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/AI%20Skill-GetJobs-6f42c1)](SKILL.md)
[![GitHub stars](https://img.shields.io/github/stars/Cap-bit-mint/GetJobs)](https://github.com/Cap-bit-mint/GetJobs)
[![Platform](https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20%7C%20ChatGPT-ff6b6b)](README.md)
[![Language](https://img.shields.io/badge/Language-中文优先-red)](README.md)

[English](README.en.md) · [安装指南](docs/installation.md) · [平台指南](docs/platform_guide.md) · [工作流](docs/workflow.md)

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

### 3. 简历优化（内置完整 8 步流程）

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
├── README.md                    # 本文件
├── LICENSE                     # MIT 许可证
│
├── prompts/                    # Prompt 模板
│   ├── job_search.md           # JD 搜索与抓取
│   ├── matcher.md              # JD-简历匹配
│   ├── tracker.md              # 投递追踪
│   ├── cover_letter.md         # 求职信生成
│   └── resume/                 # 简历优化模块 (12个)
│       ├── resume_optimizer.md           # 核心工作流
│       ├── jd_parser.md                 # JD 解析
│       ├── resume_parser.md              # 简历解析
│       ├── gap_analyzer.md              # 缺口分析
│       ├── experience_interviewer.md     # 素材追问
│       ├── resume_rewriter.md           # 简历重写
│       ├── ats_checker.md               # ATS 检查
│       ├── hr_reviewer.md               # HR 视角检查
│       ├── interview_question_generator.md # 面试追问
│       ├── risk_checker.md             # 风险检查
│       ├── final_report_generator.md    # 最终报告
│       └── truthfulness_policy.md      # 真实性政策
│
├── rubrics/                    # 评分规则
│   ├── match_score.md           # JD-简历匹配分
│   └── resume/                 # 简历评分 (5个)
│       ├── jd_match_score.md
│       ├── ats_score.md
│       ├── hr_score.md
│       ├── interview_readiness_score.md
│       └── credibility_score.md
│
├── templates/                  # 输出模板
│   ├── job_tracking_template.md    # 追踪模板
│   ├── cover_letter_template.md    # 求职信模板
│   └── resume/                 # 简历模板 (3个)
│       ├── jd_match_report_template.md
│       ├── optimized_resume_template.md
│       └── ats_plain_text_template.md
│
├── docs/                       # 文档
│   ├── installation.md           # 安装指南
│   ├── platform_guide.md        # 平台使用指南
│   ├── storage_format.md       # 存储格式
│   ├── privacy.md               # 隐私政策
│   ├── workflow.md              # 工作流程详解
│   ├── role_taxonomy.md         # 岗位类型参考
│   ├── metric_dictionary.md     # 指标词典
│   └── chinese_job_market_context.md # 招聘语境
│
├── tools/                      # 工具文档
│   ├── browser_automation.md   # 浏览器自动化
│   └── api_services.md         # API 配置
│
├── examples/                    # 示例
│   ├── sample_tracking.md       # 追踪示例
│   ├── job_samples.md           # JD 示例
│   └── resume/                 # 简历优化示例
│       └── sample_optimization.md
│
└── tests/                      # 测试
    ├── test_cases.md             # 测试用例 (15个)
    ├── failure_modes.md         # 失败模式 (22个)
    └── evaluation_checklist.md  # 验收清单
```

---

## 支持的平台

### 国内平台
| 平台 | 优先级 | 抓取方式 |
|------|--------|-----------|
| 官网招聘页 | 最高 | API / 浏览器 |
| Boss 直聘 | 高 | 用户提供 JD |
| 拉勾 | 高 | 用户提供 JD |
| 猎聘 | 中 | 用户提供 JD |
| 智联招聘 | 中 | 用户提供 JD |
| 前程无忧 | 中 | 用户提供 JD |

### 海外平台
| 平台 | 优先级 | 抓取方式 |
|------|--------|-----------|
| LinkedIn | 高 | 用户提供 JD |
| Indeed | 高 | API / 浏览器 |
| Glassdoor | 中 | 浏览器 |
| RemoteOK | 中 | API |
| Wellfound | 中 | 浏览器 |

---

## 数据存储

所有数据本地存储，保护用户隐私：

```
~/.getjobs/
├── applications.json      # 投递记录
├── config.json         # 配置文件
├── resume.md           # 用户简历
├── cache/jds/          # JD 缓存
└── output/
    ├── resumes/       # 生成的简历
    └── cover_letters/  # 生成的求职信
```

详见 [隐私政策](docs/privacy.md)。

---

## 工作流程

```
用户输入
    │
    ▼
┌─────────────────┐
│  路由判定          │
│  A/B/C/D/E       │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  8步工作流         │
│  Step 1-8        │
└─────────────────┘
    │
    ├──▶ JD 解析
    ├──▶ 简历解析
    ├──▶ 缺口分析
    ├──▶ 素材追问
    ├──▶ 简历重写
    ├──▶ 风险检查
    └──▶ 最终报告
```

详见 [工作流程文档](docs/workflow.md)。

---

## 五维评分体系

| 评分 | 说明 | 满分 |
|------|------|------|
| JD 匹配分 | 硬性条件、技能、经验、成果、职级匹配 | 100 |
| ATS 分 | 标准标题、关键词、结构、技能区、时间线 | 100 |
| HR 吸引力分 | 10秒方向、前部亮点、相关性、结果、简洁度 | 100 |
| 面试准备分 | 背景、贡献、方法、数据、复盘、JD关联 | 100 |
| 可信度分 | 数据来源、贡献边界、夸大风险、逻辑自洽 | 100 |

---

## 真实性保障

- **证据三态标记**：已确认 / 待确认 / 模型推断
- **数据深度等级**：D0 无证据 → D4 实验体系
- **贡献动词门槛**：支持 < 参与 < 负责 < 推动 < 主导
- **造假拒绝机制**：立即停止并提供真实替代路径

详见 [真实性政策](prompts/resume/truthfulness_policy.md)

---

## 相关资源

- [安装指南](docs/installation.md) - 如何安装到 Codex/ChatGPT/Claude
- [平台指南](docs/platform_guide.md) - 各招聘平台使用方法
- [工作流](docs/workflow.md) - 完整工作流程详解
- [岗位类型](docs/role_taxonomy.md) - 20 类岗位参考
- [指标词典](docs/metric_dictionary.md) - 各岗位常用指标
- [招聘语境](docs/chinese_job_market_context.md) - 国内招聘特点

---

## License

MIT License - 详见 [LICENSE](LICENSE)
