from pymongo import MongoClient
import os
import json

with open('./data/amazon_results.json') as file:
    amazon_results = json.load(file)

with open('./data/costco_results.json') as file:
    costco_results = json.load(file)

with open('./data/walmart_api_results.json') as file:
    walmart_results = json.load(file)

data_list = []
data_list.extend(amazon_results)
data_list.extend(costco_results)
data_list.extend(walmart_results)

if 'PROD' in os.environ:
    uri = os.environ['PROD']
    client = MongoClient(uri)
    db = client.get_default_database()
    print(db.collection_names())
else:
    client = MongoClient()
    db = client.benchscraper_dev

def send():
    items = db.items
    items.insert_many(data_list)
