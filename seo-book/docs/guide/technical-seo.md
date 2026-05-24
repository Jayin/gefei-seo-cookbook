# 技术 SEO 基础

技术 SEO 是确保搜索引擎能够正确抓取、索引和理解网站的技术架构。良好的技术 SEO 是获得排名的基础。

## 一、网站可访问性

### 1. robots.txt

robots.txt 文件告诉搜索引擎哪些页面可以抓取，哪些不可以。

**基本格式：**
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Disallow: /temp/

Sitemap: https://example.com/sitemap.xml
```

**最佳实践：**
- 不要阻止重要页面
- 定期检查是否有误阻止
- 在 Google Search Console 测试
- 指向 Sitemap 位置

### 2. Sitemap

Sitemap 是一个 XML 文件，列出网站的所有重要页面。

**基本格式：**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/page1</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

**最佳实践：**
- 只包含规范页面
- 及时更新 lastmod
- 提交到 Google Search Console
- 保持文件大小合理

### 3. 网站架构

**理想的网站结构：**
```
首页
├── 分类页面 1
│   ├── 内容页面 1
│   ├── 内容页面 2
│   └── 内容页面 3
├── 分类页面 2
│   ├── 内容页面 4
│   └── 内容页面 5
└── 分类页面 3
    └── 内容页面 6
```

**最佳实践：**
- 页面深度不超过 3 层
- 使用清晰的层级结构
- 合理的内部链接
- 面包屑导航

## 二、页面渲染

### 1. 服务端渲染（SSR）

服务端渲染是指在服务器上生成完整的 HTML，然后发送给浏览器。

**优点：**
- 搜索引擎可以直接抓取内容
- 首屏加载速度快
- 有利于 SEO

**实现方式：**
- Next.js（React）
- Nuxt.js（Vue）
- 传统后端渲染

### 2. 客户端渲染（CSR）

客户端渲染是指浏览器下载 JavaScript 后，由 JavaScript 生成页面内容。

**缺点：**
- 搜索引擎可能无法抓取内容
- 首屏加载慢
- 不利于 SEO

**避免使用：**
- 纯 JavaScript 渲染
- 单页应用（SPA）不做 SSR

::: warning 重要
不要使用前端渲染！Google 虽然可以执行 JavaScript，但会消耗额外资源，不会为小网站这样做。
:::

### 3. 预渲染

预渲染是指提前生成静态 HTML 文件。

**工具：**
- Prerender.io
- Puppeteer
- 静态站点生成器

## 三、HTTPS

### 1. 为什么需要 HTTPS？

- HTTPS 是排名因素
- 保护用户数据
- 提升用户信任
- 避免浏览器警告

### 2. 如何启用 HTTPS？

1. 获取 SSL 证书（免费：Let's Encrypt）
2. 安装证书
3. 配置服务器
4. 重定向 HTTP 到 HTTPS
5. 更新内部链接

### 3. 常见问题

**混合内容：**
- 页面同时加载 HTTP 和 HTTPS 资源
- 浏览器会显示警告
- 需要修复所有 HTTP 资源

**重定向链：**
- HTTP → HTTPS → www → 非 www
- 应该直接跳转到最终地址

## 四、页面速度

### 1. 为什么页面速度重要？

- 是排名因素
- 影响用户体验
- 影响转化率
- 影响爬虫效率

### 2. 测量工具

**Google PageSpeed Insights：**
- https://pagespeed.web.dev/

**Core Web Vitals：**
- LCP（最大内容绘制）
- FID（首次输入延迟）
- CLS（累积布局偏移）

### 3. 优化方法

**图片优化：**
- 压缩图片
- 使用 WebP 格式
- 使用懒加载
- 设置合适的尺寸

**代码优化：**
- 压缩 CSS 和 JavaScript
- 合并文件
- 移除未使用的代码
- 使用异步加载

**服务器优化：**
- 使用 CDN
- 启用缓存
- 启用 Gzip 压缩
- 选择好的主机

**字体优化：**
- 使用系统字体
- 预加载字体
- 使用 font-display: swap

## 五、移动端优化

### 1. 移动优先索引

Google 使用移动版本的内容进行索引和排名。

**检查方法：**
- 使用 Google 移动设备适合性测试
- 确保移动版内容完整
- 确保移动版功能正常

### 2. 响应式设计

**优点：**
- 一个 URL
- 维护简单
- Google 推荐

**实现：**
- 使用媒体查询
- 灵活的布局
- 灵活的图片

### 3. 移动端体验

**检查要点：**
- 文字可读，无需缩放
- 按钮大小适合点击（44x44 像素）
- 避免水平滚动
- 加载速度快

## 六、结构化数据

### 1. 什么是结构化数据？

结构化数据是帮助搜索引擎理解页面内容的标准化格式。

### 2. Schema.org

Schema.org 是最常用的结构化数据词汇表。

**常见类型：**
- Article（文章）
- Product（产品）
- Review（评论）
- FAQ（常见问题）
- HowTo（操作指南）

### 3. 实现方式

**JSON-LD（推荐）：**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Google SEO 入门教程",
  "author": {
    "@type": "Person",
    "name": "SEO Book"
  },
  "datePublished": "2024-01-01"
}
</script>
```

