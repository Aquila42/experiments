# Thinking of plotting the sentiment of people over time eg. Tharoor from 2013-2017

import tweepy

consumer_key = "VFK5HJ4yu5kOFqCv3Wf96Z3hE"
consumer_secret = "j7aGd8N3GCAPBqJCLVtZpvVFISTrBfaW8bKZajf8sLtbr1VMxW"
access_token = "2768519106-gvlnTTlkXaaZzqdc0MPVEWLe3EAMuNBzP1LgrmB"
access_secret = "HRwci9jhSGvXE7NcjCHsZ1joYmccoIR8Gf7G5lZuFiGvH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


