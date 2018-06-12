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

def get_amazon():
    os.system('printf "gathering amazon data...\n"')

def get_costco():
    os.system('printf "gathering costco data...\n"')

def send_to_database():
    os.system('printf "sending data to db...\n"')

get_walmart()
get_amazon()
get_costco()
send_to_database()

#
# printf 'gathering walmart data...\n'
# cd services/
# python walmart_api_recorder.py
#
# printf 'gathering amazon data...\n'
# cd scrapers/
# scrapy crawl amazon_spider
#
# printf 'gathering costco_data...\n'
# scrapy crawl costco_spider
#
# printf 'collected data\n'
#
# printf 'sending data to database\n'
# cd ../../
# python db/update_database.py
