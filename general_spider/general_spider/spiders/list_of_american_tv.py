
from BasicSpiderConfig import ExRule

class Config:

    # ExRule(start_urls[0], list_css_rules=list_css_rules)
    list_css_rules = {'dd': {'name': 'a::text'}}

    name='w'
    allowed_domains=['mianbao99.com']
    start_urls=[
        'http://www.mianbao99.com/occident/'
    ]

    ex_rules = [ExRule(start_urls[0] + '$', list_css_rules=list_css_rules)]

    follow = False
