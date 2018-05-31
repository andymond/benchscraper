import settings
import requests
import json

base_url = "http://api.walmartlabs.com/v1/search?apiKey=" + settings.WALMART_API_KEY + "&query="
text_file = open("./data/food_list.txt", "r")
paramsList = text_file.read().splitlines()

results = []

for param in paramsList:
    response = requests.get(base_url + param)
    try:
        result = response.json()
        for item in result["items"]:
            results.append({"name": item["name"], "price": item["salePrice"], "upc": item["upc"], "seller": "walmart"})
    except:
        pass

print(results)

with open('./data/barcode_api_results.jl', 'a') as outfile:
    json.dump(results, outfile)

with open('./data/barcode_api_results.json', 'a') as outfile:
    json.dump(results, outfile)
