
from BasicSpiderConfig import ExRule

class Config:

    list_css_rules = { 
        '.reply_content': {
            'content': '*::text'
        }   
    }

    posts = [
        'http://www.v2ex.com/t/247764',
        'http://www.v2ex.com/t/217281',
        'http://www.v2ex.com/t/215851',
        'http://www.v2ex.com/t/231248',
        'http://www.v2ex.com/t/239288',
        'http://www.v2ex.com/t/208278',
        'http://www.v2ex.com/t/223010',
    ]

    # print('(' + '|'.join([post + '(\?p=[1-9]|.*)?$' for post in posts]) + ')')
    # ex_rule = ExRule('(' + '|'.join([post for post in posts]) + ')', list_css_rules=list_css_rules)
    ex_rules = [
        ExRule(post + '\?p=[2-9]', list_css_rules=list_css_rules)
        for post in posts
    ]
    # ex_rule = ExRule('http://www.v2ex.com/t/204079.*?$', list_css_rules=list_css_rules)
    # ex_rules = [ex_rule]
    # print(ex_rules)
    # ex_rules = []

    name='v2ex'
    allowed_domains = ['www.v2ex.com']
    # start_urls = [post + '?p=1' for post in posts]
    start_urls = posts
    follow = False

