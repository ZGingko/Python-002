# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetdataspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CommentItem(scrapy.Item):
    phone = scrapy.Field()
    alink = scrapy.Field()
    user_comment = scrapy.Field()
