# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from newscrawlers.items import NewsCrawlersItem as Item

def stripjoin(arr):
    return (" ".join(arr)).strip()
class LentaSpider(CrawlSpider):
    name = 'lenta.ru'
    news_re =r'.*\/news\/.*'
    allowed_domains = ['lenta.ru']
    start_urls = ['http://lenta.ru']

    rules = (
        Rule(LinkExtractor(allow=(r'.*', ), deny=(news_re, ))),

        Rule(LinkExtractor(allow=(news_re,)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = Item()
        item['title'] = stripjoin(response.xpath('//h1/text()').extract())
        item['text'] = stripjoin(response.xpath("//div[@itemprop='articleBody']/p/text()").extract())
        main_tag = stripjoin(response.xpath("//a[@class='b-header-inner__block']/text()").extract())
        second_tag = stripjoin(response.xpath("//a[@class='item dark active']/text()").extract())
        item['tags'] = [main_tag, second_tag]
        item['url'] = response.url
        item['spider_name'] = self.name 
        item['_id'] = response.url
        return item
