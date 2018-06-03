import scrapy

class FoodPricesSpider(scrapy.Spider):
    name = "food_prices"
    urls = ['https://www.costco.com/grocery-household.html?dept=Grocery&keyword=beans']

    def response_is_ban(self, request, response):
        return b'banned' in response.body

    def exception_is_ban(self, request, exception):
        return None

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        names = response.xpath('//p[@class="description"]/a/text()').extract()
        prices = response.xpath('//div[@class="price"]/text()').extract()
        associated = list(zip(names, prices))
        data = [{'name': name, 'price': price, 'seller': 'costco'} for i, (name, price) in enumerate(associated)]

        # yield {
        #     'name': response.xpath('//div[@class="price"]/text()').extract(),
        #     'price': response.xpath('//p[@class="description"]/a/text()').extract(),
        #     'seller': "Costco",
        #     'url': self.start_urls[0]
        # }
