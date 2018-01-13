# coding:utf-8

from bs4 import BeautifulSoup


class Parser(object):
    pass

    def __init__(self):
        self.root_url = 'http://sh.ganji.com'

    """ 一级页面链接分析
    """

    def style_parser(self, soup):
        datas = []
        for item in soup.select('li > h4 > a'):
            title = item.text
            code = item['href']
            item_url = self.root_url + code
            data = {
                'title': title,
                'code': code,
                'item_url': item_url
            }
            datas.append(data)
        return datas

    """细分条目详情列表分析器
    """

    def item_info_parser(self, item_soup):
        info_datas = []
        if item_soup.select('.next'):
            next_url = item_soup.select('.next')[0]['href']
            next_url = self.root_url + next_url
        else:
            next_url = ''
        for item in item_soup.select('.job-list'):
            title = item.select('.list_title')[0].text
            company = item.select('p.s-tit14')[0].text
            auth = item.select('.icon-my')
            if len(auth) > 0:
                auth = auth[0].text
            level = item.select('.s-integrity')
            if len(level) > 0:
                level = level[0].text
            if item.select('ul.clearfix > li'):
                money = item.select('ul.clearfix > li')[0].text.replace("薪资待遇：", "").strip()  # 薪酬
                area = item.select('ul.clearfix > li')[1].text.replace("工作地点：", "")  # 工作地点
                jinyan = item.select('ul.clearfix > li')[2].text.replace("工作经验：", "")  # 工作经理
                xueli = item.select('ul.clearfix > li')[3].text.replace("最低学历：", "")  # 学历
                need_num = item.select('ul.clearfix > li')[4].text.replace("招聘人数：", "")  # 需要人数
                company_num = item.select('ul.clearfix > li')[5].text.replace("公司规模：", "")  # 公司规模
            else:
                money = ''
                area = ''
                jinyan = ''
                xueli = ''
                need_num = ''
                company_num = ''
            data = {
                "title": title,
                "company": company,
                "auth": auth,
                "level": level,
                "money": money,
                "area": area,
                "jinyan": jinyan,
                "xueli": xueli,
                "need_num": need_num,
                "company_num": company_num
            }
            info_datas.append(data)
        return info_datas, next_url
