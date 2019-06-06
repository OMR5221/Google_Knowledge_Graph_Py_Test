"""Example of Python client calling Knowledge Graph Search API."""
import json
import requests

api_key = open('.api_key').read()
print(api_key)
query = 'Google'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
# url = service_url + '?' + urllib.urlencode(params)
response = requests.get(service_url,  params=params)
response_json = response.json()
print(response_json)

for element in response_json['itemListElement']:
    if 'name' in element['result'].keys():
        print(element['result']['name'] + ' - ' + str(element['result']['@type']) + ' (' + str(element['resultScore']) + ')')
