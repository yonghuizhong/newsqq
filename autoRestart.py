import pymongo
import os
import time
import random
import sys

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']
count = 0  # 正文爬虫 执行次数


def watch():
    global count    # 全局变量
    while True:
        count = count + 1
        data_array = [i['href'] for i in links.find()]  # 数据库的原始数据
        got_array = [i['href'] for i in article.find()]  # 已经爬到的数据
        x = set(data_array)
        y = set(got_array)
        rest_array = x.difference(y)  # 需要爬的数据
        if len(rest_array) > 0 and count < 3:
            if count == 1:
                print('第', count, '次运行程序')
                os.system('scrapy crawl article_spider')    # 执行正文爬虫
            else:
                print('第', count, '次运行程序')
                print('暂停30秒...')
                time.sleep(30+random.uniform(1, 3))
                os.system('scrapy crawl article_spider')
        else:
            print('爬虫重启次数达到限值，已停止；或已经爬取完毕~')
            sys.exit()


watch()
