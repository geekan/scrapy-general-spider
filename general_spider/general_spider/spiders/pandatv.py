
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '.video-list-item.video-no-tag': {
            'room_name': '.video-title::text',
            'author': '.video-nickname::text',
            'people_count': '.video-number::text',
            'tag': '.video-cate::text',
        }   
    }

    ex_rule = ExRule('http://www.panda.tv/all$', list_css_rules=list_css_rules)

    name='pandatv'
    allowed_domains=['panda.tv']
    start_urls=['http://www.panda.tv/all']
    ex_rules = [ex_rule]
    follow = False

