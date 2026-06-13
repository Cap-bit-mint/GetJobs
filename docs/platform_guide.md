# 各平台使用指南

本文档说明 GetJobs Skill 在各招聘平台上的使用方法。

## 国内平台

### Boss 直聘

**特点**
- 国内头部招聘平台
- JD 信息较完整
- 薪资信息通常透明

**抓取方式**
- 优先：用户直接提供 JD 链接或文本
- 降级：browser 插件抓取

**JD 链接格式**
```
https://www.zhipin.com/job_detail/xxx.html
```

**JD 选择器**
```css
.job-detail          // JD 主体内容
.job-title          // 岗位名称
.salary             // 薪资
.company-name       // 公司名
.job-location .location-name  // 地点
.job-tags .tag      // 标签
.optional-section   // 加分项
```

**注意事项**
- 部分 JD 需要登录才能查看
- 反爬机制较严格，建议添加延迟
- 批量抓取可能被封禁

**最佳实践**
1. 让用户直接提供 Boss JD 链接
2. 若需抓取，添加 2-3 秒随机延迟
3. 每次最多抓取 5 个 JD

---

### 拉勾招聘

**特点**
- 互联网岗位较多
- JD 结构化程度高
- 公司评价信息丰富

**抓取方式**
- 优先：用户直接提供
- 降级：browser 插件

**JD 链接格式**
```
https://www.lagou.com/jobs/xxx.html
```

**JD 选择器**
```css
.job-detail-container     // 容器
.position-title          // 岗位名
.job-advantage           // 岗位优势
.company-info            // 公司信息
.job-intro              // JD 主体
.position-label          // 标签
```

**注意事项**
- 需要登录才能查看完整 JD
- 反爬机制较完善
- 建议直接请求用户提供 JD

---

### 猎聘

**特点**
- 中高端职位较多
- JD 通常包含详细职责
- 猎头职位居多

**抓取方式**
- 优先：用户直接提供
- 降级：browser 插件

**JD 选择器**
```css
.job-intro              // JD 主体
.job-requirements       // 要求
.company-info           // 公司信息
.benefits              // 福利
```

---

### 智联招聘

**特点**
- 职位数量多
- 行业覆盖广
- 有官方 API（需企业认证）

**抓取方式**
- 推荐：官方 API（若企业认证）
- 降级：browser 插件

**API 配置**
```json
{
  "platform": "zhilian",
  "base_url": "https://fe-api.zhaopin.com/c/i/sou",
  "params": {
    "cityId": "城市代码",
    "kw": "关键词"
  }
}
```

---

### 前程无忧 (51job)

**特点**
- 综合类招聘平台
- 职位数量庞大
- 传统行业岗位多

**抓取方式**
- browser 插件
- 用户直接提供

**JD 选择器**
```css
.job_msg              // JD 主体
.tCompany_main       // 公司信息
.emWarning           // 注意事项
```

---

### 公司官网招聘页

**最高优先级**
- 信息最准确
- 更新最快
- 反爬风险最低

**常见 URL 格式**
```
https://careers.company.com
https://jobs.company.com
https://www.company.com/careers
https://www.company.com/about/careers
https://hire.company.com
```

**搜索策略**
1. `公司名 + 招聘官网`
2. `公司名 + careers`
3. `公司名 + jobs`

**示例**
| 公司 | 招聘页 URL |
|------|-----------|
| 字节跳动 | jobs.bytedance.com |
| 腾讯 | careers.tencent.com |
| 阿里巴巴 | career.alibaba.com |
| 美团 | campus.meituan.com |
| 京东 | careers.jd.com |
| 百度 | talent.baidu.com |

---

## 海外平台

### LinkedIn

**特点**
- 全球最大职业社交平台
- 职位信息丰富
- 需要注意隐私

**抓取限制**
- API 需要合作伙伴资质
- 浏览器抓取可能违反 ToS
- 建议直接请求用户提供 JD

