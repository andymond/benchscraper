import scrapy
import datetime
import json

class CostcoSpider(scrapy.Spider):
    name = "costco_spider"

    def __init__(self, test=False):
        self.test = test

    def get_urls(self, file_path="./data/food_list.txt"):
        text_file = open(file_path, "r")
        params_list = text_file.read().splitlines()
        base_url = 'https://www.costco.com/grocery-household.html?dept=Grocery&keyword='
        urls = [base_url + param for param in params_list]

        return urls

    def response_is_ban(self, request, response):
        return b'banned' in response.body

    def exception_is_ban(self, request, exception):
        return None

    def start_requests(self):
        urls = self.get_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        names = response.xpath('//p[@class="description"]/a/text()').extract()
        prices = response.xpath('//div[@class="price"]/text()').extract()
        associated = list(zip(names, prices))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        results = [{'name': name, 'price': price, 'seller': 'costco', 'recorded_at': date} for i, (name, price) in enumerate(associated)]

        if self.test == False:
            with open('./data/costco_results.json', 'w') as file:
                json.dump(results, file)

        return results
