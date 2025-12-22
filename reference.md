# 参考文档

## Simon Willison's HTML Tools

本文档记录了从 Simon Willison 的博客文章中学到的设计理念和最佳实践。

### 参考链接

- [Useful patterns for building HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/)
- [tools.simonwillison.net](https://tools.simonwillison.net/) - Simon 的工具集合展示

### 核心设计原则

#### 1. 单文件 HTML
- 将 HTML、CSS 和 JavaScript 都写在一个文件中
- 方便复制粘贴和部署
- 无需构建步骤

#### 2. 避免 React
- React 的 JSX 需要构建步骤，增加复杂性
- 使用纯 JavaScript 或从 CDN 加载轻量级框架
- 更快的渲染和更少的 Bug

#### 3. CDN 依赖
- 使用 cdnjs 或 jsDelivr 加载第三方库
- 优先选择知名库
- 使用带版本号的 URL 确保稳定性

#### 4. 保持精简
- 每个工具控制在几百行代码
- 便于 LLM 理解和修改
- 易于维护和重新编写

### 功能模式

#### 剪贴板操作
- 支持粘贴内容（文本、富文本、图片、文件）
- 一键复制结果到剪贴板
- 利用剪贴板的多格式支持

#### URL 状态持久化
- 将状态保存在 URL 中
- 方便书签和分享
- 无需服务器存储

#### localStorage 存储
- 用于存储较大的状态或敏感信息（如 API 密钥）
- 数据不离开用户设备
- 适合自动保存功能

#### CORS API 调用
- 利用支持 CORS 的公开 API
- 常用的 CORS API：
  - GitHub (公开仓库)
  - iNaturalist (物种观察)
  - PyPI (Python 包)
  - Bluesky (社交媒体)
  - Mastodon

#### 文件处理
- 使用 `<input type="file">` 直接读取文件
- 无需上传到服务器
- 支持 PDF.js、Tesseract.js 等浏览器内处理库

#### 文件下载
- 使用 JavaScript 生成可下载文件
- 支持多种格式（PNG、JPEG、ICS 等）

#### Pyodide 和 WebAssembly
- Pyodide: 在浏览器中运行 Python
- WebAssembly: 运行其他语言编译的代码
- 拓展浏览器的能力边界

### 工具开发流程

#### 1. 使用 Artifacts/Canvas 原型
- 在 Claude、ChatGPT 或 Gemini 中快速原型
- 使用提示词: "Build an artifact/canvas that [需求]. No React."
- 获得可分享的 URL

#### 2. 切换到编码代理
- 对于复杂项目，使用 Claude Code 或 Codex CLI
- 可以使用 Playwright 进行测试
- 直接提交到 GitHub 仓库

#### 3. 自托管
- 部署到 GitHub Pages
- 避免 LLM 平台的沙箱限制
- 更稳定可靠

### 工具示例

#### 调试工具
- `clipboard-viewer` - 查看剪贴板的所有格式
- `keyboard-debug` - 显示当前按下的键
- `cors-fetch` - 测试 URL 是否支持 CORS
- `exif` - 显示照片的 EXIF 数据

#### 转换工具
- `json-to-yaml` - JSON 转 YAML
- `svg-render` - SVG 渲染为 PNG/JPEG
- `terminal-to-html` - 终端输出转 HTML

#### API 工具
- `github-issue-to-markdown` - GitHub Issue 转 Markdown
- `bluesky-thread` - Bluesky 讨论串查看
- `pypi-changelog` - PyPI 包版本差异

### 提示词模板

```
Build an artifact that [描述功能需求].
No React.
Use [特定库名] from CDN if needed.
Include [特定功能要求].
```

### 记录和分享

- 保存 LLM 对话记录
- 在 commit message 中包含提示词链接
- 工具页脚添加 "View source" 链接

---

## 本项目的实现

基于以上原则，JustHTMLs 实现了：

1. **标准化目录结构** - 每个工具独立文件夹，包含 index.html 和 app.html
2. **索引系统** - 使用 index.json 管理工具元数据
3. **搜索和过滤** - 前端实现的多维度搜索
4. **提交流程** - 通过 GitHub Issues 提交工具
5. **GitHub Pages 部署** - 静态托管，无服务器成本
