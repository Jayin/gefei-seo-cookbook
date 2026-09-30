# gefei_seo

哥飞公众号文章的个人研究库，以及基于其中 SEO 实战经验整理的教程站点。

原始文章来自公众号「哥飞」（`gefei_offical_article/`，589 篇 `.txt`）。经清洗、分类后存放在 `articles/`，再从中提炼出 `seo-book/` 这本基于 VitePress 的 Google SEO 实战教程。

## 目录结构

```
gefei_seo/
├── gefei_offical_article/   # 原始文章，589 篇单行 .txt（无换行，含公众号格式标记）
├── articles/                # 清洗、分类后的 Markdown，附分类索引 README.md
├── seo-book/                # VitePress 教程站点（Google SEO 实战教程）
├── process_articles.py      # 清洗营销内容并按关键词分类
└── convert_to_markdown.py   # 把单行 .txt 转成带段落的 Markdown
```

## 文章分类

`articles/` 按标题（其次按正文前 500 字）的关键词归类，未命中的默认进 `case-studies`。分类是规则匹配，个别文章会归错类。

| 目录 | 主题 | 篇数 |
| --- | --- | --- |
| `seo-tutorials` | SEO 教程和技巧 | 161 |
| `ai-tools` | AI 工具和产品 | 121 |
| `website-building` | 建站教程 | 89 |
| `monetization` | 变现方式 | 49 |
| `community` | 社群运营 | 40 |
| `product-ops` | 产品运营 | 29 |
| `case-studies` | 案例分析 | 24 |
| `demand-mining` | 需求挖掘 | 17 |
| `overseas-earning` | 出海赚钱经验 | 17 |
| `indie-dev` | 独立开发者故事 | 14 |
| `personal-growth` | 个人成长 | 12 |
| `overseas-infra` | 出海基础设施 | 6 |
| `tools` | 工具推荐 | 2 |
| `industry` | 行业观察 | 1 |
| `policy` | 政策解读 | 0 |

完整篇目见 [`articles/README.md`](articles/README.md)。

## 处理流程

原始 `.txt` 是整篇挤在一行里的文本，开头带「原创 / 在小说阅读器中沉浸阅读」之类的格式标记，末尾常有社群推广。两个脚本分工如下：

1. `process_articles.py`：去掉开头格式标记和末尾营销块，按关键词分类，输出到 `articles/<分类>/`。
2. `convert_to_markdown.py`：按句号、序号、"第 X 步"等切段，生成带标题的 Markdown。

```bash
python3 process_articles.py
python3 convert_to_markdown.py
```

依赖只有 Python 3 标准库，无需安装第三方包。

## SEO 教程站点

`seo-book/` 是一本从入门到进阶的 Google SEO 教程，用 VitePress 构建，目前 24 篇：

- `docs/guide/` — 入门：搜索引擎原理、排名因素、关键词研究、页面 SEO、技术 SEO
- `docs/advanced/` — 进阶：外链、内容 SEO、程序化 SEO、多语言、网站架构、数据分析、AI SEO、惩罚恢复
- `docs/tools/` — 工具：Google Search Console、Google Analytics、关键词工具、技术工具
- `docs/case-studies/` — 案例：内容站、工具站

```bash
cd seo-book
npm install
npm run dev      # 本地预览，默认 http://localhost:5173
npm run build    # 构建
npm run preview  # 预览构建结果
```

需要 Node.js >= 16、npm >= 7。站点自身的说明见 [`seo-book/README.md`](seo-book/README.md)。

## 许可

代码与教程站点采用 [MIT License](LICENSE)。

本许可证只覆盖本仓库中的原创部分：

- `process_articles.py`、`convert_to_markdown.py`
- `seo-book/` 下的站点代码、配置和教程文档

`gefei_offical_article/` 与 `articles/` 中的公众号文章版权归原作者所有，**不在 MIT 授权范围内**，不得再分发或声称获得了再授权。这些文本仅作学习研究引用。
