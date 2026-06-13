# PDF 解析工具说明

本文档说明如何使用 Codex 内置工具解析 PDF 文件。

## 适用场景

- 用户上传 PDF 格式的简历
- 用户上传 PDF 格式的 JD
- 需要从 PDF 中提取文本内容进行分析

## 可用方法

### 方法 1：Node.js pdf-parse（推荐）

使用 `mcp__node_repl__js` 工具执行：

```javascript
const fs = require('fs');
const pdfParse = require('pdf-parse');

async function parsePDF(filePath) {
  const dataBuffer = fs.readFileSync(filePath);
  const data = await pdfParse(dataBuffer);
  return {
    text: data.text,
    pages: data.numpages,
    info: data.info
  };
}

// 执行
const result = await parsePDF('/path/to/resume.pdf');
console.log(result.text);
```

### 方法 2：macOS 本地工具

```bash
# 使用 pdftotext（需安装 poppler）
pdftotext input.pdf output.txt

# 使用 textutil（系统自带）
textutil -convert txt -stdout input.pdf
```

### 方法 3：OCR（扫描 PDF）

如 PDF 是扫描件，需使用 OCR：

```javascript
// 使用 tesseract.js
const Tesseract = require('tesseract.js');

async function ocrPDF(imagePath) {
  const { data: { text } } = await Tesseract.recognize(imagePath);
  return text;
}
```

## 执行流程

### 步骤 1：检测文件类型

```javascript
function isPDF(filePath) {
  return filePath.toLowerCase().endsWith('.pdf');
}
```

### 步骤 2：解析 PDF

```javascript
async function extractPDFContent(filePath) {
  try {
    // 尝试文本提取
    const result = await parsePDF(filePath);
    return {
      success: true,
      text: result.text,
      pages: result.pages
    };
  } catch (e) {
    return {
      success: false,
      error: e.message
    };
  }
}
```

### 步骤 3：验证提取结果

```javascript
function validateExtractedText(text) {
  // 检查是否提取到有效内容
  if (!text || text.length < 50) {
    return { valid: false, reason: '内容过少或为空' };
  }
  
  // 检查是否为乱码
  const chineseRatio = (text.match(/[\u4e00-\u9fa5]/g) || []).length / text.length;
  if (chineseRatio < 0.1 && text.length > 500) {
    return { valid: false, reason: '可能提取失败，请尝试截图' };
  }
  
  return { valid: true };
}
```

## 完整示例

```javascript
// 用户输入：/Users/jelly/Downloads/resume.pdf

async function processResume(filePath) {
  // 1. 验证文件存在
  const fs = require('fs');
  if (!fs.existsSync(filePath)) {
    return { error: '文件不存在，请检查路径' };
  }
  
  // 2. 解析 PDF
  const pdfParse = require('pdf-parse');
  const dataBuffer = fs.readFileSync(filePath);
  const data = await pdfParse(dataBuffer);
  
  // 3. 验证内容
  if (data.text.length < 50) {
    return { error: 'PDF 内容为空或无法读取' };
  }
  
  return {
    text: data.text,
    pages: data.numpages,
    meta: data.info
  };
}
```

## 异常处理

### 文件不存在

```javascript
{
  error: '文件不存在',
  suggestion: '请检查文件路径是否正确，或直接粘贴 PDF 内容'
}
```

### PDF 加密/损坏

```javascript
{
  error: '无法解析 PDF',
  suggestion: 'PDF 可能已加密或损坏，请尝试：1) 提供文本版本 2) 上传截图'
}
```

### 扫描件（无文字层）

```javascript
{
  error: 'PDF 无文字层（扫描件）',
  suggestion: '请提供：1) 带文字的 PDF 2) 截图 3) 直接复制内容'
}
```

## 最佳实践

1. **优先文本提取**：先尝试 PDF 解析，失败再请求截图
2. **验证内容质量**：检查提取文本的长度和可读性
3. **处理编码问题**：部分 PDF 中文编码可能有问题
4. **尊重用户选择**：如用户坚持提供文本，优先使用

## 相关工具

- [browser_automation.md](browser_automation.md) - 浏览器自动化
- [api_services.md](api_services.md) - API 服务配置
