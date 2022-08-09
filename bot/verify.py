from configparser import ConfigParser
import os

import base64
import hashlib
import hmac
import json 
channel_secret = '...' # Channel secret string
body = '...' # Request body string


root = os.getcwd()
configfile = os.path.join(root, 'config', 'config.ini')

config = ConfigParser()
config.read(configfile)
TOKEN = config['verification']['TOKEN']
SECRET = config['verification']['SECRET']



def verify(body, x_line_signature):
    body = json.dumps(body)
    channel_secret = SECRET # Channel secret string
    hash = hmac.new(channel_secret.encode('utf-8'),
    body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash)  
    print('Signature:', signature)
    print('X-Line-Signature:', x_line_signature)
    return signature == x_line_signature
