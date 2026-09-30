#!/usr/bin/env python3
"""
批量处理哥飞公众号文章 v4
文章是单行文本（无换行符），需要特殊处理
"""

import os
import re
import shutil
from pathlib import Path

# 分类配置：(分类ID, 中文名, 标题关键词列表)
CATEGORIES = [
    ("seo-tutorials", "SEO教程和技巧", [
        'SEO', 'seo', '搜索', '关键词', '排名', '外链', '收录', '索引',
        'TDK', 'Canonical', 'Sitemap', 'robots', '搜索意图', '关键词密度',
        '搜索量', '竞争度', 'KGR', '谷歌趋势', 'Google Trends', 'Ahrefs',
        'Semrush', 'Similarweb', '谷歌排名', '内链', '页面优化', '结构化',
        '元标签', '谷歌Site', '搜索结果', 'SEO力', 'Nofollow', 'PageRank',
        '谷歌算法', '谷歌Search Console', 'Google Search Console',
        'Headings', 'Dofollow', '反链', '正向链接', '反向链接',
    ]),
    ("ai-tools", "AI工具和产品", [
        'AI', ' GPT', 'ChatGPT', 'Claude', 'Gemini', '大模型', 'LLM',
        '人工智能', 'DeepSeek', 'Midjourney', 'Stable Diffusion', 'DALL',
        'Sora', 'Veo', 'Embedding', '向量', 'RAG', 'AI搜索', 'AI生成',
        'AI产品', 'AI工具', 'AI编程', 'AI写作', 'copilot', 'Copilot',
        'AI代码', 'AI贴纸', 'AI对联', 'AI春联', 'SDXL', 'GPTs',
        'GPT_5', 'GPT-5', 'FLUX', 'FLUX.1', 'OpenAI', 'openai',
        '秘塔', 'SeekAll', 'ChatPDF', 'Cursor', 'cursor',
    ]),
    ("website-building", "建站教程", [
        '建站', '部署', '上线', '域名', 'Vercel', 'Cloudflare', 'WordPress',
        'Next.js', '前端', '后端', '开源', 'GitHub', '导航站', '工具站',
        '小游戏站', '游戏站', '多语言', '静态网站', '单页网站', '养网站',
        '网站防老', '上站', 'SVG', 'Logo', 'favicon', 'Tailwind', 'PHP',
        '小游戏', '小游戏网站', '饱和式建站', 'CMS',
    ]),
    ("monetization", "变现方式", [
        'Adsense', 'adsense', '广告费', '广告收入', '广告单价', 'ECPM',
        'Stripe', 'stripe', '收款', '收付款', '支付', '变现', '定价',
        '订阅', '月入', '日入', '年收入', '年营收', '月收入', '月营收',
        'Paddle', 'Creem', 'LemonSqueezy', 'Ko-fi', 'Buy me Coffee',
        '广告投放', '广告主', '广告平台', '流量主',
    ]),
    ("overseas-infra", "出海基础设施", [
        '公司注册', '海外公司', '美国公司', 'LLC', 'EIN', '银行',
        'Wise', '万里汇', '税务', '报税', '商标', '香港', '开户',
        'Mercury', '护照', 'Payoneer', 'OCBC', '海外手机号', '出海法财税',
        'Pin码', '实名认证', '港澳银行卡',
    ]),
    ("demand-mining", "需求挖掘", [
        '需求挖掘', '挖掘需求', '找词', '新词', '蓝海', '关键词挖掘',
        '长尾词', '搜索需求', '产品需求', '发现需求', '小词',
        '低竞争', '低难度', '关键词变种', '找新词', '财富密码',
    ]),
    ("product-ops", "产品运营", [
        '运营', '推广', '归因', '渠道', '增长', '留存', '转化',
        '发帖', 'Reddit', 'ProductHunt', 'Threads', 'Twitter',
        'Instagram', 'Pinterest', 'Medium', 'V2EX', '即刻', '小红书',
        '用户归因', '付费流量', '免费推广', '外链建设',
    ]),
    ("indie-dev", "独立开发者故事", [
        '独立开发', '独立开发者', '访谈', '一人公司', '个人开发者',
        '布衣', '出海赚美元', '出海赚钱', '月入万刀', '月入3W',
        '裸辞', '副业', '出海4个月', '出海半年', '出海一年',
        '第一笔美金', '第一美元', '土木工程师',
    ]),
    ("community", "社群运营", [
        '社群', '群友', '朋友们', '比赛', '线下聚会', '分享交流会',
        '新词新站比赛', 'Hackathon', '年中分享', '年终分享',
        '航海家', '南山小论坛', '哥飞的朋友们社群',
    ]),
    ("personal-growth", "个人成长", [
        '人生', '感悟', '觉醒', '牙疼', '职场', '思维', '认知',
        '普通人', '努力', '成功率', '坚持', '耐心', '从小事做起',
    ]),
    ("industry", "行业观察", [
        '排行榜', '流量排名', 'AI排行榜', '全球AI', '谷歌算法',
        '算法更新', 'HCU', '趋势', '行业观察', 'AI公众号',
        '热度榜',
    ]),
    ("tools", "工具推荐", [
        '推荐', '插件', 'AITDK', '免费工具', '开源项目',
        '前端学习', '免费产品推广',
    ]),
    ("policy", "政策解读", [
        '政策', '法规', '法律', '合规', '监管', '通知',
        '金融监管', 'BOI',
    ]),
    ("case-studies", "案例分析", [
        '案例', '月访问量', '访问量', '案例分享', '案例回顾',
        '案例观察', '评站', '拆解', '复盘',
    ]),
    ("overseas-earning", "出海赚钱经验", [
        '出海', '赚钱', '美金', '美元', '赚美元', '出海正当时',
        'Web出海', '出海产品',
    ]),
]


