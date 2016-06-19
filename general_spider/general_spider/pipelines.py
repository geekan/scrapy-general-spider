# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis


from scrapy import signals


import json
import codecs
from collections import OrderedDict
import MySQLdb


# Make sure css rules have only one root.
def bigitem_to_items(item):
    items = []
    for k, v in OrderedDict(item).items():
        for d in v:
            # print type(d), d
            li = ['|'.join(v1) for k1, v1 in OrderedDict(d).items()]
            # line = '\t'.join(li[-1:]) + '\n'
            item = li
            items.append(item)
    return items


class TXTWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.txt', 'w', encoding='utf-8')

    # process big item as default.
    def process_item(self, item, spider):
        items = bigitem_to_items(item)
        for li in items:
            line = '\t'.join(li) + '\n'
            self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class RedisPipeline(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379)

    def process_item(self, item, spider):
        if not item['id']:
            print 'no id item!!'

        str_recorded_item = self.r.get(item['id'])
        final_item = None
        if str_recorded_item is None:
            final_item = item
        else:
            ritem = eval(self.r.get(item['id']))
            final_item = dict(item.items() + ritem.items())
        self.r.set(item['id'], final_item)
        return item

    def close_spider(self, spider):
        return


class MySQLStorePipeline(object):
  def __init__(self):
    # self.conn = MySQLdb.connect(user='user', 'passwd', 'dbname', 'host', charset="utf8", use_unicode=True)
    self.conn = MySQLdb.connect(user='root', passwd='', db='live_portal', host='localhost', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        items = bigitem_to_items(item)
        try:
            self.cursor.execute("""INSERT INTO live_rooms (author, tag, room_name, url, people_count)
                            VALUES (%s, %s, %s, %s, %s)""",
                           (
                               item['author'].encode('utf-8'),
                               item['tag'].encode('utf-8'),
                               item['room_name'].encode('utf-8'),
                               item['url'].encode('utf-8'),
                               item['people_count'].encode('utf-8'),
                            )
            )

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item

