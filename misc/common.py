

from collections import OrderedDict
from misc.log import *

# Make sure css rules have only one root.
def extract_items_from_list(list_item):
    items = []

    for k, v in list_item.items():
        for d in v:
            # print type(d), d
            oi = OrderedDict(d).items()
            # info(oi)
            li = {k1: '|'.join(v1) for k1, v1 in oi}
            # line = '\t'.join(li[-1:]) + '\n'
            item = li
            items.append(item)
    return items


# Make sure css rules have only one root.
def process_items_from_list(list_item, func):
    items = []

    for k, v in list_item.iteritems():
        for d in v:
            # print type(d), d
            # oi = d.items()
            info(d)
            func(d)
            # info(oi)
            # li = {k1: '|'.join(v1) for k1, v1 in oi}
            # line = '\t'.join(li[-1:]) + '\n'
            # item = li
            # items.append(item)
    return items