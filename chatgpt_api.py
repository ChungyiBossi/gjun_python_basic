from openai import OpenAI
from secret_tokens import OPENAI_SECRET_KEY

conversation_history = {
    # 'userid':[
    #     {
    #         "role": "user",
    #         "content": "A",
    #     },
    #     {
    #         "role": "system",
    #         "content": "B",
    #     }
    # ]
}

def clear_chat_history(line_user_id):
    conversation_history.pop(line_user_id)

    return '對話歷史紀錄已清除'


def talk_to_chatgpt_with_history(line_user_id, prompt):
    # 讀取歷史紀錄
    history = conversation_history.get(line_user_id, list())
    
    # 紀錄使用者說的話
    prompt = {
        "role": "user",
        "content": prompt,
    }
    history.append(prompt)
    
    # 紀錄chatgpt回覆
    chatgpt_response = talk_to_chatgpt(history)
    response = {
        "role": "system",
        "content": chatgpt_response
    }

    history.append(response)
    conversation_history[line_user_id] = history

    return chatgpt_response



def talk_to_chatgpt(history):
    client = OpenAI(
        api_key=OPENAI_SECRET_KEY
    )
    chat_completion = client.chat.completions.create(
        messages=history,
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content
    print(response)
    return response


if __name__ == '__main__':
    # message = [
    #     {
    #         "role": "user",
    #         "content": "我想要禮物",
    #     }
    # ]
    # talk_to_chatgpt(message)

    message_1 = input("You: ")
    r = talk_to_chatgpt_with_history("FAKE_ID", message_1)
    message_2 = input("You: ")
    r = talk_to_chatgpt_with_history("FAKE_ID", message_2)
    message_3 = input("You: ")
    r = talk_to_chatgpt_with_history("FAKE_ID", message_3)