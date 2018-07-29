# -*- coding: utf-8 -*-
import scrapy
from newsqq.items import NewsqqItem
# 需要爬取的类型和链接
type_links = []
with open('type_links.txt', 'rt') as f:
    for line in f:
        type_links.append(line.strip())
print(len(type_links), type_links)
num = 0
limit_num = len(type_links)


class LinksSpiderSpider(scrapy.Spider):
    name = 'links_spider'
    allowed_domains = ['new.qq.com']
    start_urls = ['https://new.qq.com/']

    def parse(self, response):
        global num
        global type_links
        global limit_num
        print(response.request.headers['User-Agent'])
        item_list = response.xpath("//li[@class='item cf']")
        print(len(item_list))
        news = NewsqqItem()
        for item in item_list:
            news['category'] = type_links[num].split('，')[0]
            news['title'] = item.xpath(".//em[@class='f14 l24']/a/text()").extract_first()
            news['href'] = item.xpath(".//div[@class='detail']/h3/a/@href").extract_first()
            news['image'] = item.xpath(".//img[@class='picto']/@src").extract_first()
            yield news
        num += 1

        if num < limit_num:
            next_link = type_links[num].split('，')[1]
            print(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
