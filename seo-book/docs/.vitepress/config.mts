import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Google SEO 实战教程",
  description: "从零开始学习 Google SEO 优化",
  lang: 'zh-CN',
  head: [
    ['link', { rel: 'icon', href: '/favicon.svg' }]
  ],
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: '首页', link: '/' },
      { text: '学习路线', link: '/learning-path.html', target: '_self' },
      { text: '入门指南', link: '/guide/' },
      { text: '工具推荐', link: '/tools/' },
      { text: '进阶技巧', link: '/advanced/' },
      { text: '案例分析', link: '/case-studies/' }
    ],
    sidebar: {
      '/guide/': [
        {
          text: '入门指南',
          items: [
            { text: '01-什么是 SEO？', link: '/guide/' },
            { text: '02-搜索引擎工作原理', link: '/guide/how-search-engines-work' },
            { text: '03-关键词研究基础', link: '/guide/keyword-research' },
            { text: '04-页面 SEO 优化', link: '/guide/on-page-seo' },
            { text: '05-技术 SEO 基础', link: '/guide/technical-seo' },
            { text: '06-Google 排名因素', link: '/guide/google-ranking-factors' }
          ]
        }
      ],
      '/advanced/': [
        {
          text: '进阶技巧',
          items: [
            { text: '01-进阶技巧', link: '/advanced/' },
            { text: '02-内容 SEO 策略', link: '/advanced/content-seo' },
            { text: '03-网站架构优化', link: '/advanced/site-architecture' },
            { text: '04-SEO 数据分析', link: '/advanced/seo-analytics' },
            { text: '05-外链建设策略', link: '/advanced/link-building' },
            { text: '06-多语言 SEO', link: '/advanced/multilingual-seo' },
            { text: '07-程序化 SEO', link: '/advanced/programmatic-seo' },
            { text: '08-AI 搜索优化', link: '/advanced/ai-seo' },
            { text: '09-惩罚恢复指南', link: '/advanced/penalty-recovery' }
          ]
        }
      ],
      '/tools/': [
        {
          text: '工具推荐',
          items: [
            { text: '01-SEO 工具概览', link: '/tools/' },
            { text: '02-Google Search Console', link: '/tools/google-search-console' },
            { text: '03-关键词研究工具', link: '/tools/keyword-tools' },
            { text: '04-技术 SEO 工具', link: '/tools/technical-tools' },
            { text: '05-Google Analytics', link: '/tools/google-analytics' }
          ]
        }
      ],
      '/case-studies/': [
        {
          text: '案例分析',
          items: [
            { text: '01-案例分析', link: '/case-studies/' },
            { text: '02-内容网站 SEO 案例', link: '/case-studies/content-site-case' },
            { text: '03-工具网站 SEO 案例', link: '/case-studies/tool-site-case' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present'
    },
    search: {
      provider: 'local'
    },
    outline: {
      level: [2, 3],
      label: '页面导航'
    },
    lastUpdated: {
      text: '最后更新于'
    },
    docFooter: {
      prev: '上一页',
      next: '下一页'
    }
  }
})