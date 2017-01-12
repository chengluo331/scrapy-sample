# -*- coding: utf-8 -*-
import re
import scrapy


class PassportspiderSpider(scrapy.Spider):
    name = "passportspider"
    start_urls = ['http://www.chinese-embassy.org.uk/chn/lsfw/hzlxz/hzlxz/']

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

        yield {
            'result': result
        }
