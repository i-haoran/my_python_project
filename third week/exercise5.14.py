import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)


def chat_with_deepseek(prompt, model="deepseek-chat", max_tokens=500):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个有帮助的助手"},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


# 使用
answer = chat_with_deepseek("什么是python？学python的好处？")
print(answer)
