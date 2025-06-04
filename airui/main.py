import re

# 读取文件内容
with open('found_links.txt', 'r', encoding='utf-8') as f:
    links = f.readlines()

# 定义正则表达式
pattern = re.compile(r'https?://[^/]+/report/.+?/(\d+)\.shtml')

# 提取数字ID
extracted_ids = []
for link in links:
    link = link.strip()  # 去除换行符
    match = pattern.search(link)
    if match:
        extracted_ids.append(match.group(1))  # 取第一个捕获组
    else:
        print(f"未匹配到ID：{link}")

# 输出结果
print("提取的数字ID列表：")
print(extracted_ids)

# 保存结果到文件
with open('extracted_ids.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(extracted_ids))
print("已保存结果到 extracted_ids.txt")

link_template = 'https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid={}&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202505%2F{}.shtml'

# 生成替换后的链接列表
new_links = []
for report_id in extracted_ids:
    new_link = link_template.format(report_id, report_id)
    new_links.append(new_link)
    print(f"生成链接: {new_link}")

# 保存结果到文件
with open('generated_links.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_links))
print("已保存生成的链接到 generated_links.txt")