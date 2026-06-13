# GetJobs - AI 求职全流程助手

> 🚀 **JD 抓取 → 简历匹配 → 简历优化 → 投递追踪 → 求职信生成** - 一站式 AI 求职解决方案

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Test Cases](https://img.shields.io/badge/Test%20Cases-29-green)](tests)
[![Skill](https://img.shields.io/badge/AI%20Skill-GetJobs-6f42c1)](SKILL.md)
[![GitHub stars](https://img.shields.io/github/stars/Cap-bit-mint/GetJobs)](https://github.com/Cap-bit-mint/GetJobs)
[![Platform](https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20%7C%20ChatGPT-ff6b6b)](README.md)
[![Language](https://img.shields.io/badge/Language-中文优先-red)](README.md)

---

```
┌─────────────────────────────────────────────────────────────────┐
│                        GetJobs 工作流                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   🔍 JD抓取          →  📊 匹配分析      →  ✍️ 简历优化          │
│   ├── 官网/平台       │   ├── 硬性条件     │   ├── JD定制        │
│   ├── API/浏览器      │   ├── 技能匹配     │   ├── ATS优化        │
│   └── 降级策略        │   ├── 缺口诊断     │   └── 五维评分       │
│                       │   └── 多JD对比     │                     │
│                                                                 │
│   📋 投递追踪         →  ✉️ 求职信生成    →  📈 周报统计         │
│   ├── 状态管理        │   ├── 自动生成     │   ├── 投递统计       │
│   ├── 跟进提醒        │   ├── 格式多样     │   ├── 面试进度       │
│   └── 隐私脱敏        │   └── 防止夸大     │   └── 下周目标       │
│                                                                 │
└───────────────────────────────────────────────��─────────────────┘
```

---

## ✨ 核心亮点

| 指标 | 数值 |
|------|------|
| 核心功能 | **5 大模块** |
| 测试用例 | **29 个自动化测试** |
| 简历评分维度 | **5 维体系** |
| 支持平台 | **20+ 国内外招聘平台** |
| 数据存储 | **100% 本地 · 隐私无忧** |

---

## 🎯 这个 Skill 解决什么问题

| 痛点 | GetJobs 如何处理 |
|------|-----------------|
| JD 信息分散在多个平台 | 🔍 一站式搜索和抓取 |
| 不知道 JD 与简历的匹配度 | 📊 量化匹配分析 |
| 简历与 JD 不匹配 | ✍️ 基于真实经历优化定制 |
| 投递后忘记跟进 | 📋 投递状态追踪 + 提醒 |
| 每个 JD 都要写求职信 | ✉️ 基于简历生成定制求职信 |

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/Cap-bit-mint/GetJobs.git \
  ~/.codex/skills/getjobs
```

### 基本使用

```
📌 搜索 JD          →  帮我搜索字节跳动的产品经理 JD
📌 分析匹配度       →  分析我的简历与这个 JD 的匹配度
📌 优化简历         →  为这个 JD 优化我的简历
📌 追踪投递         →  添加投递记录：公司xxx，岗位xxx，匹配分85
📌 生成求职信       →  为��个 JD 生成一封求职信
```

---

## 📁 项目结构

```
getjobs/
├── SKILL.md                    # 核心规则与工作流
├── README.md                   # 项目文档
├── LICENSE                     # MIT 许可证
│
├── prompts/                    # Prompt 模板
│   ├── job_search.md           # JD 搜索与抓取
│   ├── matcher.md              # JD-简历匹配
│   ├── tracker.md              # 投递追踪
│   ├── cover_letter.md         # 求职信生成
│   └── resume/                 # 简历优化 (12个模块)
│
├── rubrics/                    # 评分规则
│   ├── match_score.md           # 匹配分计算
│   └── resume/                 # 简历五维评分
│
├── templates/                  # 输出模板
│   ├── job_tracking_template.md
│   ├── cover_letter_template.md
│   └── resume/
│
├── docs/                       # 文档
│   ├── installation.md          # 安装指南
│   ├── platform_guide.md       # 平台使用
│   ├── storage_format.md       # 存储格式
│   ├── privacy.md              # 隐私政策
│   ├── workflow.md             # 工作流程
│   └── *.md                    # 其他参考文档
│
├── examples/                   # 示例
│   ├── sample_tracking.md      # 追踪示例
│   ├── job_samples.md          # JD 示例
│   └── resume/                 # 简历优化示例
│
└── tests/                      # 测试
    ├── test_*.py               # 自动化测试 (29个)
    ├── fixtures/               # 测试数据
    ├── test_cases.md           # 测试用例 (15个)
    └── failure_modes.md        # 失败模式 (22个)
```

---

## 🛠 支持的平台

### 国内平台

| 平台 | 优先级 | 抓取方式 |
|------|--------|----------|
| 官网招聘页 | ⭐⭐⭐ | API / 浏览器 |
| Boss 直聘 | ⭐⭐ | 用户提供 JD |
| 拉勾 | ⭐⭐ | 用户提供 JD |
| 猎聘 / 智联 / 前程无忧 | ⭐ | 用户提供 JD |

### 海外平台

| 平台 | 优先级 | 抓取方式 |
|------|--------|----------|
| LinkedIn | ⭐⭐⭐ | 用户提供 JD |
| Indeed | ⭐⭐⭐ | API / 浏览器 |
| Glassdoor / RemoteOK | ⭐⭐ | 浏览器 / API |

---

## 🔒 数据存储

```
~/.getjobs/
├── applications.json      # 投递记录
├── config.json           # 配置文件
├── resume.md             # 用户简历
�── cache/jds/            # JD 缓存
└── output/
    ├── resumes/          # 生成的简历
    └── cover_letters/    # 生成的求职信
```

> 💡 所有数据本地存储，保护用户隐私

---

## 📊 五维评分体系

| 评分维度 | 说明 | 满分 |
|----------|------|------|
| JD 匹配分 | 硬性条件、技能、经验、成果、职级匹配 | 100 |
| ATS 分 | 标准标题、关键词、结构、技能区、时间线 | 100 |
| HR 吸引力分 | 10秒方向、前部亮点、相关性、结果、简洁度 | 100 |
| 面试准备分 | 背景、贡献、方法、数据、复盘、JD关联 | 100 |
| 可信度分 | 数据来源、贡献边界、夸大风险、逻辑自洽 | 100 |

---

## ✅ 真实性保障

- 🔒 **证据三态标记**：已确认 / 待确认 / 模型推断
- 📈 **数据深度等级**：D0 无证据 → D4 实验体系
- 🎯 **贡献动词门槛**：支持 < 参与 < 负责 < 推动 < 主导
- 🚫 **造假拒绝机制**：立即停止并提供真实替代路径

---

## 📚 文档导航

| 文档 | 说明 |
|------|------|
| [安装指南](docs/installation.md) | 如何安装到 Codex/ChatGPT/Claude |
| [平台指南](docs/platform_guide.md) | 各招聘平台使用方法 |
| [工作流程](docs/workflow.md) | 完整工作流程详解 |
| [岗位类型](docs/role_taxonomy.md) | 20 类岗位参考 |
| [指标词典](docs/metric_dictionary.md) | 各岗位常用指标 |
| [招聘语境](docs/chinese_job_market_context.md) | 国内招聘特点 |
| [隐私政策](docs/privacy.md) | 数据安全说明 |

[English](README.en.md)

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

---

⭐ 如果这个项目对你有帮助，欢迎 Star！
