# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class NewsqqPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.newsQQDB = self.client['newsQQDB']
        self.links = self.newsQQDB['links']
        self.article = self.newsQQDB['article']

    def process_item(self, item, spider):
        if spider.name == 'links_spider':
            data = dict(item)
            self.links.insert(data)
            return item

        elif spider.name == 'article_spider':
            data2 = dict(item)
            self.article.insert(data2)
            return item
