# coding:utf-8
class URLManager(object):

    def __init__(self):
        self.item_new_url = set()
        self.first_new_url = set()
        self.first_old_url = set()
        self.item_old_url = set()

    def add_item_new_url(self, url):
        if url is None:
            return
        else:
            self.item_new_url.add(url)

    def has_item_new_url(self):
        return len(self.item_new_url) != 0

    def get_item_new_url(self):
        new_url = self.item_new_url.pop()
        self.item_old_url.add(new_url)
        return new_url

    def add_first_new_url(self, url):
        if url is None:
            return
        else:
            self.first_new_url.add(url)

    def has_first_new_url(self):
        return len(self.first_new_url) != 0

    def get_first_new_url(self):
        new_url = self.first_new_url.pop()
        self.first_old_url.add(new_url)
        return new_url
