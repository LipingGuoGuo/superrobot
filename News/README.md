### 今日头条爬虫说明
#### 调用的库
- 1、openpyxl
```
from openpyxl import Workbook
wb = Workbook()
# 新建的工作簿默认预先建好一个工作表，通过 active 属性获取
# 如果工作簿包含多个工作表，该属性将返回第一个
ws = wb.active

# 通过create_sheet建立新的工作表
ws1 = wb.create_sheet("Mysheet")
# 在前面插入新的工作表
ws2 = wb.create_sheet("Mysheet2",0)

# 命名表格名
ws.title = "New Title"

# 遍历所有工作表，直接for in更为优雅
for sheet in wb:
    print(sheet.titlt)

```
#### 函数
- 1、获取as和cp值 `get_as_cp`
```
"""大神算法，两个参数在js文件：home_4abea46.js
! function(t){
    var e = {};
    e.getoney = function(){
        var t = Math.floor((new Date).getTime()/1e3)
            ,e = t.toString(16).toUpperCase()
            ,i = md5(t).toString().toUpperCase();
        if (8!=e.length)
            return{
                as:"",
                cp:""
             };
        for (var n = i.slice(0,5),a = i.slice(-5),s = "",o = 0;5 > o;
            s += n[o]+e[o];
        for (var r = "",c = 0;5>c;c++)
            r += e[c+3] + a[c];
        return {
            as:"",
            cp:""
        }
    }
    ,
    t.ascp = e
}(window,documnent),

"""python 获取cp和as值"""
def get_as_cp():
    zz = {}
    now = round(time.time())
    print(now)
    e = hex(int(now).upper()[2:]   
    print('e':e)
    a = hashlib.md5()
    print('a',a)
    a = update(str(int(now)).encode('utf-8'))
    i = a.hexdigest().upper()
    print('i':i)
    if len(e)!=8: 
        zz = {'as':'',
        'cp':''}
        return zz
    n = i[:5]
    a = i[-5:]
    r = ''
    s = ''
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r=e[j+3]+a[j]
    zz = {
    'as':'',
    'cp':''
    }
    print('zz',zz)
    return zz
    
```
- 3.DingtalkChatbot库
```
pip install DingtalkChatbot
```
- 4.requests库
```
# 爬虫过程中遇到payload报文，是一种json格式报文，传入的报文格式应是格式的
import requests
import json
url = ""
data = {
    'a':'',
    'b':''
}

# 1.其一方式
requests.post(url,data=json.dumps(data))
# 2.其二方式,json参数自动将字典类型的对象转换为json格式
requests.post(url,json=data)
```
