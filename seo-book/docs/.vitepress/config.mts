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
      { text: '入门指南', link: '/guide/' },
      { text: '进阶技巧', link: '/advanced/' },
      { text: '工具推荐', link: '/tools/' },
      { text: '案例分析', link: '/case-studies/' }
    ],
    sidebar: {
      '/guide/': [
        {
          text: '入门指南',
          items: [
            { text: '什么是 SEO', link: '/guide/' },
            { text: '搜索引擎工作原理', link: '/guide/how-search-engines-work' },
            { text: 'Google 排名因素', link: '/guide/google-ranking-factors' },
            { text: '关键词研究基础', link: '/guide/keyword-research' },
            { text: '页面 SEO 优化', link: '/guide/on-page-seo' },
            { text: '技术 SEO 基础', link: '/guide/technical-seo' }
          ]
        }
      ],
      '/advanced/': [
        {
          text: '进阶技巧',
          items: [
            { text: '外链建设策略', link: '/advanced/link-building' },
            { text: '内容 SEO 策略', link: '/advanced/content-seo' },
            { text: '程序化 SEO', link: '/advanced/programmatic-seo' },
            { text: '多语言 SEO', link: '/advanced/multilingual-seo' },
            { text: '网站架构优化', link: '/advanced/site-architecture' },
            { text: 'AI 搜索优化', link: '/advanced/ai-seo' },
            { text: '惩罚恢复指南', link: '/advanced/penalty-recovery' },
            { text: 'SEO 数据分析', link: '/advanced/seo-analytics' }
          ]
        }
      ],
      '/tools/': [
        {
          text: '工具推荐',
          items: [
            { text: 'SEO 工具概览', link: '/tools/' },
            { text: 'Google Search Console', link: '/tools/google-search-console' },
            { text: 'Google Analytics', link: '/tools/google-analytics' },
            { text: '关键词研究工具', link: '/tools/keyword-tools' },
            { text: '技术 SEO 工具', link: '/tools/technical-tools' }
          ]
        }
      ],
      '/case-studies/': [
        {
          text: '案例分析',
          items: [
            { text: '案例学习方法', link: '/case-studies/' },
            { text: '工具站 SEO 案例', link: '/case-studies/tool-site-case' },
            { text: '内容站 SEO 案例', link: '/case-studies/content-site-case' }
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