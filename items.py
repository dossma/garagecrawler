# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GaragecrawlerItem(scrapy.Item):
    target_url = scrapy.Field()
    referer_url = scrapy.Field()
    depth = scrapy.Field()
    domain = scrapy.Field()

