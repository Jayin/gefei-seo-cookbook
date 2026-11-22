import { createMarkdownRenderer, disposeMdItInstance } from 'vitepress'
import { mkdir, readFile, writeFile, copyFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createHash } from 'node:crypto'

const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const docs = path.join(project, 'docs')
const output = path.join(project, 'static')
const corpus = path.resolve(project, '../articles')
const manifest = JSON.parse(await readFile(path.join(corpus, 'reading-order.json'), 'utf8'))
const groups = {
  guide: ['index', 'how-search-engines-work', 'keyword-research', 'on-page-seo', 'technical-seo', 'google-ranking-factors'],
  tools: ['index', 'google-search-console', 'keyword-tools', 'technical-tools', 'google-analytics'],
  advanced: ['index', 'content-seo', 'site-architecture', 'seo-analytics', 'link-building', 'multilingual-seo', 'programmatic-seo', 'ai-seo', 'penalty-recovery'],
  'case-studies': ['index', 'content-site-case', 'tool-site-case']
}
const md = await createMarkdownRenderer(docs)
await mkdir(output, { recursive: true })
let navigation = await readFile(path.join(docs, 'public/learning-path.html'), 'utf8')
navigation = navigation.replace(/  <aside class="local-notice"[\s\S]*?  <\/script>\n/, '')
navigation = navigation.replace('    <footer class="page-footer">', `    <section class="stage"><div class="stage-heading"><h2>延伸阅读 · 哥飞文章</h2><span class="stage-count">${manifest.total} 篇</span></div><p class="stage-intro">按主题和学习进度浏览各目录中的原始文章。</p><a class="footer-link" href="./articles/index.html">打开文章分类索引 →</a></section>\n    <section class="stage"><div class="stage-heading"><h2>项目文档</h2><span class="stage-count">7 篇</span></div><p class="stage-intro">阅读使用说明、项目概况和维护资料。</p><a class="footer-link" href="./project/index.html">打开项目文档 →</a></section>\n    <footer class="page-footer">`)
await writeFile(path.join(output, 'learning-path.html'), navigation)
await writeFile(path.join(output, 'index.html'), navigation)
for (const asset of ['logo.svg', 'favicon.svg']) await copyFile(path.join(docs, 'public', asset), path.join(output, asset))
const all = Object.entries(groups).flatMap(([dir, names]) => names.map(name => `${dir}/${name}`))
const files = new Set(all)
const css = `
:root{color-scheme:light dark;--bg:#f8faf9;--paper:#fff;--text:#19302b;--muted:#52645d;--border:#dce8e1;--accent:#0a7655;--code:#eef3f0}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}a{color:var(--accent)}a:focus-visible{outline:3px solid var(--accent);outline-offset:3px}header{background:var(--paper);border-bottom:1px solid var(--border)}header nav{max-width:980px;margin:auto;padding:16px 24px;display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}header a{font-weight:700;text-decoration:none}main{max-width:860px;margin:36px auto;padding:36px 48px;background:var(--paper);border:1px solid var(--border);border-radius:14px}h1,h2,h3{line-height:1.35;scroll-margin-top:16px}h1{font-size:2rem;margin-top:0}h2{margin-top:2.2em;border-bottom:1px solid var(--border);padding-bottom:.35em}h3{margin-top:1.7em}.header-anchor{text-decoration:none;font-size:.8em}pre{overflow:auto;padding:16px;border-radius:8px;background:#24292e;color:#f5f5f5;line-height:1.5}code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}p code,li code{background:var(--code);padding:.1em .3em;border-radius:4px}table{display:block;overflow:auto;border-collapse:collapse;max-width:100%}th,td{padding:8px 12px;border:1px solid var(--border);text-align:left}blockquote,.custom-block{margin:1.3em 0;padding:12px 18px;border-left:4px solid var(--accent);background:var(--code);border-radius:4px}.custom-block p{margin:.4em 0}.custom-block-title{font-weight:700}.custom-block.warning{border-color:#c88813}img{max-width:100%;height:auto}.pagination{display:flex;justify-content:space-between;gap:20px;margin-top:42px;padding-top:20px;border-top:1px solid var(--border)}@media(max-width:650px){header nav{padding:14px 18px}main{margin:0;padding:26px 18px;border:0;border-radius:0}h1{font-size:1.6rem}.pagination{flex-direction:column}}@media(prefers-color-scheme:dark){:root{--bg:#111c19;--paper:#1b2a25;--text:#ebf4ee;--muted:#afc3b8;--border:#34493e;--accent:#8be5b9;--code:#24382e}}`
await writeFile(path.join(output, 'style.css'), css)
for (const [i, page] of all.entries()) {
  const source = await readFile(path.join(docs, `${page}.md`), 'utf8')
  const title = source.match(/^# (.+)$/m)?.[1] ?? page
  let content = md.render(source, { path: `${page}.md`, relativePath: `${page}.md` })
  // Only rewrite actual root-relative links to known tutorial pages.
  content = content.replace(/href="\/(guide|tools|advanced|case-studies)\/([^"#?]*)([?#][^"]*)?"/g, (original, dir, slug, suffix = '') => {
    const target = `${dir}/${slug.replace(/\.html$/, '') || 'index'}`
    return files.has(target) ? `href="../${target}.html${suffix}"` : original
  })
  const link = (target, label) => `<a href="../${target}.html">${label}</a>`
  const prev = i ? link(all[i - 1], '← 上一篇') : '<span></span>'
  const next = i < all.length - 1 ? link(all[i + 1], '下一篇 →') : '<span></span>'
  const html = `<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title.replaceAll('&', '&amp;').replaceAll('<', '&lt;')} | Google SEO 实战教程</title><link rel="icon" href="../favicon.svg"><link rel="stylesheet" href="../style.css"></head><body><header><nav><a href="../learning-path.html">← 学习路线</a><a href="../learning-path.html#${page.split('/')[0] === 'guide' ? 'basics' : page.split('/')[0] === 'case-studies' ? 'cases' : page.split('/')[0]}">查看本阶段</a></nav></header><main><article>${content}</article><nav class="pagination" aria-label="课程导航">${prev}${next}</nav></main></body></html>\n`
  await mkdir(path.join(output, page.split('/')[0]), { recursive: true })
  await writeFile(path.join(output, `${page}.html`), html)
}
console.log(`Generated learning path and ${all.length} offline lessons in ${output}`)

