# 浏览器自动化工具说明

本文档说明如何使用 Codex 内置的 browser 插件进行 JD 抓取。

## 可用工具

Codex 的 browser 插件提供以下工具：

### 导航与加载

| 工具 | 说明 | 参数 |
|------|------|------|
| browser_navigate | 打开 URL | url, options? |
| browser_back | 返回上一页 | - |
| browser_forward | 前进一页 | - |
| browser_refresh | 刷新页面 | - |

### 内容提取

| 工具 | 说明 | 参数 |
|------|------|------|
| browser_evaluate | 执行 JavaScript | script |
| browser_screenshot | 截图 | full_page? |
| browser_click | 点击元素 | selector |
| browser_fill | 填写表单 | selector, value |
| browser_select | 选择下拉选项 | selector, value |
| browser_hover | 悬停元素 | selector |
| browser_scroll | 滚动页面 | direction, amount? |

### 等待与检测

| 工具 | 说明 | 参数 |
|------|------|------|
| browser_wait_for | 等待元素出现 | selector, options? |
| browser_disappear | 等待元素消失 | selector |
| browser_is_visible | 检测元素可见性 | selector |

## 抓取模式

### 模式 1：官网招聘页抓取

```javascript
// 示例：抓取公司官网招聘页
async function crawlCompanyCareerPage(companyName) {
  // 1. 搜索官网招聘页
  const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(companyName + " 招聘官网")}`;
  await browser_navigate(searchUrl);

  // 2. 点击官网链接（通常第一个）
  await browser_click('a[href*="careers"], a[href*="jobs"]');

  // 3. 等待页面加载
  await browser_wait_for('body');

  // 4. 提取内容
  const content = await browser_evaluate(() => {
    return document.body.innerText;
  });

  return content;
}
```

### 模式 2：招聘平台 JD 抓取

```javascript
// 示例：抓取 Boss 直聘 JD
async function crawlBossJD(url) {
  await browser_navigate(url);

  // 等待 JD 内容加载
  await browser_wait_for('.job-detail');

  // 提取 JD 内容
  const jd = await browser_evaluate(() => {
    const detail = document.querySelector('.job-detail');
    const title = document.querySelector('.job-title');
    const salary = document.querySelector('.salary');
    const company = document.querySelector('.company-name');

    return {
      title: title?.innerText,
      salary: salary?.innerText,
      company: company?.innerText,
      content: detail?.innerText
    };
  });

  return jd;
}
```

### 模式 3：列表页批量抓取

```javascript
// 示例：抓取职位列表
async function crawlJobList(url, maxPages = 3) {
  const jobs = [];

  for (let page = 1; page <= maxPages; page++) {
    await browser_navigate(`${url}&page=${page}`);
    await browser_wait_for('.job-list');

    const pageJobs = await browser_evaluate(() => {
      return Array.from(document.querySelectorAll('.job-item')).map(item => ({
        title: item.querySelector('.title')?.innerText,
        company: item.querySelector('.company')?.innerText,
        url: item.querySelector('a')?.href
      }));
    });

    jobs.push(...pageJobs);
  }

  return jobs;
}
```

## 常用选择器

### Google 搜索结果
```css
// 搜索结果
.search-result
.result
a[href^="http"]

// 官网标识
a[href*="careers"]
a[href*="jobs"]
.text-bold:contains("官网")
```

### 国内招聘平台

```css
// Boss 直聘
.job-detail
.job-title
.salary
.company-name
.job-info .location
.tags .tag

// 拉勾
.job-detail-container
.position-title
.job-advantage
.company-info

// 猎聘
.job-intro
.job-requirements
.company-info
```

### LinkedIn
```css
// LinkedIn JD
.jobs-details-page
.two-pane-details-page
.jobs-description
.jobs-details-top-card

// 注意：LinkedIn 需要登录，可能无法直接抓取
```

### Indeed
```css
jobsearch-JobComponent
.jobsearch-JobInfoHeader-title
.jobsearch-JobInfoHeader-subtitle
.jobsearch-JobDescriptionText-section
```

## 反爬应对策略

### 策略 1：添加随机延迟

```javascript
function randomDelay(min = 1000, max = 3000) {
  const delay = Math.floor(Math.random() * (max - min + 1)) + min;
  return new Promise(resolve => setTimeout(resolve, delay));
}

// 在操作间添加延迟
await randomDelay();
await browser_click('.next-button');
await randomDelay();
```

### 策略 2：设置随机 User-Agent

```javascript
await browser_navigate(url, {
  headers: {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
  }
});
```

### 策略 3：滚动加载内容处理

```javascript
// 滚动到底部加载更多
async function scrollToLoad() {
  await browser_evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight);
  });
  await browser_wait_for('.loading-spinner', { state: 'hidden' });
}
```

## 异常处理

### 页面加载超时

```javascript
try {
  await browser_wait_for('.job-detail', { timeout: 10000 });
} catch (e) {
  // 超时处理
  return { error: 'page_load_timeout' };
}
```

### 元素不存在

```javascript
const exists = await browser_is_visible(selector);
if (!exists) {
  // 尝试备选选择器
  await browser_wait_for('.job-content');
}
```

### 需要登录

```javascript
const isLoginPage = await browser_evaluate(() => {
  return document.body.innerText.includes('登录') ||
         document.body.innerText.includes('sign in');
});

if (isLoginPage) {
  return { error: 'login_required' };
}
```

## 最佳实践

1. **优先抓取官网**：信息最准确，反爬风险最低
2. **添加随机延迟**：避免被识别为机器人
3. **尊重平台规则**：不强制抓取需要登录的内容
4. **保存原始数据**：抓取后先保存原始文本再解析
5. **记录来源 URL**：方便后续核对
6. **失败时降级**：无法抓取时请求用户提供 JD

## 配置示例

### 浏览器选项

```javascript
// 启动无头模式（可选）
await browser_navigate(url, {
  headless: true,  // 无头模式
  viewport: { width: 1280, height: 720 }
});
```

### 截图配置

```javascript
// 全页截图
await browser_screenshot({ full_page: true });

// 仅视口截图
await browser_screenshot({ full_page: false });
```

## 隐私注意事项

- 不保存登录凭证
- 不记录密码输入
- 不绕过验证码
- 不批量抓取（每次最多 10 个 JD）
- 尊重平台使用条款
