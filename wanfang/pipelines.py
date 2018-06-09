# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import mysql.connector
import sqlite3
class WanfangPipeline(object):



    #conn = mysql.connector.connect(user='root', password='', database='db1')
    #cursor = conn.cursor()
    # 创建user表:
    #cursor.execute('create table wanfang (id varchar(20) primary key, c_title TEXT, e_title TEXT, link TEXT, c_author TEXT, e_author TEXT, periodical TEXT, abstract TEXT, keywords TEXT, time VARCHAR(250), fund TEXT )')

    def open_spider(self, spider):
        self.con = sqlite3.connect("wanfang.sqlite")  # 链接数据库
        self.cu = self.con.cursor()

    def __init__(self):
        self.count = 0
        self.paper = 0
        self.name = 'TCM.txt'
    def process_item(self, item, spider):
        a = json.dumps(dict(item), ensure_ascii = False)
        print(a)
        if self.count % 10000 == 0:
            print("-------------------"*10)
            self.paper += 1
        with open("./data1/d" + str(self.paper) + self.name, "a", encoding='utf8' ) as f:
            f.write(a)
            f.write("\n")
            f.close()
        self.count += 1
        print(self.count,"**"*20)
        print(spider.name,'pipelines')
        insert_sql = "insert into wanfang (c_title, e_title, link, c_author, e_author, periodical, abstract, keywords, time, fund ) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(item['C_title'],
                                                                                                           item['E_title'],
                                                                                                           item['link'],
                                                                                                           item['C_author'],
                                                                                                           item['E_author'],
                                                                                                           item['periodical'],
                                                                                                           item['abstract'],
                                                                                                           item['keywords'],
                                                                                                           item['time'],
                                                                                                           item['fund'],
                                                                                                                        )
        #insert_sql2 = "insert into cnki (c_title, e_title, link, c_author, e_author, periodical, abstract, keywords, time, fund ) values('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')"
        print(insert_sql)
        #print(item[E_title])
        #print(insert_sql2)
        #self.cu.execute(insert_sql2)
        self.cu.execute(insert_sql)
        #self.cu.execute(insert_sql2)
        self.con.commit()
        return item
    def spider_close(self, spider):
        self.con.close()