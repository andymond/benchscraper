import sys
sys.path.insert(0, '../services/scrapers/scrapers/spiders')
import amazon_spider
import unittest
from responses import fake_response_from_file

class AmazonScraperTest(unittest.TestCase):

    def setUp(self):
        self.spider = amazon_spider.AmazonSpider(test=True)

    def test_get_urls_generates_urls(self):
        file_path = "../data/food_list.txt"
        url_list = self.spider.get_urls(file_path)

        self.assertEqual(50, len(url_list))
        self.assertEqual('https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16310101%2Ck%3A&keywords=parmesan-cheese', url_list[0])
        self.assertEqual('https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16310101%2Ck%3A&keywords=cilantro', url_list[49])

    def test_parse_generates_objects_correctly(self):
        results = self.spider.parse(fake_response_from_file('/amazon.html'))

        self.assertTrue(type(results) is list)
        self.assertEqual(3, len(results))
        self.assertTrue(type(results[0] is dict))
        self.assertEqual('Pace Medium Chunky Salsa, 64 Ounce', results[0]["name"])
        self.assertEqual(None, results[0]["price"])
        self.assertEqual('amazon', results[0]["seller"])
