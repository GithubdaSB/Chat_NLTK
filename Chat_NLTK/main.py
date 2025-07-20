import csv
from datetime import datetime
from nltk.chat.util import Chat, reflections

# 定义规则
pairs = [
    [r"hi|hello|你好|嘿", ["你好！欢迎使用电商客服机器人，有什么可以帮助你的？"]],
    [r"运费(多少|呢|怎么算)|shipping (cost|fee)", ["标准运费为10元，订单满100元免运费！"]],
    [r"退货|return|退款|refund", ["我们支持7天无理由退货，请提供订单号以便处理。"]],
    [r"订单.*(状态|哪里|进度)", ["请提供订单号，我会帮你查询订单状态！"]],
    [r".*(谢|感谢|thanks)", ["不用客气，帮助你我也很开心"]],
    [r"(.*)", ["抱歉，我没听懂，能再详细说明吗？"]]
]

chatbot = Chat(pairs, reflections)

# 记录用户输入到CSV
def log_input(user_input, response):
    with open('chat_log.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), user_input, response])

# 交互循环
def converse_with_logging():
    print("我是电商客服机器人！输入'quit'退出。")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print(response)
        log_input(user_input, response)

if __name__ == "__main__":
    # 初始化CSV文件
    with open('chat_log.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'User Input', 'Response'])
    converse_with_logging()