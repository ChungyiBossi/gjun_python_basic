from openai import OpenAI


def chat_with_openai(prompt):
    client = OpenAI(
        api_key='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'
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "你好，聖誕老公公，等一下你回話可不可以短於50字，因為很貴。",
            },
            {
                "role": "system", # ChatGPT 的回覆
                "content": "我是聖誕老公公，Merry Christmas!",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    print(chat_completion.choices[0].message.content)


if __name__ == '__main__':
    chat_with_openai("我想要禮物")