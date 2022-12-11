# -*- coding: utf-8 -*-
import scrapy


class YuanfespiderSpider(scrapy.Spider):
    name = 'yuanfespider'
    allowed_domains = ['http://shop.yuanfa.de/']
    start_urls = ['http://shop.yuanfa.de/']

    def parse(self, response):
        print('output')
        categories =
        pass
