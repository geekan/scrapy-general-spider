import re
import json
from urlparse import urlparse
import urllib
import pdb


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle


from general_spider.items import *
from misc.log import *
from misc.spider import CommonSpider


import BasicSpiderConfig


class general_spiderSpider(CommonSpider):
    name = 'general_spider'
    list_css_rules = {}

    def __init__(self, conf_module='TestSpiderConfig', *args, **kwargs):
        if conf_module.endswith(".py"):
            conf_module = conf_module[:-3]
        cm  = __import__(conf_module, globals=globals())
        conf = cm.Config()
        self.name = conf.name
        self.allowed_domains = conf.allowed_domains
        self.start_urls = conf.start_urls
        self.list_css_rules = conf.list_css_rules
        self.rules = [Rule(sle(allow=(c.allowed_rule_regex)), callback='parse_1', cb_kwargs=c.paras, follow=conf.follow) for c in conf.ex_rules]
        self.conf = conf

        info(self.start_urls)
        info(self.rules)
        info([[c.allowed_rule_regex, c.paras] for c in conf.ex_rules])
        # import pdb; pdb.set_trace()
        super(general_spiderSpider, self).__init__(*args, **kwargs)

    def parse_1(self, response, list_css_rules):
        info('---------------------')
        info('Parse '+response.url)
        info('list_css_rules:')
        info(list_css_rules)
        x = self.parse_with_rules(response, list_css_rules, dict)

        # info(x)
        preprocess_item = getattr(self.conf, "preprocess_item", None)
        if callable(preprocess_item):
            for item in x:
                preprocess_item(item)

        # x = self.parse_with_rules(response, self.content_css_rules, dict)
        # print(json.dumps(x, ensure_ascii=False, indent=2))
        # pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, general_spiderItem)
        return x

    def parse_start_url(self, response):
        if type(self.list_css_rules) != dict:
            return
        return self.parse_1(response, self.list_css_rules)

