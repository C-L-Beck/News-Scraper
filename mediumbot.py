# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import numpy as np
from scrapy.crawler import CrawlerProcess

class MediumbotSpider(scrapy.Spider):
    name = 'mediumbot'
    allowed_domains = ['https://medium.com/tag/cryptocurrency']
    start_urls = ['https://medium.com/tag/cryptocurrency/']

    custom_settings = {
    'FEED_FORMAT' :  'csv' ,
    'FEED_URI' : 'file:///C:\Users\surfacepro3\Desktop\ProvingGround/mediumbot.csv'}

    def parse(self, response):
        #Extract
        titles = response.css("h3::text").extract()
        times = response.css("time::text").extract()
        url = response.css(".button.button--smaller.button--chromeless.u-baseColor--buttonNormal::attr(href)").extract()

        for item in zip(titles, times, url):
            #dict
            mediumdata = {
                'title' : item[0],
                'time' : item[1],
                'url' : item[2],
            }

            yield mediumdata

            pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MediumbotSpider)
process.start() # the script will block here until the crawling is finished
