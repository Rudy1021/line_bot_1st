import os
from os.path import isfile, isdir, join
from flask import Flask, request, abort
import random
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
ran = False
line_message = True
c = 10
d = 10
picc = 0
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Channel Access Token')
# Channel Secret
handler = WebhookHandler('Channel Secret')
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#	global f
#	global fi
	user_id = event.source.user_id
	print("user_id =", user_id)
#群組ID 沒用到
#	group_id = event.source.group_id
#	print("group_id =", group_id)

	text = event.message.text
	global picc
	global c
	global line_message
	global ran
	global d
	b = 0
	an = 0
	arr = []
	apw = []
	che = True
	if(ran == True):
		c = random.randint(0,10)

	if(text == '你很煩' and line_message == True and ran == False):
		line_bot_api.reply_message(event.reply_token, TextMessage(text='那我少講話行了吧'))
		ran = True
		c = random.randint(0, 10)
		che == False

	for ww in text:
		apw.append(text[an:an+1])
		an+=1
		qq = len(apw)
	for mu in text:
		arr.append(text[b:b+2])
		b+=1
		a = len(arr)
#有關鍵字
	for n in range(a):
		if (arr[n] == '笑死' and line_message == True and c == 10):
			line_bot_api.reply_message(event.reply_token, TextMessage(text='笑死'))
			break
		if (arr[n] == '?' or text=='？' and line_message == True and c == 10):
			line_bot_api.reply_message(event.reply_token, TextMessage(text='這我知道!!'))
			break

		if (arr[n] == '阿哲' and line_message == True and c == 10 and che == True):
			picc = random.randint(1, 10)
			if(picc==10):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==1):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==2):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==3):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==4):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==5):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==6):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==7):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==8):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
			if(picc==9):
				message = ImageSendMessage(
   				original_content_url='jpg',
   				preview_image_url='jpg')
				line_bot_api.reply_message(event.reply_token, message)
#
#
#
	if(text == '閉嘴' and line_message == True and c == 10):
		line_message = False
		line_bot_api.reply_message(event.reply_token, TextMessage(text='好我閉嘴'))

	if (text == '講話' and (line_message == False or ran == True or che == False)):
			line_bot_api.reply_message(event.reply_token, TextMessage(text='啥'))
			line_message = True
			ran = False
			c = 10
			che = True
#有關鍵字
#單關鍵字區
	for qu in range(qq):
		if (apw[qu] == '郭' and line_message == True and c == 10):
			line_bot_api.reply_message(event.reply_token, TextMessage(text='小郭4P喔'))
			break
#單關鍵字區
#User_id區
	if (text == '滾' and user_id != user_id):
		line_bot_api.reply_message(event.reply_token, TextMessage(text='兇啥小?'))

	if (text == '滾' and user_id == user_id):
		line_bot_api.reply_message(event.reply_token, TextMessage(text='好我自退'))
		line_bot_api.leave_group(group_id)

	if(user_id == user_id and d == 10):
		line_bot_api.reply_message(event.reply_token, TextMessage(text='另一個我閉嘴好不好'))		
		d = random.randint(9, 10)
#User_id區
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