// Render article HTML examples as text instead of executing the source markup.
disposeMdItInstance()
const articleMd = await createMarkdownRenderer(docs, { html: false })
// Generate offline reading copies of the classified source articles.
const escapeHtml = s => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;')
const articleDir = path.join(output, 'articles')
await mkdir(articleDir, { recursive: true })
const articleId = item => createHash('sha256').update(item.path).digest('hex').slice(0, 20)
let indexSections = ''
for (const category of manifest.categories) {
  let items = ''
  let currentStage = ''
  for (const item of category.articles) {
    const id = articleId(item)
    const text = await readFile(path.join(corpus, item.path), 'utf8')
    const body = articleMd.render(text, { path: item.path, relativePath: item.path })
    const heading = escapeHtml(`${item.number}-${item.title}`)
    const html = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${heading}</title><link rel="stylesheet" href="../style.css"></head><body><header><nav><a href="./index.html#${category.id}">← ${escapeHtml(category.name)}文章索引</a><a href="../learning-path.html">学习路线</a></nav></header><main><article>${body}</article><nav class="pagination" aria-label="文章导航"><a href="./index.html#${category.id}">返回文章分类</a><a href="../learning-path.html">返回学习路线</a></nav></main></body></html>`
    await writeFile(path.join(articleDir, `${id}.html`), html)
    if (item.stage !== currentStage) { if (currentStage) items += '</ul>'; currentStage = item.stage; items += `<h3>${escapeHtml(currentStage)}</h3><ul>` }
    items += `<li><a href="./${id}.html">${heading}</a></li>`
  }
  if (currentStage) items += '</ul>'
  indexSections += `<section id="${category.id}"><h2>${escapeHtml(category.name)}（${category.articles.length} 篇）</h2>${items}</section>`
}
const quickLinks = manifest.categories.map(c => `<a href="#${c.id}">${escapeHtml(c.name)}</a>`).join(' · ')
const articleIndex = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>哥飞文章分类索引</title><link rel="stylesheet" href="../style.css"></head><body><header><nav><a href="../learning-path.html">← 返回学习路线</a></nav></header><main><h1>哥飞文章分类索引</h1><p>共 ${manifest.total} 篇，按各目录的学习顺序排列。原始文章中的观点和时效性请结合 Google 官方文档验证；部分原始文章仅有标题或内容较短。</p><nav aria-label="文章分类">${quickLinks}</nav>${indexSections}</main></body></html>`
await writeFile(path.join(articleDir, 'index.html'), articleIndex)
console.log(`Generated ${manifest.total} offline articles`)

const projectDocs = ['README.md', 'USAGE.md', 'SUMMARY.md', 'DEPLOYMENT.md', 'CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md']
const projectDir = path.join(output, 'project')
await mkdir(projectDir, { recursive: true })
const projectTitles = []
for (const name of projectDocs) {
  const text = await readFile(path.join(project, name), 'utf8')
  const title = text.match(/^# (.+)$/m)?.[1] ?? name
  projectTitles.push({name, title})
  let body = articleMd.render(text, {path: name, relativePath: name})
  body = body.replace(/href="(?:\.\/)?(README|USAGE|SUMMARY|DEPLOYMENT|CONTRIBUTING|SECURITY|CHANGELOG)(?:\.md|\.html)?"/gi, (_, doc) => `href="./${doc.toUpperCase()}.html"`)
  body = body.replace(/href="(?:\.\/)?docs\/(guide|tools|advanced|case-studies)\/([^"#?]*)([?#][^"]*)?"/g, (original, dir, slug, suffix = '') => {
    const target = `${dir}/${slug.replace(/\.(md|html)$/, '') || 'index'}`
    return files.has(target) ? `href="../${target}.html${suffix}"` : original
  })
  body = body.replace(/href="(?:\.\/)?static\/learning-path\.html"/g, 'href="../learning-path.html"')
  body = body.replace(/href="(?:\.\/)?static\/index\.html"/g, 'href="../index.html"')
  body = body.replace(/href="(?:\.\/)?LICENSE(?:\.html)?"/g, 'href="./LICENSE"')
  await writeFile(path.join(projectDir, `${name.replace(/\.md$/, '')}.html`), `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeHtml(title)}</title><link rel="stylesheet" href="../style.css"></head><body><header><nav><a href="./index.html">← 项目文档</a><a href="../learning-path.html">学习路线</a></nav></header><main><article>${body}</article></main></body></html>`)
}
await copyFile(path.join(project, 'LICENSE'), path.join(projectDir, 'LICENSE'))
await writeFile(path.join(projectDir, 'index.html'), `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>项目文档</title><link rel="stylesheet" href="../style.css"></head><body><header><nav><a href="../learning-path.html">← 学习路线</a></nav></header><main><h1>项目文档</h1><ul>${projectTitles.map(({name,title}) => `<li><a href="./${name.replace(/\.md$/, '')}.html">${escapeHtml(title)}</a></li>`).join('')}</ul></main></body></html>`)
console.log(`Generated ${projectDocs.length} project documents`)
