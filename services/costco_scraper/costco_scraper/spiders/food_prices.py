import scrapy
import json

class FoodPricesSpider(scrapy.Spider):
    name = "food_prices"

    def get_urls(self):
        text_file = open("../../data/food_list.txt", "r")
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
        results = [{'name': name, 'price': price, 'seller': 'costco'} for i, (name, price) in enumerate(associated)]

        with open('../../data/costco_results.json', 'a') as outfile:
            json.dump(results, outfile)
