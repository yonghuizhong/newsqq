import pymongo
import pandas
import time
import os

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']


for i in article.find():    # 将article表中文章正文更新到links表中
    links.update_one({'href': i['href']}, {'$set': {'article': i['article'], 'second_article': i['second_article']}})
del_num = 0
for i in links.find():  # 新闻阅读页面的链接
    if i['article'] == "none" or i['article'] == "":
        links.remove({'_id': i['_id']})
        del_num = del_num + 1
    else:
        my_url = 'http://127.0.0.1:8000/details/'  # 注意替换
        second_href = my_url + '?t=' + str(i['_id'])
        links.update_one({'_id': i['_id']}, {'$set': {'second_href': second_href}})
print("the delete number is ", del_num)

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
