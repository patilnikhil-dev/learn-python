import requests

# url which returns a JSON data
url = "https://itunes.apple.com/search?entity=song&limit=5&term=weezer"
response = requests.get(url)

# printing response informat of JSON
print(response.json())
