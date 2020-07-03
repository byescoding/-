

from scrapy import signals
import random  # 用来设置随机的头跟ip


class FangComSpiderMiddleware:
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

# 下载中间件
class FangComDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 这是我弄得，其他的默认没动
    def process_request(self, request, spider):
        '''在这里设置代理ip跟随机请求头'''
        # 随机请求头
        ua = random.choice(spider.settings.get("UA_LIST"))
        request.headers["User-Agent"] = ua


    def process_response(self, request, response, spider):
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
class ProxyMiddleware(object):
    Proxy = [
       '123.134.231.245:36514',
       '175.146.70.245:43963',
        '171.43.16.66:34873',
        '223.214.29.235:14609',
        '42.59.103.69:10893',
        '123.149.141.224:44032',
        '117.95.201.13:12001',
        '113.121.171.88:25309',
        '115.151.129.69:31998',
        '183.148.128.177:19891',
        '27.44.203.227:19959',
        '202.101.232.191:16241',
        '113.117.120.17:15135',
        '111.77.197.251:20510',
        '58.52.112.166:18404',
        '113.74.62.243:49177',
        '42.242.10.9:31012',
       '123.163.27.219:38767',
        '140.224.129.65:37381',
        '27.42.139.89:18914',
        '111.178.87.173:20777',
        '222.163.221.29:15236',
        '58.50.2.159:45275',
        '60.176.234.205:11357',
        '115.230.61.196:27076',
        '58.52.114.26:12469',
        '112.91.78.187:44999',
        '59.62.33.57:20213',
        '113.226.96.64:49435',
        '60.176.236.248:18577',
        '49.84.40.110:47249',
        '59.62.206.196:22340',
        '121.224.84.240:47444',
        '117.92.154.71:28652',
        '223.199.18.229:46019',
        '115.213.225.100:23138',
        '49.72.142.90:34754',
        '111.227.41.44:10778',
        '58.52.115.93:15925',
        '180.120.210.57:32174',
        '36.62.112.117:40766',
        '218.95.51.226:22174',
        '111.178.90.142:22099',
        '27.22.133.244:44145',
        '111.177.186.246:37692',
        '27.152.194.227:49612',
        '119.85.12.168:25814',
        '113.110.63.237:10245',
        '113.238.104.198:31308',
        '1.59.99.9:40912',
    ]


    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://' + random.choice(self.Proxy)
        print(random.choice(self.Proxy))