**JD 选择器（需登录）**
```css
.jobs-details-page    // 页面容器
.jobs-description    // JD 主体
.two-pane-details    // 详情面板
```

**注意事项**
- 尊重 LinkedIn 隐私政策
- 不批量抓取会员信息
- 建议使用用户提供的 JD

---

### Indeed

**特点**
- 全球职位聚合
- API 可用（需 Publisher 账号）
- 职位数量庞大

**API 调用**
```javascript
// Indeed Publisher API
const baseUrl = 'https://api.indeed.com/ads/apisearch';
```

**JD 选择器**
```css
jobsearch-JobComponent   // JD 容器
.jobsearch-JobInfoHeader-title    // 岗位名
.jobsearch-JobInfoHeader-subtitle // 公司+地点
.jobsearch-JobDescriptionText     // JD 主体
```

**配置**
```json
{
  "platform": "indeed",
  "publisher_id": "YOUR_PUBLISHER_ID",
  "api_available": true
}
```

---

### Glassdoor

**特点**
- 公司评价丰富
- 薪资数据参考价值高
- JD 通常从其他平台聚合

**抓取方式**
- browser 插件
- 用户直接提供

**JD 选择器**
```css
.css-1etFOyp          // JD 主体
.css-q9z1g7          // 岗位信息
```

**注意事项**
- 部分内容需要登录
- API 需要企业账号

---

### RemoteOK

**特点**
- 专注远程工作
- 有免费公开 API
- JSON 格式数据

**API 端点**
```
https://remoteok.com/api
```

**API 返回格式**
```json
[
  {
    "id": "xxx",
    "position": "岗位名",
    "company": "公司名",
    "location": "Remote",
    "salary": "$100k - $150k",
    "tags": ["tag1", "tag2"],
    "url": "https://remoteok.com/xxx",
    "date": 1234567890
  }
]
```

**使用示例**
```javascript
const response = await fetch('https://remoteok.com/api');
const jobs = await response.json();
```

---

### AngelList / Wellfound

**特点**
- 初创公司职位
- 强调文化契合
- 包含公司估值/融资信息

**抓取方式**
- browser 插件
- 用户直接提供

**URL 格式**
```
https://wellfound.com/jobs/xxx
```

---

## 抓取策略总结

### 优先级排序

| 优先级 | 来源 | 理由 |
|--------|------|------|
| 1 | 官网招聘页 | 最准确、最可靠 |
| 2 | API 服务 | 稳定、结构化 |
| 3 | 用户提供 | 完全准确 |
| 4 | Browser 抓取 | 可能不完整 |

### 降级路径

```
用户请求 JD
    ↓
检查是否有 API 配置
    ↓ 是 → 使用 API
    ↓ 否 → 检查官网
           ↓ 是官网 → 抓取官网
           ↓ 无官网 → Browser 抓取招聘平台
                       ↓ 失败 → 请求用户提供
```

### 平台选择建议

| 用户需求 | 推荐平台 |
|----------|----------|
| 互联网/科技岗位 | 官网、拉勾、Boss |
| 传统行业 | 智联、前程无忧 |
| 中高端职位 | 猎聘 |
| 海外职位 | LinkedIn、Indeed |
| 远程工作 | RemoteOK |
| 初创公司 | Wellfound、LinkedIn |

---

## 反爬注意事项

### 国内平台
- Boss 直聘：严格，建议添加延迟或直接请求用户提供
- 拉勾：严格，建议直接请求用户提供
- 猎聘：中等
- 智联：有官方 API，推荐使用

### 海外平台
- LinkedIn：严格，不建议强制抓取
- Indeed：有 Publisher API，推荐使用
- Glassdoor：中等
- RemoteOK：宽松，有公开 API

---

## 合规使用建议

1. **优先官方渠道**：优先使用 API 或官网
2. **尊重平台规则**：遵守 robots.txt 和 ToS
3. **限制抓取频率**：避免批量抓取
4. **保护用户隐私**：不保存登录凭证
5. **降级策略**：优先请求用户提供 JD
