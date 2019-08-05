import requests
import re
import urllib.request
import json
import sys
import os


headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=61f921ad913d1fc846412334774c700ca347aaff1158cac9381383468f5bdb40"


def DingtalkMsg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }
    print(requests.post(api_url, json.dumps(json_text), headers=headers).content)


# 创建opener对象设置为全局对象
url = "https://tianqi.moji.com/weather/china/zhejiang/hangzhou"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
# 正则的含义？？
par = '(<meta name="description" content=")(.*?)(">)'
opener = urllib.request.build_opener()
opener.addheaders = [header]

# 获取网页
html = urllib.request.urlopen(url).read().decode('utf-8')

# 提取需要爬取的内容
data = re.search(par, html).group(2)
DingtalkMsg(data)