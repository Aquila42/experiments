# Thinking of plotting the sentiment of people over time eg. Tharoor from 2013-2017

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


