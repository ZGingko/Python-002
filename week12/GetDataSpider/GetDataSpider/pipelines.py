# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
import pandas as pd
from snownlp import SnowNLP

from GetDataSpider.config import common
from GetDataSpider.items import CommentItem


class GetdataspiderPipeline:
    def process_item(self, item, spider):
        return item


class PhonePipeline:
    def process_item(self, item, spider):
        return item


class CommentPipeline:
    def open_spider(self, spider):
        self.db_conn = pymysql.connect(**common.DATABASE)
        db_cur = self.db_conn.cursor()
        try:
            db_cur.execute(common.SQL_DELETE_TABLE)
            db_cur.execute(common.SQL_CREATE_TABLE)
            db_cur.close()
        except Exception as e:
            print(e)
            self.db_conn.rollback()

    def process_item(self, item, spider):
        if spider.name != 'phone':
            return item
        phone = item['phone']
        alink = item['alink']
        user_comment = item['user_comment']
        print(phone, "\t", len(user_comment))
        for user, comment in user_comment:
            try:
                sentiments = SnowNLP(comment).sentiments
            except:
                sentiments = 0.5
            try:
                db_cur = self.db_conn.cursor()
                db_cur.execute(
                    common.SQL_INSERT.format(
                        phone,
                        alink,
                        user,
                        comment,
                        sentiments
                    )
                )
                db_cur.close()
            except Exception as e:
                print("???", e)
                self.db_conn.rollback()
        return item

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()
