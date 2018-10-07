import pymongo
import os

client = pymongo.MongoClient('localhost', 27017)
newsQQDB = client['newsQQDB']
links = newsQQDB['links']
article = newsQQDB['article']
cate = newsQQDB['cate']


if __name__ == '__main__':
    links.remove()
    article.remove()
    cate.remove()
    print('已清空数据库，开始运行程序')

    print('生成需获取的所有页面链接')
    os.system('python genLinks.py')

    print('获取所有页面的新闻链接及相关信息')
    os.system('scrapy crawl links_spider')

    print('获取所有新闻的正文')
    os.system('python autoRestart.py')

    print('文章正文获取完毕！正在更新数据库...')
    os.system('python linksAndArticleToExcel.py')
    print('已导出')
