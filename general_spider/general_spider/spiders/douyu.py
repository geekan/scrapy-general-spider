
from BasicSpiderConfig import ExRule
from collections import OrderedDict
from misc.common import *
from misc.log import *

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

    def preprocess_item(self, item):
        oi = OrderedDict(item)
        items = bigitem_to_items(oi)
        info('## preprocess_item')
        info(len(oi))
        return oi