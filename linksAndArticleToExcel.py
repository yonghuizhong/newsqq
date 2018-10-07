import pymongo
import pandas
import time
import os

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']


for i in article.find():    # 将article表中文章正文更新到links表中
    links.update_one({'href': i['href']}, {'$set': {'article': i['article']}})

for i in links.find().limit(1):  # 将关键词转换为数组
    if isinstance(i['keywords'], list):
        print('keywords已经是list')
    else:
        print('keywords正在转为list')
        for j in links.find():
            keywords_array = j['keywords'].split(';')
            links.update_one({'href': j['href']}, {'$set': {'keywords': keywords_array}})

# links表放到Excel中
# name = '{}'.format(time.strftime("%m%d", time.localtime()))
# array = [i for i in links.find({}, {'_id': 0})]
# df = pandas.DataFrame(array)
# df.to_excel('./data/' + name + '.xlsx')

# links表放到json中
# command = 'mongoexport -d newsQQDB -c links --type=json -o ./data/{}.json'.format(name)
# os.system(command)
