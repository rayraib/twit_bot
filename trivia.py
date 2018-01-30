#!/usr/bin/python3
import requests


'''
   Fetches random trivia from numbersapi.
'''
url = "http://numbersapi.com/random/trivia?json"
response = requests.get(url)
text = response.json()["text"]
print(text)
