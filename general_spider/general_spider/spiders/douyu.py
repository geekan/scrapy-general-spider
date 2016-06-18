
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '#live-list-contentbox li': {
            'url': 'a::attr(href)',
            'room_name': 'a::attr(title)',
            'tag': 'span.tag.ellipsis::text',
            'people_count': '.dy-num.fr::text'
        }
    }

    ex_rule = ExRule('http://www.douyu.com/all$', list_css_rules=list_css_rules)

    name='douyu.com'
    allowed_domains=['douyu.com']
    start_urls=['http://www.douyu.com/all']
    ex_rules = []
    follow = False

