# Benchscraper
Tools to gather pricing data from the Internet

## About 
* Currently contains scrapers to hit amazon & costco, and consumes from the walmart api for pricing information
* The project contains a food_list.txt to search for 50 different kinds of foods by default, but can search for anything you put into the file separated by line breaks
* The scrapers & api recorder save info into a json file
* If the data looks good, a user can populate their mongodb collection with the information gathered

## Dependencies
Python 3.6.5  
Requests  
Scrapy  
PyMongo  
Walmart API Key  
MLabs Mongodb database (for production only)  

## Setup & Use
install python 3 & pip  
get into the project:  
```git clone https://github.com/andymond/benchscraper.git```  
```cd benchscraper```  
  
set up  
```python -m venv venv```  
```. ./venv/bin/activate```  
```pip install -r requirements.txt```  
```scripts/update-data``` to run api recorder, both scrapers and save to local database  
-> to save to production database, set ```PROD=<your production mongodb uri>```  
  
to run scrapers individually:  
from within services directory:
```scrapy crawl costco_spider```  
```scrapy crawl amazon_spider```  
```python walmart_api_recorder.py``` 

to populate db from json records:
from root directory
```python db/update_database.py```

to test scrapers generate urls & parse return as expected:
from within test directory:
```python -m unittest run_all.py```
