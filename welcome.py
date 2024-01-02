import os
import pprint
import json
import sys
from flask import Flask
from flask import render_template
from web_crawler.web_crawler import get_google_news
from flask import Flask, request, abort
from linebot.v3 import (
     WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from python_scripts.test_openai import chat_with_openai
from secret_tokens import (
    LINEBOT_ACCESS_TOKEN,
    LINEBOT_CHANNEL_SECRET
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = LINEBOT_CHANNEL_SECRET
channel_access_token = LINEBOT_ACCESS_TOKEN
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

handler = WebhookHandler(channel_secret)
configuration = Configuration(
    access_token=channel_access_token
)


@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    pprint.pprint(json.loads(body))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    chatgpt_response = chat_with_openai(event.message.text)
    # 回覆User傳過來的Message Event
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=chatgpt_response)
                ]
            )
        )
