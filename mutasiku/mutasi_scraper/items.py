# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class IdIbankingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def replace(value):
    return value.strip().replace('\xa0', ' ')


class IbMandiriBallance(scrapy.Item):
    ballance = scrapy.Field(
        input_processor=MapCompose(replace),
        output_processor=TakeFirst()
    )


class IbMandiriSentence(scrapy.Item):
    spider = scrapy.Field()
    ballance = scrapy.Field()
    hash_id = scrapy.Field()
    tanggal = scrapy.Field(
        output_processor=TakeFirst()
    )
    keterangan = scrapy.Field(
        output_processor=Join('\n')
    )
    keluar = scrapy.Field(
        output_processor=TakeFirst()
    )
    masuk = scrapy.Field(
        output_processor=TakeFirst()
    )
