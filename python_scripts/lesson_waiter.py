
def send_to_speaker(mp4_filename):
    pass

def generate_voice_mp4(text):
    pass

def waiter_said_hello(customer_name):
    hello_words = f"Hello! {customer_name}, my name is ChatGPT."
    # 語音生成
    filename = generate_voice_mp4(text=hello_words)
    # 喇叭播放
    send_to_speaker(filename)

if __name__ == '__main__':
    waiter_said_hello("Peter")
    waiter_said_hello("Halen")
    waiter_said_hello("Joe")