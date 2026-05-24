#!/usr/bin/env python3
"""
将 articles/ 目录下的 .txt 文件转换为 markdown 格式
"""

import re
from pathlib import Path


def convert_to_markdown(content, filename):
    """将单行文本转换为 markdown 格式"""

    # 提取标题（文件名去掉扩展名，用空格替换下划线）
    title = filename.replace('.txt', '').replace('_', ' ')

    # 清理内容开头的格式标记
    content = re.sub(r'^原创\s+我是哥飞\s+哥飞\s+在小说阅读器中沉浸阅读\s*', '', content)
    content = re.sub(r'^哥飞\s+在小说阅读器中沉浸阅读\s*', '', content)
    content = re.sub(r'^编者荐语：\s*', '', content)
    content = re.sub(r'^以下文章来源于\w+\s*，?\s*作者\w+\s*', '', content)

    # 去掉末尾标记
    content = re.sub(r'\s*阅读原文\s*$', '', content)
    content = re.sub(r'\s*修改于\s*$', '', content)
    content = re.sub(r'\s*作者提示:.*$', '', content)

    # 构建 markdown
    md_lines = []

    # 添加标题
    md_lines.append(f'# {title}')
    md_lines.append('')

    # 将内容按句子分割，然后重新组合成段落
    # 策略：在特定标点后添加换行，形成段落
    text = content.strip()

    # 在句号、问号、感叹号后添加换行（但不在数字后面的句号后）
    # 先处理明显的段落分隔点
    text = re.sub(r'([。！？])', r'\1\n\n', text)

    # 处理列表项（1、2、3、等）
    text = re.sub(r'(\d+、)', r'\n\1', text)

    # 处理"第X点"、"第X步"等
    text = re.sub(r'(第[一二三四五六七八九十\d]+[点步])', r'\n\1', text)

    # 处理"一、"、"二、"等中文序号
    text = re.sub(r'([一二三四五六七八九十]+、)', r'\n\1', text)

    # 处理"案例1："、"案例2："等
    text = re.sub(r'(案例\d+[：:])', r'\n\1', text)

    # 处理"样式1："、"样式2："等
    text = re.sub(r'(样式\d+[：:])', r'\n\1', text)

    # 处理"备注："、"注意："、"提示："
    text = re.sub(r'(备注[：:])', r'\n\1', text)
    text = re.sub(r'(注意[：:])', r'\n\1', text)
    text = re.sub(r'(提示[：:])', r'\n\1', text)

    # 处理"总结："、"结论："
    text = re.sub(r'(总结[：:])', r'\n\1', text)
    text = re.sub(r'(结论[：:])', r'\n\1', text)

    # 处理"举例："、"例如："
    text = re.sub(r'(举例[：:])', r'\n\1', text)
    text = re.sub(r'(例如[：:])', r'\n\1', text)

    # 清理多余的空行
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 分割成段落
    paragraphs = text.split('\n\n')

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # 检查是否是列表项
        if re.match(r'^\d+[、.]', para):
            # 转换为 markdown 列表
            para = re.sub(r'^(\d+)[、.]', r'\1.', para)
            md_lines.append(para)
            md_lines.append('')
        elif re.match(r'^[一二三四五六七八九十]+、', para):
            # 中文序号转为二级标题
            para = re.sub(r'^([一二三四五六七八九十]+、)', r'## \1', para)
            md_lines.append(para)
            md_lines.append('')
        elif re.match(r'^案例\d+[：:]', para):
            # 案例标题转为三级标题
            para = re.sub(r'^(案例\d+[：:])', r'### \1', para)
            md_lines.append(para)
            md_lines.append('')
        elif re.match(r'^样式\d+[：:]', para):
            # 样式标题转为三级标题
            para = re.sub(r'^(样式\d+[：:])', r'### \1', para)
            md_lines.append(para)
            md_lines.append('')
        elif re.match(r'^(备注|注意|提示)[：:]', para):
            # 备注等转为引用块
            para = re.sub(r'^(备注|注意|提示)[：:]', r'> **\1：**', para)
            md_lines.append(para)
            md_lines.append('')
        elif re.match(r'^(总结|结论)[：:]', para):
            # 总结等转为二级标题
            para = re.sub(r'^(总结|结论)[：:]', r'## \1：', para)
            md_lines.append(para)
            md_lines.append('')
        else:
            # 普通段落
            md_lines.append(para)
            md_lines.append('')

    # 添加来源信息
    md_lines.append('---')
    md_lines.append('')
    md_lines.append(f'> 来源：哥飞公众号')
    md_lines.append(f'> 原始文件：{filename}')

    return '\n'.join(md_lines)


def process_all():
    """处理所有文件"""
    input_dir = Path('/Users/jayinton/projects/my_research/gefei_seo/articles')

    # 统计
    total = 0
    converted = 0

    # 遍历所有分类目录
    for cat_dir in sorted(input_dir.iterdir()):
        if not cat_dir.is_dir():
            continue

        # 处理该目录下的所有 .txt 文件
        txt_files = sorted(cat_dir.glob('*.txt'))

        for txt_file in txt_files:
            total += 1

            try:
                # 读取内容
                content = txt_file.read_text(encoding='utf-8')

                # 转换为 markdown
                md_content = convert_to_markdown(content, txt_file.name)

                # 生成 .md 文件路径
                md_file = txt_file.with_suffix('.md')

                # 保存
                md_file.write_text(md_content, encoding='utf-8')

                converted += 1

            except Exception as e:
                print(f'错误: {txt_file.name}: {e}')

        if txt_files:
            print(f'{cat_dir.name}/: 处理了 {len(txt_files)} 个文件')

    print(f'\n转换完成！')
    print(f'总计: {total} 个文件')
    print(f'成功: {converted} 个文件')
    print(f'失败: {total - converted} 个文件')


if __name__ == '__main__':
    process_all()
