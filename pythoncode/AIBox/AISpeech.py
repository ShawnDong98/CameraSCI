#!/sur/bin/python
#coding: utf8
#@date = '2018.4.29'
#@author = 'ShawnDong'

#--------------------------------
import requests
import json
import base64
import urllib
from aip import AipSpeech
import os

#---------------------------------

#---------------------------------------------------------------------------
# The AI-Recognization Program
#---------------------------------------------------------------------------
def  get_access_token():
    APP_ID = '11172380'
    API_KEY = 'Zs4xdq3iChrqAAetHPTaBcyb'
    SECRET_KEY = 'dv7To8GRDqgDmfnajTzPMk8UvHiXsZ73'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
    response = requests.post(host)
    access_token = response.content.decode('utf-8')
    access_token = json.loads(access_token)

    access_token = str(access_token['access_token'])

    return access_token, client

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def VoiceRecognization(client):
    result = client.asr(get_file_content('/home/pi/pythoncode/AIBox/temp.wav'), 'wav', 16000, {
        'dev_pid': '1536',
        })
    return result

def SyntheticSpeech(str,client):
     result  = client.synthesis(str, 'zh', 1, {
            'pit':4, 'vol': 5, 'per': 3,
             })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
     if not isinstance(result, dict):
        with open('JarvisAnswer.mp3', 'wb') as f:
            f.write(result)

    
