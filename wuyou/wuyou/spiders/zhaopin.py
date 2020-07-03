# -*- coding: utf-8 -*-
import scrapy
# import json
from wuyou.items import WuyouItem
# import re
from scrapy_redis.spiders import RedisSpider
class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,01,9,99,%2520,2,1.html']
    # redis_key = "zhaopin_url"

    def parse(self, response):
        urls=response.xpath('//div[@class="el"]')
        for url in urls:
            href = url.xpath('./p[contains(@class,"t1")]/span/a/@href').get()
            if href is not None:
                # print(href)
                yield scrapy.Request(url=href, callback=self.parseDetail)

        next_url = response.xpath('//a[text()="下一页"]/@href').get()
        if next_url is not None and next_url != "javascript:void(0)":
            # 在这里组合成完整链接，因为这里是已经过滤的了，能节省时间
            yield scrapy.Request(url=next_url, callback=self.parse)
        pass

#爬取详情页
    def parseDetail(self, response):
        item = WuyouItem()
        header_info=response.xpath('//div[@class="tHeader tHjob"]')
        title=header_info.xpath('//div[@class="cn"]/h1/@title').get()
        money=header_info.xpath('//div[@class="cn"]/strong/text()').get()
        company=header_info.xpath('//p[@class="cname"]/a/text()').get()
        detail=header_info.xpath('//p[@class="msg ltype"]/text()').getall()
        advantage=header_info.xpath('//div[@class="t1"]/span/text()').getall()
        company_detail=header_info.xpath('//div[@class="com_tag"]/p/@title').getall()
        position=header_info.xpath('//a[@class="el tdn"]/text()').getall()
        # detail = [re.sub(r'\s \xa0', '', i) for i in detail]  # 将\n\t等字符替换为空字符
        # detail = [i for i in detail if len(i) > 0]  # 去掉空字符
        item['title']=title
        item['money'] = money
        item['company'] = company
        item['detail'] = detail
        item['advantage'] = advantage
        item['company_detail'] = company_detail
        item['position'] = position
        yield item

        pass

#只是爬取列表信息
    # print(response.xpath('//a[text()="下一页"]/@href'))
    # info_list=response.xpath('//div[@class="el"]')
    # # print(info_list)
    # item = WuyouItem()
    # for info in info_list:
    #     zhiwei=info.xpath('p/span/a/text()').get()
    #     # zhiwei = [re.sub(r'\s|/|－|\|', '', i) for i in zhiwei]
    #     # item["type"] = [i for i in zhiwei if len(i) > 0]  # 去掉空字符
    #     gs=info.xpath('span[@class="t2"]/a/text()').get()
    #     wz=info.xpath('span[@class="t3"]/text()').get()
    #     xz=info.xpath('span[@class="t4"]/text()').get()
    #     rq=info.xpath('span[@class="t5"]/text()').get()
    #     if zhiwei is not None and gs is not None and wz is not None and xz is not None and rq is not None:
    #         item['zhiwei']=zhiwei
    #         item['gongsi'] = gs
    #         item['didian'] = wz
    #         item['xinzi'] = xz
    #         item['jingyan'] = rq
    #         yield item
    # next_url = response.xpath('//a[text()="下一页"]/@href').get()
    # print(next_url)
    # if next_url is not None and next_url != "javascript:void(0)":
    #     # 在这里组合成完整链接，因为这里是已经过滤的了，能节省时间
    #     yield scrapy.Request(url=next_url, callback=self.parse)




