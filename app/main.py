from flask import request, abort, Flask
from bot.handler import handler
import json


app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello CleanNavi!</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        handler(request.json, request.headers['X-Line-Signature'])
        print(request.json)
        return request.json
    else:
        abort(400)


    

