# -*- coding: utf-8 -*-
import scrapy
import json
from newsqq.items import NewsqqItem

# 需要爬取的链接
links = []
with open('links.txt', 'rt') as f:
    for line in f:
        links.append(line.strip())
print(len(links))
num = 0
limit_num = len(links)


class LinksSpiderSpider(scrapy.Spider):
    name = 'links_spider'
    s_url = links[num].split('，')[2]
    start_urls = [s_url]
    print(s_url)

    def parse(self, response):
        global num, links, limit_num
        print(response.request.headers['User-Agent'])
        news_data = json.loads(response.text)
        item_list = news_data['data']
        print(len(item_list))
        news = NewsqqItem()
        for item in item_list:
            news['category'] = links[num].split('，')[0]
            news['cate_en'] = links[num].split('，')[1]
            news['title'] = item['title']
            news['href'] = item['vurl']
            news['image'] = item['img']
            news['article'] = 'none'
            news['introduce'] = item['intro']
            news['keywords'] = item['keywords']
            news['time'] = item['publish_time']
            news['source'] = item['source']
            yield news

        num += 1
        if num < limit_num:
            print(num)
            next_link = links[num].split('，')[2]
            print(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
