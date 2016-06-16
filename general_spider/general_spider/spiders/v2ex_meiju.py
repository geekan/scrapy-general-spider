
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '.reply_content': {
            'content': '*::text'
        }   
    }

    posts = [
        'http://www.v2ex.com/t/285736',
        'http://www.v2ex.com/t/258331',
        'http://www.v2ex.com/t/216199',
        'http://www.v2ex.com/t/204079',
    ]

    # print('(' + '|'.join([post + '(\?p=[1-9]|.*)?$' for post in posts]) + ')')
    # ex_rule = ExRule('(' + '|'.join([post for post in posts]) + ')', list_css_rules=list_css_rules)
    ex_rules = [
        ExRule(post, list_css_rules=list_css_rules)
        for post in posts
    ]
    # ex_rule = ExRule('http://www.v2ex.com/t/204079.*?$', list_css_rules=list_css_rules)
    # ex_rules = [ex_rule]
    # print(ex_rules)

    name='v2ex'
    allowed_domains = ['www.v2ex.com']
    # start_urls = [post + '?p=1' for post in posts]
    start_urls = posts
    follow = False

