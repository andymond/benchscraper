import os
import sys
sys.path.insert(0, './services/scrapers/scrapers/spiders')
import amazon_spider
import costco_spider
sys.path.insert(0, './services')
import walmart_api_recorder
sys.path.insert(0, './db')
import update_database

def get_walmart():
    os.system('printf "gathering walmart data...\n"')
    walmart_api_recorder.record()

def get_amazon():
    os.system('printf "gathering amazon data...\n"')
    amazon_spider.start_requests()

def get_costco():
    os.system('printf "gathering costco data...\n"')
    costco_spider.start_requests()

def send_to_database():
    os.system('printf "sending data to db...\n"')
    db_manager.send()
