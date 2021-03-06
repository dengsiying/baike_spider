from baike_spider import url_manager,html_downloader,html_outputer,html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
     #爬虫调度循环
    def craw(self,root_url):
        count = 1
        #将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 当url管理器中有待爬取url时，获取一个新的url
                new_url = self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))
                # 启动网页下载器 下载内容放到一个容器中
                html_cont =self.downloader.download(new_url)
                # 解析得到新的url列表和数据
                new_urls,new_data =self.parser.parse(new_url,html_cont)
                # 将新的url列表补充进url管理器 同时进行数据的收集
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count==100:
                    break
                count = count +1
            except:
                print('craw failed')
        # 调用输出器输出网页
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
