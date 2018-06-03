import scrapy

class TestSpider(scrapy.Spider):
    name = 'test_spider'

    def __init__(self, company):
        sites = {
            'costco': 'https://www.costco.com/grocery-household.html?dept=Grocery&keyword=beans',
            'amazon': 'https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16310101%2Ck%3A&keywords=salsa'
        }
        self.start_urls = [sites[company]]
        self.filename = company
        print('../../test/responses/%s.html' % self.filename)

    def response_is_ban(self, request, response):
        return b'banned' in response.body

    def exception_is_ban(self, request, exception):
        return None

    def parse(self, response):
        filepath = '../../test/responses/%s.html' % self.filename
        html_file = open(filepath, 'w')
        html_file.write(response.body.decode("utf-8"))
        print('response from %s recorded in /test/responses/' % response.url)
