import urllib
import re
import time
import types
import page
import mysql
import sys
from bs4 import BeautifulSoup


class Spider:

     # 初始化
    def __init__(self):
         self.page_num = 1
         self.total_num = None
         self.page_spider = page.Page()
         self.mysql = mysql.Mysql()

    # 获取具体时间
    def getCurrentTime(self):
         return time.strftime('[%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 获取具体日期
    def getCurrentData(self):
         return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 通过页面的URL来获取页面的代码
    def getPageURL(self,url):
         try:
             request = urllib.request(url)
             response = urllib.urlopen(request)
             return response.read().decode('utf-8')
         except Exception as e:
             print("出错",e)

