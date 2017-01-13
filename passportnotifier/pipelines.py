# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import logging
from scrapy.mail import MailSender

logger=logging.getLogger(__name__)


class PassportnotifierPipeline(object):
    def __init__(self, settings):
        self.data = {
            'result': {
                u'./t1203113.htm': u'(2014-10-23)',
                u'./t1218764.htm': u'(2014-12-12)',
                u'./t1253051.htm': u'(2015-04-08)',
                u'./t1288968.htm': u'(2015-08-15)',
                u'./t1321069.htm': u'(2015-12-04)',
                u'./t1327029.htm': u'(2015-12-23)',
                u'./t1332058.htm': u'(2016-01-15)',
                u'./t1339882.htm': u'(2016-02-11)',
                u'./t1346149.htm': u'(2016-03-08)',
                u'./t1353931.htm': u'(2016-04-07)',
                u'./t1361195.htm': u'(2016-05-06)',
                u'./t1371654.htm': u'(2016-06-13)',
                u'./t1383779.htm': u'(2016-07-22)',
                u'./t1388896.htm': u'(2016-08-13)',
                u'./t1397571.htm': u'(2016-09-14)',
                u'./t1397572.htm': u'(2016-09-14)',
                u'./t1406897.htm': u'(2016-10-18)',
                u'./t1414860.htm': u'(2016-11-12)',
                u'./t1423526.htm': u'(2016-12-13)',
                u'./t712286.htm': u'(2010-05-25)',
                u'./t765259.htm': u'(2014-07-29)',
                }
            }

        # self.mailer = MailSender.from_settings(settings)
        # self.mailto=settings.get('MAIL_TO')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_item(self, item, spider):
        if item != self.data:
            logger.info("page updated!")
            # self.mailer.send(to=[self.mailto], subject="passport updated", body="please take a look")
        else:
            logger.info("no update detected on the page")
        return item
