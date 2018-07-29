import os
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']

while True:
	print(links.find().count())
	time.sleep(5)
