from textrank4zh import TextRank4Sentence
from pathos.multiprocessing import ProcessingPool
import pymongo
import time

# 读取数据库文章信息
client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
tr4s = TextRank4Sentence()


def gen_summary(text, _id):
    global tr4s
    tr4s.analyze(text=text, lower=True, source='all_filters')
    try:
        summary = tr4s.get_key_sentences(num=1)[0].sentence
    except:
        summary = ''
    links.update_one({'_id': _id}, {'$set': {'summary': summary, 'my_summary': ''}})


if __name__ == '__main__':
    print('正在生成摘要...')
    begin = time.time()
    text_list = [i['article'] for i in links.find()]
    id_list = [i['_id'] for i in links.find()]
    pool = ProcessingPool()
    pool.map(gen_summary, text_list, id_list)
    end = time.time() - begin
    print('摘要生成完毕，耗时：')
    print(end)