def classify_article(title, content_head):
    """根据标题和内容前500字分类"""
    title_lower = title.lower()

    for cat_id, cat_name, keywords in CATEGORIES:
        for kw in keywords:
            if kw.lower() in title_lower:
                return cat_id

    head_lower = content_head.lower()
    for cat_id, cat_name, keywords in CATEGORIES:
        for kw in keywords:
            if kw.lower() in head_lower:
                return cat_id

    return "case-studies"


def remove_marketing(content):
    """移除营销内容（适配单行文本格式）

    文章格式：标题 + 正文 + 营销推广（通常在末尾）
    文章是单行文本，没有换行符。
    """
    # 去掉开头格式标记
    content = re.sub(r'原创\s+我是哥飞\s+哥飞\s+在小说阅读器中沉浸阅读\s*', '', content)
    content = re.sub(r'^哥飞\s+在小说阅读器中沉浸阅读\s*', '', content)
    content = re.sub(r'编者荐语：\s*', '', content)
    content = re.sub(r'以下文章来源于\w+\s*，?\s*作者\w+\s*', '', content)

    # 去掉末尾标记
    content = re.sub(r'\s*阅读原文\s*$', '', content)
    content = re.sub(r'\s*修改于\s*$', '', content)
    content = re.sub(r'\s*作者提示:.*$', '', content)

    # 策略：从末尾往前找营销块的起始位置
    # 营销块通常包含：微信号、社群定价、付费社群推广等
    # 找到后截断

    # 模式1：从"如果你也想像哥飞"或类似引导句开始的推广
    m = re.search(r'如果你也想像哥飞', content)
    if m:
        content = content[:m.start()].strip()

    # 模式2：从"欢迎加入哥飞的付费社群"开始
    m = re.search(r'欢迎加入哥飞.{0,10}付费社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式3：从"如果想更多了解社群"开始
    m = re.search(r'如果想更多了解社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式4：从"如果对社群感兴趣"开始
    m = re.search(r'如果对社群感兴趣', content)
    if m:
        content = content[:m.start()].strip()

    # 模式5：从"社群主要面向"开始的社群介绍
    m = re.search(r'社群主要面向', content)
    if m:
        content = content[:m.start()].strip()

    # 模式6：从"那么这到底是一个什么样的社群"开始
    m = re.search(r'那么这到底是一个什么样的社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式7：从"感兴趣请加哥飞微信"开始
    m = re.search(r'感兴趣请加哥飞微信', content)
    if m:
        content = content[:m.start()].strip()

    # 模式8：从"欢迎加哥飞微信"开始
    m = re.search(r'欢迎加哥飞微信', content)
    if m:
        content = content[:m.start()].strip()

    # 模式9：从"请加哥飞微信"开始
    m = re.search(r'请加哥飞微信', content)
    if m:
        content = content[:m.start()].strip()

    # 模式10：从"加哥飞微信"开始（但不在引号内）
    m = re.search(r'[，。！]加哥飞微信', content)
    if m:
        content = content[:m.start() + 1].strip()

    # 模式11：从"社群定价"开始
    m = re.search(r'[，。]社群定价', content)
    if m:
        content = content[:m.start() + 1].strip()

    # 模式12：从"目前社群定价"开始
    m = re.search(r'目前社群定价', content)
    if m:
        content = content[:m.start()].strip()

    # 模式13：从"这个社群7月"开始的社群运营介绍
    m = re.search(r'这个社群\d+月\d+号?开始运营', content)
    if m:
        content = content[:m.start()].strip()

    # 模式14：哥飞运营了一个付费社群
    m = re.search(r'哥飞运营了一个付费社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式15：从"如果你是程序员，那么这绝对"开始
    m = re.search(r'如果你是程序员，那么这绝对', content)
    if m:
        content = content[:m.start()].strip()

    # 模式16：从"给大家看看已经在社群里的"开始
    m = re.search(r'给大家看看已经在社群里的', content)
    if m:
        content = content[:m.start()].strip()

    # 模式17：从"下面给大家介绍一下哥飞的这个付费社群"开始
    m = re.search(r'下面给大家介绍一下哥飞的这个付费社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式18：从"哥飞运营的付费社群"开始
    m = re.search(r'哥飞运营的付费社群', content)
    if m:
        content = content[:m.start()].strip()

    # 模式19：从"推荐阅读"或"相关阅读"开始
    m = re.search(r'推荐阅读|相关阅读', content)
    if m and m.start() > len(content) * 0.5:  # 只在文章后半部分才移除
        content = content[:m.start()].strip()

    # 最终清理
    content = content.strip()

    return content


def process_all():
    root = Path(__file__).resolve().parent
    input_dir = root / 'gefei_offical_article'
    output_dir = root / 'articles'

    # 清空并重建
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    cat_ids = [c[0] for c in CATEGORIES]
    for cat_id in cat_ids:
        (output_dir / cat_id).mkdir(parents=True, exist_ok=True)

    article_files = sorted(input_dir.glob('*.txt'))
    print(f"找到 {len(article_files)} 篇文章")

    results = {}
    skipped = []

    for i, f in enumerate(article_files, 1):
        try:
            content = f.read_text(encoding='utf-8')

            # 提取标题
            title = content.split('原创')[0].strip() if '原创' in content else content[:100]
            title = re.sub(r'【.*?】', '', title).strip()

            # 移除营销内容
            cleaned = remove_marketing(content)

            # 内容前500字用于分类
            content_head = cleaned[:500]

            # 分类
            category = classify_article(title, content_head)

            # 跳过太短的
            if len(cleaned.strip()) < 50:
                skipped.append((f.name, len(cleaned.strip())))
                continue

            # 保存
            output_path = output_dir / category / f.name
            output_path.write_text(cleaned, encoding='utf-8')

            if category not in results:
                results[category] = []
            results[category].append(f.name)

        except Exception as e:
            print(f"  错误: {f.name}: {e}")
            skipped.append((f.name, 0))

        if i % 100 == 0:
            print(f"已处理 {i}/{len(article_files)} 篇文章")

    # 统计
    print(f"\n处理完成！")
    cat_names = {c[0]: c[1] for c in CATEGORIES}
    total = 0
    for cat_id in cat_ids:
        count = len(results.get(cat_id, []))
        total += count
        if count > 0:
            print(f"  {cat_names[cat_id]}: {count} 篇")
    print(f"  总计: {total} 篇")
    if skipped:
        print(f"  跳过: {len(skipped)} 篇")

    # 生成索引
    generate_index(results, cat_names, cat_ids, output_dir)


def generate_index(results, cat_names, cat_ids, output_dir):
    index_path = output_dir / 'readme.md'

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# 哥飞公众号文章分类索引\n\n")
        f.write("本目录包含哥飞公众号「哥飞」的文章，已按主题分类整理。\n\n")
        f.write("## 分类目录\n\n")

        for cat_id in cat_ids:
            files = results.get(cat_id, [])
            if files:
                f.write(f"- [{cat_names[cat_id]}](#{cat_id}) ({len(files)} 篇)\n")

        f.write("\n---\n\n")

        for cat_id in cat_ids:
            files = results.get(cat_id, [])
            if not files:
                continue

            f.write(f"## {cat_id}\n\n")
            f.write(f"**{cat_names[cat_id]}**\n\n")

            for filename in sorted(files):
                title = filename.replace('.txt', '').replace('_', ' ')
                f.write(f"- [{title}]({cat_id}/{filename})\n")

            f.write("\n")

    print(f"\n索引文件已生成: {index_path}")


if __name__ == '__main__':
    process_all()
