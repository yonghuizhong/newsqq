import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']

up = 0
while True:
    links_array = [i['href'] for i in links.find()]
    article_array = [i['href'] for i in article.find()]
    x = set(links_array)
    y = set(article_array)
    print('总共需获取' + str(len(x)), '已获取' + str(len(y)))
    down = len(y)
    left_set = x.difference(y)
    rate = (down-up) / 5
    up = down
    print('仍需获取 ' + str(len(left_set)), '目前速率：%s num/s\n' % (str(rate)))
    time.sleep(5)
