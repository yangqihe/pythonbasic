import requests
import json
#url = 'https://www.baidu.com'
url = 'https://jiaoyou.hongqiai.com/user/getMatchList?token=psF7seD4dDbILEOzZT7nTQ=='
try:
    response = requests.post(url)
    if (response):
        print("请求成功")
        str = response.text;
        #该方法字符串转json字符串 会加上转义符
        #jsonstr = json.dumps(str)
        #该方法会去除转义符 字符串转字典 如果有多个转义符  json.load(json.loads(str)) 需要多次转换
        dict = json.loads(str)
        if(dict['isSuccess']):
            print(dict['result'])
        else:
            print(dict)
except Exception as e:
    print("请求错误 \n" , e)