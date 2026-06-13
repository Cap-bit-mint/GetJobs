# 安装与接入指南

`getjobs-skill` 是一个用于求职全流程管理的 AI Skill，支持 JD 抓取、简历匹配、简历优化、投递追踪和求职信生成。

## 先理解文件作用

| 路径 | 作用 | 什么时候加载 |
|---|---|---|
| `SKILL.md` | 最高优先级规则、输入路由、输出要求 | 始终加载 |
| `prompts/` | JD 搜索、匹配、优化、追踪等阶段 Prompt | 执行对应阶段时加载 |
| `templates/` | 追踪记录、简历、求职信等输出模板 | 生成输出时加载 |
| `rubrics/` | 匹配度评分规则 | 评分时加载 |
| `docs/` | 平台指南、存储格式、隐私政策 | 需要时加载 |
| `tools/` | 浏览器自动化、API 配置说明 | JD 抓取时参考 |

## 获取项目文件

### 方式一：Git 克隆

```bash
git clone https://github.com/Cap-bit-mint/GetJobs.git
cd GetJobs
```

### 方式二：下载 ZIP

1. 下载最新 Release
2. 解压到 `~/.codex/skills/getjobs/` 目录

## 安装到 Codex

### 标准安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Cap-bit-mint/GetJobs.git \
  ~/.codex/skills/getjobs
```

### 验证安装

在新会话中输入：

```
使用 $getjobs。
说说你能做什么。
```

## 安装到 ChatGPT / Claude

### 方式一：自定义 GPT

1. 创建新的自定义 GPT
2. 将 `SKILL.md` 内容放入 Instructions
3. 上传 `prompts/`、`templates/`、`rubrics/` 为 Knowledge
4. 上传 `docs/`、`tools/` 为参考文档

### 方式二：Project Instructions

```
始终加载 SKILL.md 作为最高优先级工作流。
JD 抓取使用 prompts/job_search.md。
简历优化使用 prompts/resume/ 目录下的文件。
投递追踪使用 prompts/tracker.md。
求职信生成使用 prompts/cover_letter.md。
评分使用 rubrics/ 目录下的文件。
```

## 首次配置

### 1. 创建数据目录

```bash
mkdir -p ~/.getjobs/{cache/jds,output/{resumes,cover_letters,reports}}
```

### 2. 配置文件（可选）

创建 `~/.getjobs/config.json`：

```json
{
  "version": "1.0",
  "api_services": {
    "enabled": false
  },
  "browser": {
    "fallback_enabled": true
  }
}
```

### 3. 准备简历

将简历保存为 `~/.getjobs/resume.md`：

```markdown
# 我的简历

## 基本信息
姓名：...
手机：...（建议脱敏）
邮箱：...

## 教育背景
...

## 工作经历
...

## 项目经历
...

## 技能清单
...
```

## 快速开始

### 场景 1：搜索并抓取 JD

```markdown
帮我搜索 [公司名] 的 [岗位名] JD。
```

### 场景 2：分析匹配度

```markdown
分析我的简历与这个 JD 的匹配度：

JD：[粘贴 JD 内容]
简历：[粘贴简历]
```

### 场景 3：优化简历

```markdown
为这个 JD 优化我的简历。

JD：[粘贴 JD 内容]
简历：[粘贴简历]

请先分析差距，追问关键信息后再生成最终简历。
```

### 场景 4：管理投递记录

```markdown
添加一条投递记录：
公司：xxx
岗位：xxx
匹配分：85
```

### 场景 5：生成求职信

```markdown
为这个 JD 生成一封求职信。
```

## 安装成功标准

- [ ] Skill 能说明自己的三条核心规则
- [ ] 能搜索并抓取 JD（或提示用户提供）
- [ ] 能分析简历与 JD 的匹配度
- [ ] 能基于真实经历优化定制简历
- [ ] 能创建和更新投递记录
- [ ] 能生成定制求职信

## 常见问题

### Q：JD 抓取失败怎么办？

A：GetJobs 支持多种数据来源，按优先级：
1. 官网招聘页
2. 用户直接提供 JD
3. Browser 插件自动化

### Q：简历优化需要提供什么？

A：最好同时提供 JD 和简历。如果没有 JD，只能做基础简历诊断；如果没有简历，只能解析 JD。

### Q：如何导出投递记录？

A：使用追踪命令：

```markdown
导出投递记录为 CSV 格式。
```

### Q：如何删除所有数据？

A：删除本地数据目录：

```bash
rm -rf ~/.getjobs
```

## 更新 Skill

```bash
cd ~/.codex/skills/getjobs
git pull
```

## 获取帮助

- 查看 `SKILL.md` 了解核心规则
- 查看 `docs/platform_guide.md` 了解各平台使用方法
- 查看 `docs/privacy.md` 了解隐私政策
