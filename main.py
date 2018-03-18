from keys import key
import tweepy
import csv
import numpy as np
from textblob import TextBlob

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token,key.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Theresa May")

csvTweet = ["Tweet"]
csvPolarity = ["Polarity"]

for tweet in public_tweets:
  text = tweet.text.replace(",","")
  analysis = TextBlob(tweet.text).sentiment.polarity
  if analysis < 0.5:
    analysisText = "Negative"
  else:
    analysisText = "Positive"
  csvTweet.append(text)
  csvPolarity.append(analysisText)

data = np.column_stack((csvTweet,csvPolarity))

np.savetxt("polarity.csv",data,delimiter=",", fmt="%s")
  
