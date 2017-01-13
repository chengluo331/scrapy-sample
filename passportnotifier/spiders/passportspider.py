# -*- coding: utf-8 -*-
import re
import scrapy


class PassportspiderSpider(scrapy.Spider):
    name = "passportspider"
    start_urls = ['http://www.chinese-embassy.org.uk/chn/lsfw/hzlxz/hzlxz/']

    data = {
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
        u'./t765259.htm': u'(2014-07-29)'
        }

    def parse(self, response):
        result={}
        for title in response.css('#docMore .title'):
            ref = title.css('a::attr(href)').extract_first()
            items = title.css('td::text').extract()
            d='unknown'
            for item in items:
                match = re.match(u'.(\d+\-\d+\-\d+).', item)
                if match:
                    d=match.group(0)
                    break
            result[ref]=d

        if result!=PassportspiderSpider.data:
            yield {'result': result}
