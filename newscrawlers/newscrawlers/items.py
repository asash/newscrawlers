# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsCrawlersItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
    spider_name = scrapy.Field()
