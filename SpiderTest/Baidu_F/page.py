# 1.对百度贴吧的任意帖子进行抓取
# 2.指定是否只抓取楼主发帖内容
# 3.将抓取到的内容分析并保存到文件
# 首先分析URL格式：基础部分http://tieba.baidu.com/p/3138733512，参数部分？see_lz=1&pn=1
# 正则表达式变更，当前代码需完善！

import re
import urllib

# 处理页面标签类
class Tool:
    # 去除img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceID = re.compile('<td>')
    # 将段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceID,"\t",x)
        x = re.sub(self.replacePara ,"\n  ",x)
        x = re.sub(self.replaceBR, "\n",x)
        x = re.sub(self.removeExtraTag ,"",x)
        # strip() 将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseURL,seeLZ):
        self.baseURL = baseURL
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()

    # 传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+self.seeLZ+"&pn="+str(pageNum)
            request = urllib.request(url)
            response = urllib.urlopen(request)
            return response.read().decode('utf-8')
        except:
            return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容，传入页面内容
    def getContent(self,page):
        pattern = re.compile('div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        # for item in items:
        #     print(item)
        print(self.tool.replace(items[1]))


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getContent(bdtb.getPage(1))
