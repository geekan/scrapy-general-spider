
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '.video-list-item.video-no-tag': {
            'room_name': '.video-title::text',
            'anchor': '.video-nickname::text',
            'audience_count': '.video-number::text',
            'tag': '.video-cate::text',
            'url': 'a::attr(href)',
            'platform': ['pandatv'],
            'platform_prefix_url': ['http://www.panda.tv/'],
        }   
    }

    ex_rule = ExRule('http://www.panda.tv/all$', list_css_rules=list_css_rules)

    name='pandatv'
    allowed_domains=['panda.tv']
    start_urls=['http://www.panda.tv/all']
    ex_rules = []
    follow = False

