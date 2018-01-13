# coding:utf-8
""" 页面资源下载器
    通过不同的url 路径，下载页面，返回接下后的soup
"""

import requests
from bs4 import BeautifulSoup
import time


class DownLoad(object):
    def __init__(self):
        self.re = self.per()

    @staticmethod
    def per():
        session = requests.session()
        session.header = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.32'}
        return session

    def soup_get(self, url):
        if url is None:
            pass
        else:
            session = self.re
            time.sleep(1)
            res = session.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup

    def soup_post(self, url, payload):
        if url is None:
            pass
        else:
            session = self.re
            res = session.post(url, payload)
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
