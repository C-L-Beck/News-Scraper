# -*- coding: utf-8 -*
import scrapy
import pandas as pd
import numpy as np
from scrapy.crawler import CrawlerProcess

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['http://www.reddit.com/r/CryptoCurrency/']
    start_urls = ['http://www.reddit.com/r/CryptoCurrency/']

    custom_settings = {
    'FEED_FORMAT' :  'csv' ,
    'FEED_URI' : 'file:///C:\Users\surfacepro3\Desktop\ProvingGround/redditbot.csv'}

    def parse(self, response):
        #Extract
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css("time::text").extract()
        comments = response.css('.comments::text').extract()
        url = response.css('.bylink.comments.may-blank::attr(href)').extract()

        for item in zip(titles, votes, times, comments, url):
            #dict
            redditdata = {
                'title' : item[0],
                'votes' : item[1],
                'time' : item[2],
                'comments' : item[3],
                'url' : item[4],

            }

            yield redditdata
        pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(RedditbotSpider)
process.start() # the script will block here until the crawling is finished
