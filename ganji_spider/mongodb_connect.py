# coding:utf-8

import pymongo


class Connect(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.ganji = client['ganjijianzhi']

    def insert_first(self, first_datas):
        first_item = self.ganji['first_item']

        for item in first_datas:
            if first_item.find_one(item):
                pass
            else:
                first_item.insert(item)

    def insert_second(self, name, second_datas):
        print(name)
        name = self.ganji[name]

        for item in second_datas:
            if name.find_one(item):
                pass
            else:
                name.insert(item)
