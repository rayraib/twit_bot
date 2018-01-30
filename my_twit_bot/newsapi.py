#!/usr/bin/python3
import requests
import json

'''
    create the URL with appropriate query paramters
    here: news souruce, techcrunch 
'''
def get_news_url():
    url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&sortBy=popularity&page=1&apiKey="
    api_key = "212cdf34d92143aa828eae7d56d2c936"
    url += api_key

# request information 
    response = requests.get(url)

# parse the received response for specific data: link to the story
    story_headline = response.json()['articles'][1]['title']
    story_link = response.json()['articles'][1]['url']
    print (story_headline)
    print (story_link)
    return (story_link)

if __name__ == "__main__":
    get_news_url()
