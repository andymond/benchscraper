import sys
sys.path.insert(0, './services/scrapers/scrapers/spiders')
import costco_spider
import unittest
from responses import fake_response_from_file

class CostcoSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = costco_spider.CostcoSpider(test=True)

    def test_get_urls_generates_urls(self):
        file_path = "./data/food_list.txt"
        url_list = self.spider.get_urls(file_path)

        self.assertEqual(50, len(url_list))
        self.assertTrue('https://www.costco.com/grocery-household.html?dept=Grocery&keyword=parmesan-cheese' in url_list)

    def test_parse_generates_objects_correctly(self):
        results = self.spider.parse(fake_response_from_file('/costco.html'))

        self.assertTrue(type(results) is list)
        self.assertEqual(38, len(results))
        self.assertTrue(type(results[0] is dict))
        self.assertEqual('Kirkland Signature Organic Ethiopia Whole Bean Coffee, 2 lbs., 2-count', results[0]["name"])
        self.assertEqual('$39.99', results[0]["price"])
        self.assertEqual('costco', results[0]["seller"])
