
from BasicSpiderConfig import ExRule

class Config:

    # ExRule(start_urls[0], list_css_rules=list_css_rules)
    list_css_rules = [{'i': {'name': 'a::text'}}, {'#mw-content-text li': {'name': 'a::text'}}]

    name='w'
    allowed_domains=['wikipedia.org']
    start_urls=[
        'https://en.wikipedia.org/wiki/List_of_American_television_series', 
        'https://zh.wikipedia.org/wiki/%E7%BE%8E%E5%9B%BD%E7%94%B5%E8%A7%86%E5%89%A7%E5%88%97%E8%A1%A8'
    ]

    ex_rules = [ExRule(start_urls[0], list_css_rules=list_css_rules[0]),
                ExRule(start_urls[1], list_css_rules=list_css_rules[1])]

    follow = False
