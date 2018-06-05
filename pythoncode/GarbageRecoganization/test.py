import requests
import json
import base64
import urllib
from aip import AipImageClassify, AipSpeech
import os
import time

def IfWIFI():
    a = os.popen("hostname -I")
    a = a.readline()
    print(len(a))
    if len(a) == 1:
        return 1
    else:
        return 0

while (IfWIFI()):
    print("No WIFI")
    


