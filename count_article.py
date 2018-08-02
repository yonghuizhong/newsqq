import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']

while True:
    links_array = [i['href'] for i in links.find()]
    article_array = [i['href'] for i in article.find()]
    x = set(links_array)
    y = set(article_array)
    print('总共需获取' + str(len(x)), '已获取' + str(len(y)))
    left_set = x.difference(y)
    print('仍需获取 ' + str(len(left_set)))
    time.sleep(5)
