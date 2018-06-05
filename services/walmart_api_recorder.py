import settings
import requests
import datetime
import json

base_url = "http://api.walmartlabs.com/v1/search?apiKey=" + settings.WALMART_API_KEY + "&query="
text_file = open("../data/food_list.txt", "r")
paramsList = text_file.read().splitlines()

results = []

for param in paramsList:
    response = requests.get(base_url + param)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        result = response.json()
        for item in result["items"]:
            results.append({"name": item["name"], "price": item["salePrice"], "upc": item["upc"], "seller": "walmart", "recorded_at": date})
    except:
        pass

print(results)

with open('../data/walmart_api_results.json', 'w') as outfile:
    json.dump(results, outfile)
