import scrapy
import datetime
import json

class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"

    def __init__(self, test=False):
        self.test = test

    def get_urls(self, file_path="../../data/food_list.txt"):
        text_file = open(file_path)
        params_list = text_file.read().splitlines()
        base_url = "https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16310101%2Ck%3A&keywords="
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
        list = response.xpath('//ul[@id="s-results-list-atf"]/li').extract()
        names_and_prices = []
        for i, item in enumerate(list):
            id = '"result_%s"' % i
            name_xpath = '//*[@id=%s]/div/div[3]/div[1]/a/h2/@data-attribute' % id
            price_xpath = '//*[@id=%s]/div/div[4]/div[3]/a/span[1]/text()' % id
            name = response.xpath(name_xpath).extract_first()
            price = response.xpath(price_xpath).extract_first()
            if not (name is None) or ((name, price) in names_and_prices):
                names_and_prices.append((name, price))

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        results = [{'name': name, 'price': price, 'seller': 'amazon', 'recorded_at': date} for i, (name, price) in enumerate(names_and_prices)]

        if self.test == False:
            with open('../../data/amazon_results.json') as file:
                data = json.load(file)

            for item in results:
                if item not in data:
                    data.append(item)

            with open('../../data/amazon_results.json', 'w') as file:
                json.dump(data, file)

        return results
