
from BasicSpiderConfig import ExRule

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

