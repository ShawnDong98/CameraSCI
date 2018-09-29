'''
Created on 2018-1-26
定制化图像接口-Python3 -API示例代码
@author: 小帅丶
'''
import urllib3,base64
import json
access_token='24.ab6b4beef713cd0e98faa0bb0aefa5d2.2592000.1527074728.282335-11054645'
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/rubbish?access_token='+access_token
f = open('/home/pi/pythoncode/shot.png','rb')
#参数image：图像base64编码 以及top_num参数
img = base64.b64encode(f.read())
#img参数进行一下str转换
params={'image':''+str(img,'utf-8')+'','top_num':5}
#对base64数据进行urlencode处理
encoded_data = json.dumps(params).encode('utf-8')
request=http.request('POST', 
                      url,
                      body=encoded_data,
                      headers={'Content-Type':'application/json'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)
