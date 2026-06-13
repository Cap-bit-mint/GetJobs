# 投递追踪模板

## 投递记录文件

```json
{
  "version": "1.0",
  "last_updated": "{{last_updated}}",
  "config": {
    "default_resume_path": "~/.getjobs/resume.md",
    "output_dir": "~/.getjobs/output",
    "auto_backup": true,
    "backup_count": 5
  },
  "applications": []
}
```

## 单条投递记录

```json
{
  "id": "{{uuid}}",
  "created_at": "{{created_at}}",
  "last_updated": "{{last_updated}}",

  "company": "{{company_name}}",
  "position": "{{position_name}}",
  "department": "{{department}}",

  "platform": "{{platform}}",
  "source_url": "{{jd_source_url}}",
  "jd_summary": "{{jd_summary_100_chars}}",

  "match_score": {{match_score}},
  "salary_range": "{{salary_range}}",
  "salary_currency": "CNY/USD",
  "location": "{{location}}",
  "remote_policy": "{{onsite/hybrid/remote}}",
  "job_type": "{{fulltime/intern/contract}}",

  "applied_date": "{{applied_date}}",
  "status": "{{pending/viewed/interview/offer/rejected/withdrawn}}",

  "status_history": [
    {
      "status": "{{status}}",
      "date": "{{date}}",
      "note": "{{note}}"
    }
  ],

  "follow_up_date": "{{follow_up_date}}",
  "follow_up_reminded": false,

  "resume_version": "{{v1/v2/v3}}",
  "resume_path": "{{path_to_resume}}",
  "cover_letter": {{true/false}},
  "cover_letter_path": "{{path_to_cover_letter}}",

  "interview_rounds": {{number}},
  "interviews": [
    {
      "round": 1,
      "type": "{{phone/video/onsite}}",
      "date": "{{date}}",
      "feedback": "{{feedback}}",
      "result": "{{passed/failed/pending}}"
    }
  ],

  "feedback": "{{hr_feedback}}",
  "rejection_reason": "{{reason}}",

  "notes": "{{user_notes}}",
  "priority": "{{high/medium/low}}",

  "tags": ["{{tag1}}", "{{tag2}}"],

  "deleted": false,
  "deleted_at": null
}
```

## 状态流转图

```
                        ┌─────────────┐
                        │   PENDING   │
                        │    待查看    │
                        └──────┬──────┘
                               │
                    ┌──────────┼──────────┐
                    ▼          ▼          ▼
              ┌─────────┐ ┌─────────┐ ┌──────────┐
              │ VIEWED  │ │REJECTED │ │WITHDRAWN │
              │ 已查看  │ │  已拒绝  │ │  已撤回   │
              └────┬────┘ └─────────┘ └──────────┘
                   │
                   ▼
              ┌─────────┐
              │INTERVIEW│
              │  面试中  │
              └────┬────┘
                   │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
   ┌─────────┐ ┌─────────┐ ┌──────────┐
   │  OFFER  │ │REJECTED │ │WITHDRAWN │
   │   Offer │ │  已拒绝  │ │  已撤回   │
   └─────────┘ └─────────┘ └──────────┘
```

## 统计指标

### 周统计

```markdown
## 本周统计

| 指标 | 数值 |
|------|------|
| 新投递 | {{count}} |
| 收到查看 | {{count}} |
| 进入面试 | {{count}} |
| 收到 Offer | {{count}} |
| 被拒绝 | {{count}} |

本周投递率：{{rate}}%
面试转化率：{{conversion_rate}}%
```

### 月统计

```markdown
## 本月统计

| 指标 | 本月 | 累计 |
|------|------|------|
| 投递总数 | {{count}} | {{total}} |
| 平均匹配分 | {{avg}} | - |
| 最高匹配分 | {{max}} | - |
| 进入面试率 | {{rate}}% | - |
```

### 平台统计

```markdown
## 平台分布

| 平台 | 投递数 | 进入面试 | 面试率 |
|------|--------|----------|--------|
| Boss 直聘 | {{count}} | {{count}} | {{rate}}% |
| 官网 | {{count}} | {{count}} | {{rate}}% |
| 拉勾 | {{count}} | {{count}} | {{rate}}% |
| 猎聘 | {{count}} | {{count}} | {{rate}}% |
| LinkedIn | {{count}} | {{count}} | {{rate}}% |
```

## 导出格式

### CSV 格式

```csv
ID,公司,岗位,平台,匹配分,薪资,地点,投递日期,状态,跟进日期,备注
{{id}},{{company}},{{position}},{{platform}},{{match_score}},{{salary}},{{location}},{{date}},{{status}},{{follow_up}},{{notes}}
```

### Markdown 格式

```markdown
## 投递记录

| 公司 | 岗位 | 平台 | 匹配分 | 状态 | 跟进日期 |
|------|------|------|--------|------|----------|
| {{company}} | {{position}} | {{platform}} | {{score}} | {{status}} | {{date}} |
```
