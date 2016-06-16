conf=${1:-scrapy_examples}
scrapy crawl -L INFO general_spider -a conf_module=$conf
