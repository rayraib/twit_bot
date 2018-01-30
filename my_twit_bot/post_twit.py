#!/usr/bin/python3
import twitter
import os
from datetime import datetime
from quote_api import get_quote
from newsapi import get_news_url

def authorization_for_twi(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    return (api)

def create_twit():
    day = int(datetime.now().day)
    
    if (day % 2 == 0):
        message = get_news_url()
    else:
        message = get_quote()
        print (message)
        if (len(message) > 140):
            message = get_news_url()
    return (message) 

if __name__ == "__main__":
    CONSUMER_KEY = process.env.consumer_key 
    CONSUMER_SECRET = process.env.consumer_secret 
    ACCESS_TOKEN = process.env.access_token 
    ACCESS_TOKEN_SECRET = process.env.access_token_secret 
    api = authorization_for_twi(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)    
    message = create_twit()
    api.PostUpdate(message)
