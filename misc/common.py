

from collections import OrderedDict

# Make sure css rules have only one root.
def bigitem_to_items(item):
    items = []

    for k, v in OrderedDict(item).items():
        for d in v:
            # print type(d), d
            oi = OrderedDict(d).items()
            # info(oi)
            li = {k1: '|'.join(v1) for k1, v1 in oi}
            # line = '\t'.join(li[-1:]) + '\n'
            item = li
            items.append(item)
    return items