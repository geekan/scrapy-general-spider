
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '.reply_content': {
            'content': '*::text'
        }   
    }

    ex_rule = ExRule('http://www.v2ex.com/t/285736\?p=[1-9]$', list_css_rules=list_css_rules)

    name='v2ex'
    allowed_domains=['www.v2ex.com']
    start_urls=['http://www.v2ex.com/t/285736?p=1']
    ex_rules = [ex_rule]
    follow = False

