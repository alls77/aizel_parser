# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from django_app.tasks import save_to_db
from django_app.signals import data_saved


class ScrapyProjectPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item._values)
        if len(self.items) >= 200:
            save_to_db.delay(self.items)
            self.items.clear()
            data_saved.send(sender="parser", status="get first 200")
        return item

    def close_spider(self, spider):
        if self.items:
            save_to_db.delay(self.items)
            self.items.clear()
        data_saved.send(sender="parser", status="finished")


