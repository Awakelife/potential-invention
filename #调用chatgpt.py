#调用chatgpt
# 您好！要使用Python调用ChatGPT制作中文聊天机器人，需要先安装相应的Python包和依赖项。
# 在此之前，您需要一个OpenAI API密钥才能使用ChatGPT API。您可以在OpenAI的网站上注册并获取API密钥。

# 一旦您有了API密钥，就可以安装Python OpenAI包并使用以下代码与ChatGPT API进行交互：


import openai
openai.api_key = "org-LtTWDpM5Me8zHzAxdNu93DO3"

try:
    def ask_question(question, model, temperature=0.5):
        response = openai.Completion.create(
            engine=model,
            prompt=question,
            max_tokens=1024,
            temperature=temperature
        )

        answer = response.choices[0].text
        return answer.strip()
finally:
    print("连接超时")
    

# 这个函数使用OpenAI的Python SDK向ChatGPT API发送问题并返回回答。在这个函数中，您需要将YOUR_API_KEY_HERE替换为您的API密钥。

# 接下来，您可以定义一个简单的交互循环，让用户输入问题并获取回答：
model_engine = "davinci"  # 模型引擎
print("欢迎来到中文聊天机器人！输入“exit”退出程序。")

while True:
    user_input = input("您的问题: ")
    if user_input.lower() == "exit":
        break

    answer = ask_question(user_input, model_engine)
    print("聊天机器人: " + answer)
# 在这个循环中，用户输入一个问题，程序将使用ask_question函数从ChatGPT API中获取回答，并将其输出到控制台上。

# 请注意，这个示例代码使用的是英文的ChatGPT模型，如果您需要使用中文模型，请将模型引擎替换为中文模型的名称。
# 同时，ChatGPT中文模型的效果并不如英文模型，因此可能需要更多的训练和调整才能达到良好的效果。