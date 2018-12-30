# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsqqItem(scrapy.Item):
    cate_en = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    image = scrapy.Field()
    article = scrapy.Field()
    introduce = scrapy.Field()
    keywords = scrapy.Field()
    time = scrapy.Field()
    source = scrapy.Field()
    second_article = scrapy.Field()
