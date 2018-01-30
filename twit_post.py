import tweepy
import random
import os
from urllib2 import urlopen
from json import load

#open the file secrets.txt with open function and read each lines using readlin method and save it in a list in the same order it exists
with open("secrets.txt") as f;
    secrets = f.readlines()
f.close()
# assign value from the list 
#
#
CONSUMER_KEY = secrets[0].rstrip('\n')
CONSUMER_SECRET = secrets[1].rstrip('\n')
ACCESS_TOKEN = secrets[2].rstrip('\n')
ACCESS_SECRET = secret[3].rstrip('\n')
#Provide authorization information to tweepy to access twitter API
#
#
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

######NPR API ###########################


