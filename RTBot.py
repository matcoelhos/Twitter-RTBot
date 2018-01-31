import tweepy
from lxml import html
import requests
import time

#this data is obtained after creating you application
#at https://apps.twitter.com/
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

#authentication to access twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    filename=open("list.txt",'r')   #import users from file list.txt
    f=filename.readlines()          #reads each line and after closes file
    filename.close()
    for line in f:
        #reads last tweet from each line and tries to retweet
        cand = api.get_user(line)
        cid = cand.id;
        statuses = api.user_timeline(screen_name = line, count = 1, include_rts = True)
        #tries to retweet the last status
        #the application does not retweet repeted data
        try:
            api.retweet(statuses[0].id)
        except tweepy.error.TweepError:
            pass
        #waits for 240 seconds to try next user
        time.sleep(240);
