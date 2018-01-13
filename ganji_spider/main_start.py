# coding:utf-8
# 主启动页

from ganji_spider import html_download, html_parser, url_manager, mongodb_connect


class MainStart(object):
    def __init__(self):
        self.root_url = 'http://sh.ganji.com'
        self.urls = url_manager.URLManager()
        self.download = html_download.DownLoad()
        self.parser = html_parser.Parser()
        self.mongo = mongodb_connect.Connect()

    def control(self, url):
        count = 0
        soup = self.download.soup_get(url)
        datas = self.parser.style_parser(soup)
        self.mongo.insert_first(datas)
        item_count = 0
        for item in datas:
            new_url = item['item_url']
            self.urls.add_item_new_url(new_url)
            while self.urls.has_item_new_url():
                try:
                    item_soup = self.download.soup_get(self.urls.get_item_new_url())
                    info, next_url = self.parser.item_info_parser(item_soup)
                    self.urls.add_item_new_url(next_url)
                    self.mongo.insert_second(datas[item_count]['code'], info)
                    count += 1
                    print(count)
                    print(next_url)
                except:
                    print()
            item_count += 1


if __name__ == "__main__":
    spider = MainStart()
    spider.control("http://sh.ganji.com/jianzhi/")
