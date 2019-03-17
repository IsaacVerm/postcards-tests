import requests
from secrets import collection_uid, postman_api_key

url = f'https://api.getpostman.com/collections/{collection_uid}'
headers = {
    'X-Api-Key': postman_api_key
}
response = requests.request('GET', url, headers=headers)

collection = open("postcards_postman_collection.json", "w")
collection.write(response.text)
collection.close()
