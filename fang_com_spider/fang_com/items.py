# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangComItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # title = scrapy.Field()
    # comment_num=scrapy.Field()
    # type = scrapy.Field()
    # address = scrapy.Field()
    # status = scrapy.Field()
    # house_title = scrapy.Field()
    # price = scrapy.Field()
    # tel = scrapy.Field()
    # detail_url = scrapy.Field()

    # title = scrapy.Field()
    # type = scrapy.Field()
    # address = scrapy.Field()
    # advantage = scrapy.Field()
    # total_price = scrapy.Field()
    # price = scrapy.Field()
    # detail_url = scrapy.Field()

#租房
    title = scrapy.Field()
    type = scrapy.Field()
    # address = scrapy.Field()
    address = scrapy.Field()
    distance = scrapy.Field()
    price = scrapy.Field()
    advantage = scrapy.Field()

    pass
