import pymongo
import pandas
import time
import os

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']


for i in article.find():
    links.update_many({'href': i['href']}, {'$set': {'article': i['article']}})

# links表放到Excel中
name = '{}'.format(time.strftime("%m%d", time.localtime()))
array = [i for i in links.find({}, {'_id': 0})]
df = pandas.DataFrame(array)
df.to_excel('./data/' + name + '.xlsx')
# command = 'mongoexport -d newsQQDB -c links --type=json -o ./data/{}.json'.format(name)
# os.system(command)
