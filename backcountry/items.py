# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BackcountryItem(Item):
    # define the fields for your item here like:
    brand = Field() #Brand name
    product_name = Field() #Product name
    #product_id = scrapy.Field() #Product id
    price = Field() #Product price
    low_price = Field() #Current price if on sale
    high_price = Field() #Previous price if on sale
    href = Field() #Product link
