from urllib.request import urlopen
import requests
import json

## creating URL with query strings to the base API url ####
url = "http://api.npr.org/query?id=1027,1019&fields=title&title=kj&dateType=story&output=JSON&apiKey="
key = "UxaD9khYZEfndGEUuNH0uZXA4KAVqdLjg2G1K0dI"
url += key
## Open the url ##
response = requests.get(url)
print (response.json)
for key in response:
    print (key)
## create a json object of the returned response ##
story_link = response.json()['list']['title']#['story']['link']['$text']
print (story_link)
