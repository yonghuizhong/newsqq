import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']
cate = newsQQDB['cate']

# type_array = []
# with open('myType.txt', 'rt') as f:
#     for line in f:
#         type_array.append(line.strip())
# print('类型数为' + str(len(type_array)))
# for i in type_array:
#     data = {
#         'type_name': i.split('，')[0],
#         'type_link': i.split('，')[2]
#     }
#     cate.insert_one(data)


while True:
    links_array = [i['href'] for i in links.find()]
    article_array = [i['href'] for i in article.find()]
    x = set(links_array)
    y = set(article_array)
    print('总共需获取' + str(len(x)), '已获取' + str(len(y)))
    left_set = x.difference(y)
    print('仍需获取 ' + str(len(left_set)))
    time.sleep(5)
