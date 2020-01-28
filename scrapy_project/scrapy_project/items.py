# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    category = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    sizes = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
