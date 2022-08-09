
import requests
from bot.verify import TOKEN, root, SECRET
import os
import json
import io
from PIL import Image
richmenu_id = '0'

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


# data = {
#     "size": {
#       "width": 2500,
#       "height": 1686
#     },
#     "selected": False,
#     "name": "Nice richmenu",
#     "chatBarText": "Tap here",
#     "areas": [
#       {
#         "bounds": {
#           "x": 0,
#           "y": 0,
#           "width": 2500,
#           "height": 1686
#         },
#         "action": {
#           "type": "postback",
#           "data": "action=buy&itemid=123"
#         }
#       }
#    ]
# }
# 
# data = json.dumps(data)
# r = requests.post(f'https://api.line.me/v2/bot/richmenu', 
#                     data=data,
#                     headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'})


# print(r)


line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)



image = os.path.join(root, 'register.png')
file = open(image, 'rb')

print(file)

file = Image.open(image)
# line_bot_api.set_rich_menu_image(richmenu_id, 'image/png', file)


rich_menu_list = line_bot_api.get_rich_menu_list()
for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)