# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class WuyouPipeline(object):
    def process_item(self, item, spider):
        f = open('zp.csv', 'a+', encoding='utf-8', newline='')
        writer = csv.writer(f)
        writer.writerow(
            [item['title'], item['money'], item['company'], item['detail'], item['advantage'],item['company_detail'],item['position']])
        f.close()

        return item
