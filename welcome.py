import pprint
import json
import sys
import requests
import cv2
from flask import Flask, request, abort, render_template
from linebot.v3 import (
     WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    ImageMessageContent
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage,
    LocationMessage
)
from chatgpt_api import (
    talk_to_chatgpt_with_history,
    clear_chat_history
)

from mediapipe_image_embedding import (
    opencv_detect_faces
)

from secret_tokens import (
    LINEBOT_ACCESS_TOKEN,
    LINEBOT_CHANNEL_SECRET
)

from imgur_upload import upload_to_imgur

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
@app.route("/show_image",methods=['POST','GET'])
def show_image():
    # Handle audio process here
    return render_template('show_image.html') # render image with jinja parameters

@app.route("/xxx",methods=['POST','GET'])
def frontend_trigger():
    return render_template('frontend_trigger.html')

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    pprint.pprint(json.loads(body))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_text(event):
    user_id = event.source.user_id
    user_message = event.message.text
    if user_message in ['清除歷史紀錄', '清除對話', '忘記我吧']:
        chatgpt_response = clear_chat_history(user_id)
    else:
        chatgpt_response = talk_to_chatgpt_with_history(user_id, user_message)
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

import numpy as np
@handler.add(MessageEvent, message=ImageMessageContent)
def handle_image(event):
    image_binary = get_image(event)
    face_cascade = cv2.CascadeClassifier(".\ml_models\haarcascade_frontalface_default.xml")   # 載入人臉模型
    img_array = np.frombuffer(image_binary, dtype=np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    bboxes, _ = opencv_detect_faces(image, face_cascade, './face_image')

    response_message = [TextMessage(text=f'I got a image. their are {len(bboxes)} people')]

    # 需要把圖檔傳到雲端空間(有https url的)，才能夠回傳圖檔訊息
    image_url = upload_to_imgur('face_bbox.jpg')
    response_message.append(ImageMessage(
        originalContentUrl=image_url,
        previewImageUrl=image_url)
    )

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=response_message
            )
        )

def get_image(event, save_image=True):
    message_id = event.message.id
    # 'Authorization: Bearer {channel access token}'
    image_data = requests.get(
        url=f'https://api-data.line.me/v2/bot/message/{message_id}/content',
        headers={'Authorization': f'Bearer {channel_access_token}'}
    )

    if save_image:
        with open('image.jpg', 'wb') as image:
            image.write(image_data.content)
    
    return image_data.content

