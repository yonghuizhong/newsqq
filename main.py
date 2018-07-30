import os
import pymongo

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']

links.remove()
if os.path.isfile('newsqq.json'):
    os.remove('newsqq.json')
os.system('scrapy crawl links_spider -o newsqq.json')
