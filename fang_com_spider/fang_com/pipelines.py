# -*- coding: utf-8 -*-
from pymongo import MongoClient

# # 链接数据库
# client = MongoClient(host='127.0.0.1', port=27017)
# db = client["fang"]
import csv
class FangComPipeline:
    def process_item(self, item, spider):
        # '''这里保存数据,我是保存到MongoDB里'''
        # db.fang_date.insert_one(dict(item))
        # print(item)
        # return item

        # f = open('fang.csv', 'a+', encoding='utf-8', newline='')
        # writer = csv.writer(f)
        # writer.writerow(
        #     # [item['title'], item['type'], item['address'], item['advantage'], item['total_price'],
        #     #  item['price'], item['detail_url']]
        #     [item['title'],item['comment_num'], item['type'], item['address'], item['status'], item['house_title'], item['price'],
        #              item['tel'], item['detail_url']]
        #   )
        # f.close()

        f = open('zf.csv', 'a+', encoding='utf-8', newline='')
        writer = csv.writer(f)
        writer.writerow(
            # [item['title'], item['type'], item['address'], item['advantage'], item['total_price'],
            #  item['price'], item['detail_url']]
            [item['title'],item['type'], item['address'], item['distance'], item['price'],
             item['advantage']]
        )
        f.close()
        return item

    # def esf_item(self, item, spider):
    #     f = open('esf.csv', 'a+', encoding='utf-8', newline='')
    #     writer = csv.writer(f)
    #     writer.writerow(
    #         [item['title'], item['type'], item['addres'], item['status'], item['house_title'], item['price'],
    #          item['tel'], item['detail_url']])
    #     f.close()
    #     return item