# -*- coding: utf-8 -*-
import scrapy
import json
from newsqq.items import NewsqqItem


class LinksSpiderSpider(scrapy.Spider):
    name = 'links_spider'

    def __init__(self):
        # 需要爬取的链接
        self.links = []
        with open('links.txt', 'rt') as f:
            for line in f:
                self.links.append(line.strip())
        print(len(self.links))
        self.num = 0
        self.limit_num = len(self.links)

        s_url = self.links[self.num].split(',')[2]
        self.start_urls = [s_url]  # 入口链接
        print(s_url)

    def parse(self, response):
        print(response.request.headers['User-Agent'])
        news_data = json.loads(response.text)
        item_list = news_data['data']
        print(len(item_list))
        news = NewsqqItem()
        for item in item_list:
            news['category'] = self.links[self.num].split(',')[0]
            news['cate_en'] = self.links[self.num].split(',')[1]
            news['title'] = item['title']
            news['href'] = item['vurl']
            news['image'] = item['irs_imgs']['294X195'][0]
            news['article'] = 'none'
            news['introduce'] = item['intro']
            news['keywords'] = item['keywords']
            news['time'] = item['publish_time']
            news['source'] = item['source']
            yield news

        self.num += 1
        if self.num < self.limit_num:
            print(self.num)
            next_link = self.links[self.num].split(',')[2]
            print(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
