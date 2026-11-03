import requests
import json

# url which returns a JSON data
url = "https://itunes.apple.com/search?entity=song&limit=5&term=weezer"
response = requests.get(url)

# printing response informat of JSON
#print(json.dumps(response.json(), indent = 2))


# printing specific key data
o = response.json()

for result in o["results"]:
    print(result["trackName"])