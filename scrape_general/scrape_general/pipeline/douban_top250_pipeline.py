# -*- coding: utf-8 -*-

# Define your item pipeline here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrape_general.settings import mongo_host, mongo_port
from scrape_general.setting.douban_top250_settings import mongo_db_name, mongo_db_collection
from scrape_general.util.mongo_db_helper import MongoDBHelper


class ScrapeGeneralPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection

        self.post = MongoDBHelper(sheetname, dbname, host, port)

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert_item(data)
        return item
