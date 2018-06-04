import sys
sys.path.insert(0, '../services/scrapers/scrapers/spiders')
import costco_spider
import unittest

class CostcoSpiderTest(unittest.TestCase):

    def setup:
        self.spider = costco_spider.CostcoSpider()

    def test_get_urls_generates_urls:
        file_path = "../data/food_list.txt"
        url_list = self.spider.get_urls(file_path)

        self.assertEqual(50, len(url_list))
