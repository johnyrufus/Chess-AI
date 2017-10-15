# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:24:52 2017

@author: Chris Falter
"""
import re
from collections import Counter, defaultdict
from nltk.corpus import stopwords
import string

class Prediction():
    
    def __init__(self, predictedLocation, actualLocation, tweet):
        self.predicted = predictedLocation
        self.actual = actualLocation
        self.tweet = tweet

def getLocationAndTweet(s):
    '''
    Returns a tuple (location, tweet)
    location = first token in string s
    tweet = remainder of string s
    '''
    divider = s.find(' ')
    return s[:divider], s[divider + 1:] 

stopWords = set(stopwords.words('english'))
punctuation = list(string.punctuation)
punctuation.remove('#') # don't remove the hash tag symbol
punctuation = set(punctuation)
specialEntitiesRegex = re.compile("&[a-z]+;")

def removeSpecialEntities(s):
    m = specialEntitiesRegex(s)
    while (m):
        s = s[:m.start()] + s[m.end():]
        m = specialEntitiesRegex(s)
    return s

def getTokens(tweet):
    '''
    Returns a list of tokens after removing punctuation and stopwords + lower-casing
    '''
    lower = tweet.lower()
    removedSpecialEntities = removeSpecialEntities(lower)
    removedPunctuation = [c for c in removedSpecialEntities if c not in punctuation]
    tokens = removedPunctuation.split()
    return [t for t in tokens if t not in stopWords]    

class TweetClassifier():
    '''
    train() method determines priors for P(location), P(token | location)
    test() method applies naive Bayes classification to each tweet
    '''
    
    total = 'total'
    
    def __init__(self):
        self.tweetCounts = Counter()
        self.wordCounts = Counter()
        self.tokens = defaultdict(Counter)
    
    def train(self, tweets):
        '''
        Returns dictionary of token as key to [dictionary of locations (keys) to
        likelihood of appearing in a tweet from that location (value)] as value
        
        Input:
            tweets - list of strings. First token = location, remainder = tweet
        '''
        self.numTweets = len(tweets)
        for t in tweets:
            loc, tweet = getLocationAndTweet(t)
            self.tweetCounts[loc] += 1
            for token in getTokens(tweet):
                self.wordCounts[loc] += 1
                self.tokens[token][loc] += 1                            
        
    def test(self, tweets):
        '''
        Returns list of Prediction objects
        
        Input:
            tweets = list of tweets. First token = location, remainder = tweet
        '''
        self.calculateProbabilities()
        result = []
        for t in tweets:
            loc, tweet = getLocationAndTweet(t)
            prediction = self.predictLocation(tweet)
            result.append(Prediction(prediction, loc, tweet))
        return result
    
    def calculateProbabilities(self):
        pass
    
    def predictLocation(self, tweet):
        pass
    
    def top5PerLocation(self):
        pass