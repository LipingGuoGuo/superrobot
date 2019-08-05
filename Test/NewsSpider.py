
from bs4 import BeautifulSoup
import re
import requests

class downloader(object):
    def __init__(self):
        self.target = 'http://imd.ccnu.edu.cn/xwdt/xydt.htm' #目标网址
    """
    函数说明:获取翻页地址
    Parameters:
        xiayiye - 下一页地址(string)
    Returns:
        fanye - 当前页面的翻页地址(list)
    """
    def get_fanye_url(self,target):
        req = requests.get(target) #获取对象
        req.encoding = "utf-8" #设置编码格式
        html = req.text #获得网页源代码
        bf = BeautifulSoup(html,'lxml') #利用BeautifulSoup进行解析
        fanye = []
        for x in bf.find_all('a',class_="Next"): #找到目标a标签
            link = x.get('href') #提取链接
            if link:
                link =  link.replace('xydt/','')
                link = "http://imd.ccnu.edu.cn/xwdt/xydt/" + link #将提取出来的链接补充完整
                fanye.append(link) #存入列表
        return fanye
    """
    函数说明:获取新闻地址
    Parameters:
        fanye - 翻页地址(string)
    Returns:
        xinwen_linklist - 新闻链接(list)
    """
    def get_xinwen_url(self, fanye):
         req = requests.get(fanye) #获取对象
         req.encoding = "utf-8" #设置编码格式
         html = req.text #获得网页源代码
         bf = BeautifulSoup(html,'lxml') #利用BeautifulSoup进行解析
         xinwen_linklist = [] #存入翻页地址
         for x in bf.find_all('a',href = re.compile('info/')): #找到目标a标签
             link = x.get('href') #提取链接
             if link:
                link = "http://imd.ccnu.edu.cn" + link.replace('../..','') #将提取出来的链接补充完整
                xinwen_linklist.append(link) #存入列表
         return xinwen_linklist

    """
    函数说明:获取新闻信息
    Parameters:
        xinwen_url - 新闻链接(string)
    Returns:
        xinwen - 新闻信息(list)
    """
    def get_xinwen(self, xinwen_url):
         req = requests.get(xinwen_url) #获取对象
         req.encoding = "utf-8" #设置编码格式
         html = req.text #获得网页源代码
         bf = BeautifulSoup(html,'lxml') #利用BeautifulSoup进行解析
         titles = bf.find_all('h1') #获取页面所有的h1标签
         title = titles[2].text#提取最后一个节点转换为文本
         print("标题："+title)
         author_date = bf.find_all('div',class_="cz")[0].text #获取页面的作者和日期
         print("作者和日期："+author_date)
         article = bf.find_all('div',class_="normal_intro")[0].text #获取页面正文
         print("正文："+article)
         xinwen = ["标题：" + title, "作者和日期：" + author_date, "正文：" + article]
         return xinwen


if __name__ == "__main__":
    dl = downloader()
    fanye = dl.get_fanye_url(dl.target)
    '''
    获取全部的翻页链接
    '''

    for x in fanye:
        b = dl.get_fanye_url(x)
        for w in b:  # 这一个循环的目的是获取翻页链接的同时去重
            if w not in fanye:
                fanye.append(w)
                print("翻页链接" + w)
    '''
    获取每一个翻页链接里的新闻链接
    '''
    xinwen_url = []
    for x in fanye:
        a = dl.get_xinwen_url(x)
        for w in a:  # 这一个循环的目的是获取新闻链接的同时去重
            if w not in xinwen_url:
                xinwen_url.append(w)
                print("新闻地址" + w)
    '''
    获取每一个新闻链接的新闻信息
    '''
    xinwen = []
    for x in xinwen_url:
        xinwen.append(dl.get_xinwen(x))