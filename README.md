# 基于selenium爬取艾瑞网报告


## 一、项目简介
该项目主要用于从艾瑞网爬取不付费的报告信息，标题、行业、作者、摘要和报告原件。

## 二、项目结构
![` ST~2)_M_@{FBW8B`)U}VY](https://github.com/user-attachments/assets/83d0e204-1be0-41c5-907a-237d8dba0dc3)

## 三、环境要求
1.本项目基于 Python 开发，运行前需确保已安装 Python 环境，项目依赖的 Python 库在requirement.txt中列出。

2.运行本项目需要安装对应版本的Edge驱动，详细参考blog：

## 四、使用指南
### 4.1 准备工作
1.安装依赖；

2.确保项目目录具有读写权限，以便程序生成和保存文件。

### 4.2 运行项目
1.在项目根目录下，运行main.py文件：

2.运行过程中，程序会在终端输出提取和生成链接的相关信息，如：

提取的数字ID列表：

['12345', '67890', ...]

已保存结果到 extracted_ids.txt

生成链接: https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid=12345&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202505%2F12345.shtml
...

已保存生成的链接到 generated_links.txt

### 4.3 查看结果

运行完成后，可在项目目录下查看生成的extracted_ids.txt和generated_links.txt文件，获取提取的数字 ID 和生成的新链接。

## 声明
本爬虫项目仅用于学习用途。严禁将本项目用于任何非法目的，包括但不限于恶意攻击网站、窃取用户隐私数据、破坏网站正常运营、商业侵权等行为。

用户在使用本项目时，需自行承担因使用不当或违反法律法规所引发的一切后果与责任。若因用户使用本项目导致任何第三方权益受损或违反法律规定，相关法律责任均由用户自行承担，与本项目开发者及维护者无关。
