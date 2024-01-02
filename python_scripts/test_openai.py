from openai import OpenAI
from secret_tokens import OPENAI_SECRET_KEY


def chat_with_openai(prompt):
    client = OpenAI(
        api_key=OPENAI_SECRET_KEY
        
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content
    print(response)
    return response


if __name__ == '__main__':
    chat_with_openai("我想要禮物")