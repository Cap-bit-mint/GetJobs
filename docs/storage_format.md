# 数据存储格式说明

本文档说明 GetJobs Skill 的数据存储格式和结构。

## 存储目录结构

```
~/.getjobs/
├── applications.json      # 投递记录主文件
├── config.json           # 配置文件
├── resume.md             # 用户主简历
├── cache/
│   ├── jds/              # 缓存的 JD 文本
│   └── analysis/         # 缓存的分析结果
└── output/
    ├── resumes/          # 生成的定制简历
    ├── cover_letters/   # 生成的求职信
    └── reports/          # 生成的报告
```

## 配置文件格式

### config.json

```json
{
  "version": "1.0",
  "last_updated": "2026-06-13",

  "paths": {
    "resume": "~/.getjobs/resume.md",
    "output_dir": "~/.getjobs/output",
    "cache_dir": "~/.getjobs/cache"
  },

  "api_services": {
    "enabled": false,
    "services": {}
  },

  "browser": {
    "fallback_enabled": true,
    "default_delay_ms": 2000,
    "max_retries": 3
  },

  "privacy": {
    "save_critical_data": true,
    "backup_before_write": true,
    "backup_count": 5
  },

  "defaults": {
    "follow_up_days": 7,
    "match_threshold": 60
  }
}
```

## 投递记录格式

### applications.json（主文件）

```json
{
  "version": "1.0",
  "last_updated": "2026-06-13T10:30:00Z",

  "config": {
    "resume_path": "~/.getjobs/resume.md",
    "output_dir": "~/.getjobs/output"
  },

  "applications": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "created_at": "2026-06-10T14:00:00Z",
      "last_updated": "2026-06-13T10:30:00Z",

      "company": "字节跳动",
      "position": "高级产品经理",
      "department": "电商产品",

      "platform": "boss",
      "source_url": "https://www.zhipin.com/job_detail/xxx.html",
      "jd_hash": "sha256:abc123...",

      "jd_summary": "负责电商订单系统，3年+B端经验，需SQL...",,

      "match_score": 85,
      "salary_range": "35-60k",
      "salary_currency": "CNY",
      "location": "北京",
      "remote_policy": "onsite",

      "applied_date": "2026-06-10",
      "status": "viewed",
      "status_reason": "",

      "status_history": [
        {
          "status": "pending",
          "date": "2026-06-10T14:00:00Z",
          "note": "创建记录"
        },
        {
          "status": "viewed",
          "date": "2026-06-12T09:00:00Z",
          "note": "HR 已查看"
        }
      ],

      "follow_up_date": "2026-06-17",
      "follow_up_reminded": false,

      "resume_version": "v2",
      "resume_path": "~/.getjobs/output/resumes/字节跳动-高级产品经理-v2.md",
      "cover_letter": true,
      "cover_letter_path": "~/.getjobs/output/cover_letters/字节跳动-高级PM.md",

      "interview_rounds": 0,
      "interviews": [],

      "feedback": "",
      "rejection_reason": "",

      "notes": "内推渠道，HR 姓张",

      "priority": "high",

      "tags": ["b端", "电商", "内推"],

      "deleted": false,
      "deleted_at": null
    }
  ]
}
```

## JD 缓存格式

### ~/.getjobs/cache/jds/{hash}.json

```json
{
  "hash": "sha256:abc123...",
  "crawled_at": "2026-06-10T14:00:00Z",
  "source": {
    "platform": "boss",
    "url": "https://www.zhipin.com/job_detail/xxx.html",
    "company": "字节跳动",
    "position": "高级产品经理"
  },
  "raw_content": "完整 JD 原始文本...",
  "parsed": {
    "company": "字节跳动",
    "position": "高级产品经理",
    "department": "电商产品",
    "location": "北京",
    "salary_range": "35-60k",
    "salary_currency": "CNY",
    "job_type": "fulltime",
    "experience": "3-5年",
    "education": "本科及以上",
    "requirements": ["B端产品经验", "SQL", "PRD输出"],
    "responsibilities": ["负责订单系统", "跨团队推进"],
    "preferred": ["有电商经验", "有数据背景"],
    "benefits": ["六险一金", "免费三餐"]
  },
  "parsed_at": "2026-06-10T14:05:00Z"
}
```

## 输出文件格式

### 定制简历

```
~/.getjobs/output/resumes/{公司名}-{岗位名}-v{n}.md
```

文件头：

```markdown
---
version: v2
company: 字节跳动
position: 高级产品经理
generated_at: 2026-06-10
source_jd_hash: sha256:abc123...
---
```

### 求职信

```
~/.getjobs/output/cover_letters/{公司名}-{岗位名}.md
```

文件头：

```markdown
---
type: cover_letter
version: 1.0
company: 字节跳动
position: 高级产品经理
generated_at: 2026-06-10
---
```

### 分析报告

```
~/.getjobs/output/reports/{公司名}-{岗位名}-match-report.md
```

## 字段类型定义

### 枚举类型

| 字段 | 可选值 |
|------|--------|
| platform | boss, lagou, liepin, zhilian, 51job, linkedin, indeed, glassdoor, company_website, other |
| status | pending, viewed, interview, offer, rejected, withdrawn |
| remote_policy | onsite, hybrid, remote |
| job_type | fulltime, intern, contract |
| priority | high, medium, low |
| salary_currency | CNY, USD, EUR, GBP, other |
| education | high_school, associate, bachelor, master, doctoral |

### 日期格式

所有日期使用 ISO 8601 格式：
- `2026-06-13` - 仅日期
- `2026-06-13T10:30:00Z` - 完整时间戳（UTC）

### 哈希计算

JD 内容使用 SHA-256 哈希，用于去重和版本追踪：

```javascript
const hash = crypto
  .createHash('sha256')
  .update(jdContent)
  .digest('hex');
```

## 版本管理

### 数据迁移

当配置格式变更时：

1. 在文件中保留 `version` 字段
2. 在代码中处理版本兼容
3. 不删除旧字段，标记为 deprecated

### 备份策略

每次写入前自动备份：
- 保留最近 5 个备份
- 备份文件命名：`{filename}.backup.{timestamp}`

## 导出格式

### JSON（完整数据）

```bash
cat ~/.getjobs/applications.json | jq .
```

### CSV（表格数据）

```csv
id,company,position,platform,match_score,salary_range,location,applied_date,status,follow_up_date,priority
550e8400-e29b-41d4-a716-446655440000,字节跳动,高级产品经理,boss,85,35-60k,北京,2026-06-10,viewed,2026-06-17,high
```

### Markdown（报告）

```markdown
## 投递记录

| 公司 | 岗位 | 平台 | 匹配分 | 状态 |
|------|------|------|--------|------|
```

## 错误处理

### 文件不存在

首次使用自动创建默认配置：
```json
{
  "version": "1.0",
  "applications": []
}
```

### 格式错误

回退到上一个正确版本，并报告错误。

### 权限错误

提示用户检查文件权限，或使用备用目录。
