# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WanfangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    C_title = scrapy.Field()#中文标题
    E_title = scrapy.Field()#英文标题
    link = scrapy.Field()#链接
    C_author = scrapy.Field()#作者姓名 中文
    E_author = scrapy.Field()#作者姓名 英文
    periodical = scrapy.Field()#期刊名称
    abstract = scrapy.Field()#摘要 中文
    keywords = scrapy.Field()#关键字 中文
    time = scrapy.Field()#出版日期
    fund = scrapy.Field()#基金项目
    pass
