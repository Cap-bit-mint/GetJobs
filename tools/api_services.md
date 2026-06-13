# API 服务配置

本文档说明 GetJobs Skill 的 API 服务配置方式。

## API 配置原则

### 优先级策略

```
1. 优先使用官方/可信 API
2. 次选第三方招聘 API
3. 降级到浏览器自动化
4. 最后使用用户手动提供
```

### API vs 浏览器对比

| 维度 | API | 浏览器自动化 |
|------|-----|------------|
| 稳定性 | 高 | 中 |
| 数据完整性 | 高 | 中 |
| 维护成本 | 中（API 变更） | 高（UI 变更） |
| 反爬风险 | 低 | 中 |
| 成本 | 可能收费 | 免费 |

## 配置方式

### 方式 1：环境变量

```bash
# .env 文件
BOSS_API_KEY=your_boss_api_key
LAGOU_API_KEY=your_lagou_api_key
LINKEDIN_API_KEY=your_linkedin_api_key
```

### 方式 2：配置文件

```json
// ~/.getjobs/config.json
{
  "api_services": {
    "enabled": true,
    "boss": {
      "enabled": false,
      "api_key": ""
    },
    "lagou": {
      "enabled": false,
      "api_key": ""
    },
    "linkedin": {
      "enabled": false,
      "api_key": ""
    }
  },
  "browser_fallback": {
    "enabled": true,
    "default_delay": 2000
  }
}
```

## 支持的 API 服务

### 国内招聘 API

#### 1. 智联招聘 API

```json
{
  "name": "智联招聘",
  "platform": "zhilian",
  "api_docs": "https://open.zhaopin.com/",
  "pricing": "企业认证后免费",
  "data_coverage": ["职位搜索", "JD详情", "公司信息"],
  "rate_limit": "100次/分钟"
}
```

#### 2. 前程无忧 API

```json
{
  "name": "前程无忧",
  "platform": "51job",
  "api_docs": "https://www.51job.com/",
  "pricing": "付费",
  "data_coverage": ["职位搜索", "JD详情"],
  "rate_limit": "企业用户限定"
}
```

#### 3. BOSS 直聘（无官方 API）

```json
{
  "name": "BOSS直聘",
  "platform": "boss",
  "api_docs": "无公开API",
  "recommendation": "使用 browser 插件或用户手动提供"
}
```

#### 4. 拉勾招聘（无公开 API）

```json
{
  "name": "拉勾招聘",
  "platform": "lagou",
  "api_docs": "无公开API",
  "recommendation": "使用 browser 插件或用户手动提供"
}
```

### 海外招聘 API

#### 1. LinkedIn API

```json
{
  "name": "LinkedIn",
  "platform": "linkedin",
  "api_docs": "https://learn.microsoft.com/en-us/linkedin/",
  "pricing": "需要合作伙伴资质",
  "data_coverage": ["职位列表", "公司信息", "个人资料"],
  "access_level": "受限，需企业账号"
}
```

#### 2. Indeed API

```json
{
  "name": "Indeed",
  "platform": "indeed",
  "api_docs": "https://www.indeed.com/publisher",
  "pricing": "免费（有限制）",
  "data_coverage": ["职位搜索", "JD摘要"],
  "rate_limit": "有限制",
  "note": "Publisher API 需要网站绑定"
}
```

#### 3. Glassdoor API

```json
{
  "name": "Glassdoor",
  "platform": "glassdoor",
  "api_docs": "https://www.glassdoor.com/developer/index.htm",
  "pricing": "企业付费",
  "data_coverage": ["公司评价", "薪资数据", "职位列表"]
}
```

#### 4. RemoteOK API

```json
{
  "name": "RemoteOK",
  "platform": "remoteok",
  "api_docs": "https://remoteok.com/api",
  "pricing": "免费",
  "data_coverage": ["远程职位列表"],
  "rate_limit": "无明确限制"
}
```

#### 5. JSearch API (RapidAPI)

```json
{
  "name": "JSearch",
  "platform": "rapidapi",
  "api_docs": "https://rapidapi.com/SabaStarnavi/api/jsearch",
  "pricing": "免费额度后付费",
  "data_coverage": ["跨平台职位搜索"],
  "supported_platforms": ["LinkedIn", "Indeed", "Glassdoor"]
}
```

## API 使用示例

### Indeed Publisher API

```javascript
// Indeed Publisher API 调用示例
async function searchIndeedJobs(query, location) {
  const baseUrl = 'https://api.indeed.com/ads/apisearch';
  const params = new URLSearchParams({
    publisher: YOUR_PUBLISHER_ID,
    format: 'json',
    l: location,
    q: query,
    v: '2'
  });

  const response = await fetch(`${baseUrl}?${params}`);
  const data = await response.json();

  return data.results.map(job => ({
    title: job.jobtitle,
    company: job.company,
    location: job.formattedLocation,
    snippet: job.snippet,
    url: job.url,
    postedDate: job.date
  }));
}
```

### RemoteOK API

```javascript
// RemoteOK API 调用示例
async function searchRemoteOKJobs(keyword) {
  const response = await fetch('https://remoteok.com/api', {
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const data = await response.json();

  return data
    .filter(job => !job.tags?.includes('no_remote'))
    .filter(job => !keyword || job.position.toLowerCase().includes(keyword.toLowerCase()))
    .map(job => ({
      title: job.position,
      company: job.company,
      location: job.location || 'Remote',
      salary: job.salary || 'Not specified',
      tags: job.tags,
      url: job.url,
      postedAt: new Date(job.date * 1000).toISOString()
    }));
}
```

## 降级策略

当 API 不可用时，自动降级到浏览器自动化：

```javascript
async function getJobs(query, options = {}) {
  // 1. 尝试 API
  if (apiEnabled && !options.forceBrowser) {
    try {
      const results = await searchAPI(query);
      if (results.length > 0) return results;
    } catch (e) {
      console.log('API failed, falling back to browser');
    }
  }

  // 2. 降级到浏览器
  return await browserCrawl(query);
}
```

## 配置检查清单

- [ ] 已配置至少一个 API 服务
- [ ] API 密钥已正确设置
- [ ] 已测试 API 连通性
- [ ] 已在 Skill 初始化时检测配置

## 错误处理

### API 限流

```json
{
  "error": "rate_limit_exceeded",
  "message": "API 请求频率超限",
  "suggestion": "启用浏览器降级模式或等待重试",
  "retry_after": 60
}
```

### API 认证失败

```json
{
  "error": "auth_failed",
  "message": "API 密钥无效或已过期",
  "suggestion": "检查配置文件中的 API 密钥"
}
```

### API 服务不可用

```json
{
  "error": "service_unavailable",
  "message": "API 服务暂时不可用",
  "suggestion": "降级到浏览器自动化模式"
}
```
