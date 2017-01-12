# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PassportnotifierPipeline(object):
    def __init__(self):
        self.date_seen = set()

    def process_item(self, item, spider):
        print '*'*6
        print item
