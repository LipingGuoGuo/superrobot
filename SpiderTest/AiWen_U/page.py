import time
import sys
import urllib


# 获取具体时间
def getCurrentTime(self):
    return time.strftime('[%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 获取具体日期
def getCurrentData(self):
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

# 主函数
def main(self):
    # 因为需要将缓冲区设置输出到log中，需要在程序的最前面加上这两句
    f_handler = open('out_log', 'w')
    sys.stdout = f_handler
    page = open('page.txt','r')
    content = page.readline()
    start_page = int(content.strip()) - 1
    page.close()
    print(self.getCurrentTime(),"开始页码",start_page)
    print(self.getCurrentTime,"爬虫开始启动，开始爬取爱问知识人问题")
    self.total_num = self.getTotalPageNum()
    print(self.getCurrentTime(),"获取到目录页面的个数",self.total_num,"个")
    if not start_page:
        start_page = self.total_num
    for x in range(1,start_page):
        print(self.getCurrentTime(),"正在抓取第",start_page-x+1,"个页面")
        try:
            self.getQuestions(start_page-x+1)
        except Exception as e:
            print(self.getCurrentTime(),"某总页面内抓取或提取失败，错误原因",e)
        if start_page-x+1 < start_page:
            with open("page.txt","w") as f:
                f.write(str(start_page-x+1))
                print(self.getCurrentTime(),"写入新页码",start_page-x+1)
                f.close()


