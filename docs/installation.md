# 安装与接入指南

`getjobs-skill` 是一个用于求职全流程管理的 AI Skill，支持 JD 抓取、简历匹配、投递追踪和简历联动。

## 先理解文件作用

| 路径 | 作用 | 什么时候加载 |
|---|---|---|
| `SKILL.md` | 最高优先级规则、输入路由、输出要求 | 始终加载 |
| `prompts/` | JD 搜索、匹配、追踪等阶段 Prompt | 执行对应阶段时加载 |
| `templates/` | 追踪记录、求职信等输出模板 | 生成输出时加载 |
| `rubrics/` | 匹配度评分规则 | 评分时加载 |
| `docs/` | 平台指南、存储格式、隐私政策 | 需要时加载 |
| `tools/` | 浏览器自动化、API 配置说明 | JD 抓取时参考 |

## 获取项目文件

### 方式一：Git 克隆

```bash
git clone https://github.com/your-repo/getjobs-skill.git
cd getjobs-skill
```

### 方式二：下载 ZIP

1. 下载最新 Release
2. 解压到 `~/.getjobs/` 目录

## 安装到 Codex

### 标准安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/your-repo/getjobs-skill.git \
  ~/.codex/skills/getjobs-skill
```

### 验证安装

在新会话中输入：

```
使用 $getjobs-skill。
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
匹配分析使用 prompts/matcher.md 和 rubrics/match_score.md。
投递追踪使用 prompts/tracker.md。
简历联动调用 resume-jd-optimizer-cn。
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

### 场景 3：管理投递记录

```markdown
添加一条投递记录：
公司：xxx
岗位：xxx
匹配分：85
```

### 场景 4：生成定制简历

```markdown
为这个 JD 生成定制简历，然后写一封求职信。
JD：[粘贴 JD]
```

## 与 resume-jd-optimizer-cn 联动

### 前提条件

确保 `resume-jd-optimizer-cn` 已安装在 Codex：

```bash
git clone https://github.com/coinluu/resume-jd-optimizer-cn.git \
  ~/.codex/skills/resume-jd-optimizer-cn
```

### 联动触发

```markdown
我想投递这个岗位，请调用简历优化 Skill 生成定制简历。
JD：[粘贴 JD]
```

## 安装成功标准

- [ ] Skill 能说明自己的三条核心规则
- [ ] 能搜索并抓取 JD（或提示用户提供）
- [ ] 能分析简历与 JD 的匹配度
- [ ] 能创建和更新投递记录
- [ ] 能调用 resume-jd-optimizer-cn 生成定制简历

## 常见问题

### Q：JD 抓取失败怎么办？

A：GetJobs 支持多种数据来源，按优先级：
1. 官网招聘页
2. 用户直接提供 JD
3. Browser 插件自动化

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
cd ~/.codex/skills/getjobs-skill
git pull
```

## 获取帮助

- 查看 `SKILL.md` 了解核心规则
- 查看 `docs/platform_guide.md` 了解各平台使用方法
- 查看 `docs/privacy.md` 了解隐私政策