**Microdata：**
```html
<div itemscope itemtype="https://schema.org/Article">
  <h1 itemprop="headline">Google SEO 入门教程</h1>
</div>
```

### 4. 测试工具

- Google 结构化数据测试工具
- Google 富媒体搜索结果测试

## 七、Canonical 标签

### 1. 什么是 Canonical 标签？

Canonical 标签告诉搜索引擎哪个 URL 是页面的规范版本。

### 2. 使用场景

- 同一内容多个 URL
- HTTP 和 HTTPS 版本
- www 和非 www 版本
- 带参数和不带参数的 URL

### 3. 实现方式

```html
<link rel="canonical" href="https://example.com/page">
```

### 4. 最佳实践

- 指向自己也是可以的
- 使用绝对 URL
- 确保规范页面可访问
- 不要指向不同的内容

## 八、Hreflang 标签

### 1. 什么是 Hreflang 标签？

Hreflang 标签告诉搜索引擎页面的语言和地区版本。

### 2. 使用场景

- 多语言网站
- 不同地区版本
- 相同语言不同地区

### 3. 实现方式

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/">
<link rel="alternate" hreflang="zh" href="https://example.com/zh/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">
```

### 4. 最佳实践

- 每个版本都指向所有版本
- 包含 x-default
- 使用正确的语言代码
- 使用绝对 URL

## 九、常见技术 SEO 问题

### 1. 页面未被索引

**检查：**
- robots.txt 是否阻止
- 是否有 noindex 标签
- 页面是否可访问
- 是否有 canonical 标签

### 2. 抓取错误

**检查：**
- 服务器错误（5xx）
- 404 错误
- 重定向问题
- 软 404

### 3. 重复内容

**解决：**
- 使用 canonical 标签
- 301 重定向
- 使用 noindex
- 合并内容

### 4. 页面速度慢

**检查：**
- 图片是否过大
- 代码是否压缩
- 服务器响应慢
- 第三方脚本

## 十、技术 SEO 检查清单

### 基础检查
- [ ] 网站可访问
- [ ] robots.txt 正确
- [ ] Sitemap 已提交
- [ ] HTTPS 已启用

### 页面检查
- [ ] 页面可被索引
- [ ] 没有 noindex 标签
- [ ] canonical 标签正确
- [ ] 页面速度正常

### 移动端检查
- [ ] 移动设备适合
- [ ] 响应式设计
- [ ] 内容完整
- [ ] 功能正常

### 结构检查
- [ ] 清晰的层级结构
- [ ] 合理的内部链接
- [ ] 面包屑导航
- [ ] 页面深度合理

::: tip 关键要点
技术 SEO 是基础，确保搜索引擎能够正常抓取和索引你的网站。在此基础上，再进行内容优化和外链建设。
:::