import requests
from pprint import pprint
import json



url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
countries = response.json()

country_data= []

for country in countries:
    country_info = {
        'name': country['name']['common'],
        'iso_code': country['cca2'],
        'phone_code': country['idd']['root'] + country['idd']['suffixes'][0] if 'idd' in country and 'root' in country['idd'] and 'suffixes' in country['idd'] else None,
        'language': list(country['languages'].values())[0] if 'languages' in country else None,
        'capital': country['capital'][0] if 'capital' in country and country['capital'] else None
    }
    country_data.append(country_info)

json_file = 'country_data.json'

# Write data to JSON file
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(country_data, file, ensure_ascii=False, indent=2)

print(f"Data has been written to {json_file}")