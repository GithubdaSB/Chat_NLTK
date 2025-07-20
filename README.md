# 电商客服聊天机器人
这是一个基于NLTK的规则-based聊天机器人项目，设计用于电商客服场景。

## 技术栈
- Python
- NLTK (Natural Language Toolkit)
- CSV数据记录

## 功能
- 支持5种用户意图（问候、运费、退货、订单状态、默认回复）
- 意图识别准确率：60%（优化前50%）
- 记录用户对话到chat_log.csv

## 界面原型
- 设计：Figma
- 链接：[https://www.figma.com/design/XN6dBKt1w9hRwT53PAG50X/Chat_bot?m=dev&t=iwD30ZisVgUWhDXs-1]

## 成果
- 50名用户测试，85%正面反馈
- 优化：扩展规则，处理未回答问题

## 安装与运行
1. 克隆仓库：
   ```bash
   git clone https://github.com/GithubdaSB/Chat_NLTK.git
2.安装依赖
  pip install nltk
  python -m nltk.downloader punkt
