# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# import requests
import json


class WuyouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WuyouDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
        '''在这里设置代理ip跟随机请求头'''
        # 随机请求头
        ua = random.choice(spider.settings.get("UA_LIST"))
        request.headers["User-Agent"] = ua

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        '''可以查看请求头有没有设置成功'''
        #print(request.headers["User-Agent"])
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


#代理ip
# class ChangeProxy(object):
#     def __init__(self):
#         # self.get_url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=be36e0a411c546d8a5fb38bb26ff43fe&orderno=YZ20173293618kDUVrD&returnType=2&count=10"
#         self.get_url = "https://ape.vip/T-000001"
#         self.tmp_url = "http://ip.chinaz.com/getip.aspx"
#         self.ip_list = []
#         self.count = 0
#         self.evecount = 0
#
#     def getIPData(self):
#         temp_data = requests.get(url=self.get_url).text
#         self.ip_list.clear()
#         for eve_ip in json.loads(temp_data)["RESULT"]:
#             print(eve_ip)
#             self.ip_list.append({
#                 "ip": eve_ip["ip"],
#                 "port": eve_ip["port"]
#             })
#
#     def changeProxy(self, request):
#         request.meta["proxy"] = "http://" + str(self.ip_list[self.count-1]["ip"]) + ":" + \
#                                 str(self.ip_list[self.count-1]["port"])
#
#     def yanzheng(self):
#         requests.get(url=self.temp_url, proxies={"http":str(self.ip_list[self.count-1]["ip"]) + ":" +
#                                                        str(self.ip_list[self.count-1]["port"])}, timeout=5)
#
#     def ifUsed(self,request):
#         try:
#             self.changeProxy(request)
#             self.yanzheng()
#         except:
#             if self.count == 0 or self.count == 10:
#                 self.getIPData()
#                 self.count = 1
#             self.count = self.count + 1
#             self.ifUsed(request)
#
#     def process_request(self, request, spider):
#
#         if self.count == 0 or self.count == 10:
#             self.getIPData()
#             self.count = 1
#
#         if self.evecount == 80:
#             self.count = self.count + 1
#             self.evecount = 0
#         else:
#             self.evecount = self.evecount + 1
#
#         self.ifUsed(request)
