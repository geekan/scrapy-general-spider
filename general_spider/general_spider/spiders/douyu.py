#coding: utf-8

from BasicSpiderConfig import ExRule
from collections import OrderedDict
from misc.common import *
from misc.log import *
import re

class Config:

    list_css_rules = { 
        '#live-list-contentbox li': {
            'url': 'a::attr(href)',
            'room_name': 'a::attr(title)',
            'tag': 'span.tag.ellipsis::text',
            'audience_count': '.dy-num.fr::text',
            'anchor': '.dy-name::text',
            'platform': ['douyu'],
            'platform_prefix_url': ['http://www.douyu.com/'],
        }
    }

    ex_rule = ExRule('http://www.douyu.com/all$', list_css_rules=list_css_rules)

    name='douyu.com'
    allowed_domains=['douyu.com']
    start_urls=['http://www.douyu.com/directory/all']
    ex_rules = []
    follow = False

    @staticmethod
    def deal_human_readable_numbers(hrn=''):
        numbers = re.findall(r'\d+\.?\d*', hrn)
        if len(numbers) == 0:
            return 0
        elif len(numbers) > 1:
            warn('suspect numbers:'+str(numbers))

        number = float(numbers[0])

        # FIXME magic logic. Consider to add log here.
        if hrn.endswith(u'万'):
            number = (number * 10000.0)
        return str(int(number))

    # Note that if not force 1 item, item['audience_count'] would contain a list.
    @staticmethod
    def update_audience_count(item):
        if type(item['audience_count']) != list:
            return

        audience_count = [Config.deal_human_readable_numbers(i) for i in item['audience_count']]
        item['audience_count'] = audience_count

    @staticmethod
    def preprocess_item(list_item):
        oi = OrderedDict(list_item)

        process_items_from_list(oi, Config.update_audience_count)

        # for item in items:
            # audience_count = Config.deal_human_readable_numbers(item['audience_count'])
            # print(item['url'], item['audience_count'], audience_count)
            # item['audience_count'] = audience_count
            # info(item)

        # info('------------------')
        # info(items)
        info('------------------')
        info(oi)

        info('## preprocess_item')
        # info(len(oi))
        return oi