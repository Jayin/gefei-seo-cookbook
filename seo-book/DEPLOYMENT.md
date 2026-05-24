# 部署指南

本指南介绍如何部署 Google SEO 实战教程网站。

## 本地开发

### 启动开发服务器

```bash
cd seo-book
npm install
npm run dev
```

访问 http://localhost:5173 查看效果。

### 构建生产版本

```bash
npm run build
```

构建完成后，静态文件会生成在 `docs/.vitepress/dist/` 目录。

### 预览生产版本

```bash
npm run preview
```

访问 http://localhost:4173 预览生产版本。

## 部署选项

### 1. GitHub Pages

#### 步骤 1：创建 GitHub 仓库

1. 在 GitHub 上创建新仓库
2. 将代码推送到仓库

#### 步骤 2：配置 GitHub Actions

创建 `.github/workflows/deploy.yml` 文件：

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm install

      - name: Build
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

#### 步骤 3：配置 GitHub Pages

1. 进入仓库设置
2. 找到 "Pages" 选项
3. 选择 "Deploy from a branch"
4. 选择 "gh-pages" 分支
5. 保存设置

### 2. Vercel

#### 步骤 1：连接仓库

1. 登录 Vercel
2. 点击 "New Project"
3. 连接 GitHub 仓库

#### 步骤 2：配置项目

- **Framework Preset:** VitePress
- **Build Command:** `npm run build`
- **Output Directory:** `docs/.vitepress/dist`
- **Install Command:** `npm install`

#### 步骤 3：部署

点击 "Deploy" 按钮完成部署。

### 3. Netlify

#### 步骤 1：连接仓库

1. 登录 Netlify
2. 点击 "New site from Git"
3. 连接 GitHub 仓库

#### 步骤 2：配置项目

- **Build command:** `npm run build`
- **Publish directory:** `docs/.vitepress/dist`

#### 步骤 3：部署

点击 "Deploy site" 按钮完成部署。

### 4. 静态文件托管

#### 步骤 1：构建项目

```bash
npm run build
```

#### 步骤 2：上传文件

将 `docs/.vitepress/dist/` 目录中的所有文件上传到你的静态文件托管服务。

常见的静态文件托管服务：
- AWS S3
- Google Cloud Storage
- Azure Blob Storage
- 阿里云 OSS
- 腾讯云 COS

### 5. 自托管

#### 步骤 1：构建项目

```bash
npm run build
```

#### 步骤 2：配置 Web 服务器

**Nginx 配置示例：**

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/seo-book/docs/.vitepress/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

**Apache 配置示例：**

```apache
<VirtualHost *:80>
    ServerName your-domain.com
    DocumentRoot /path/to/seo-book/docs/.vitepress/dist

    <Directory /path/to/seo-book/docs/.vitepress/dist>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

## 自定义域名

### GitHub Pages

1. 在仓库根目录创建 `CNAME` 文件
2. 在文件中写入你的域名
3. 在域名 DNS 设置中添加 CNAME 记录

### Vercel

1. 进入项目设置
2. 找到 "Domains" 选项
3. 添加你的域名
4. 按照提示配置 DNS

### Netlify

1. 进入站点设置
2. 找到 "Domain management" 选项
3. 添加你的域名
4. 按照提示配置 DNS

## 环境变量

如果需要配置环境变量，可以在项目根目录创建 `.env` 文件：

```env
# 网站标题
VITE_TITLE=Google SEO 实战教程

# 网站描述
VITE_DESCRIPTION=从零开始学习 Google SEO 优化

# 网站 URL
VITE_SITE_URL=https://your-domain.com
```

## 性能优化

### 1. 启用 Gzip 压缩

在 Web 服务器配置中启用 Gzip 压缩。

### 2. 配置缓存

为静态资源配置长期缓存。

### 3. 使用 CDN

使用 CDN 加速静态资源加载。

### 4. 优化图片

压缩图片，使用 WebP 格式。

## 监控和分析

### 1. Google Analytics

在 `docs/.vitepress/config.mts` 中添加 Google Analytics 代码：

```typescript
head: [
  ['script', { async: true, src: 'https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID' }],
  ['script', {}, `
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_MEASUREMENT_ID');
  `]
]
```

### 2. Google Search Console

1. 验证网站所有权
2. 提交 Sitemap
3. 监控索引状态

## 常见问题

### Q: 部署后页面空白怎么办？

A: 检查 `base` 配置是否正确。如果部署在子目录，需要设置 `base`。

### Q: 如何配置 base？

A: 在 `docs/.vitepress/config.mts` 中添加：

```typescript
export default defineConfig({
  base: '/seo-book/',  // 如果部署在子目录
  // ...
})
```

### Q: 如何添加自定义样式？

A: 在 `docs/.vitepress/theme/` 目录创建自定义主题。

### Q: 如何添加自定义组件？

A: 在 `docs/.vitepress/theme/` 目录注册自定义组件。

## 更新和维护

### 更新内容

1. 修改 `docs/` 目录中的 Markdown 文件
2. 提交代码到仓库
3. 自动部署会更新网站

### 更新依赖

```bash
npm update
```

### 备份

定期备份 `docs/` 目录和配置文件。

## 技术支持

如有问题，请：

1. 查看 VitePress 官方文档
2. 搜索相关问题
3. 提交 Issue

---

**祝部署顺利！**