# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:04:50 2020

@author: Das
"""
import pandas as pd
import numpy as np
import re
import tweepy
import twitter_credentials
import mod_sentiment as s
class TweetAnalyzer():

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self,tweet):
        a = self.clean_tweet(tweet)
        #print(a)
        b = s.sentiment(tweet)
        return b

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        #df.drop_duplicates(subset = 'tweets', keep=False, inplace=True)
        return df
    
if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit = True)
    tweet_analyzer = TweetAnalyzer()
    
    numtweets = int(input("Enter no of tweets"))
    num = int(input("Enter no of companies"))
    score = {}
    for i in range(num):
        query=input("Enter Company Name :")
        tweets =[]
        
        for tweet in tweepy.Cursor(api.search, q=query, lang="en", rpp=100).items(numtweets):
            tweets.append(tweet)
        
        df = tweet_analyzer.tweets_to_data_frame(tweets)
    
        df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
        df.drop_duplicates(subset = 'tweets', keep=False, inplace=True)
        score[query] =  df['Sentiment'].str.count("pos").sum() - df['Sentiment'].str.count("neg").sum()
        #df.to_csv('{}.csv'.format(query)) #to save csv file of every company
        
    sorted_score = sorted(score.items(), key=lambda x: x[1], reverse = True)
    sorted_score = list(sorted_score)
    
    #Ranking of companies
    print("Rank of Companies")
    for i in range(len(sorted_score)):
        print(i+1,sorted_score[i][0])
    