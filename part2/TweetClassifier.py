# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:24:52 2017

@author: Chris Falter
"""
import re
from collections import Counter, defaultdict
from nltk.corpus import stopwords
import string
import numpy as np

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

punc = string.punctuation.replace('#','').replace('@','').replace('-','').replace(' ','')
punctuationRemover = str.maketrans(punc, ' '*len(punc))
stopWords = set(stopwords.words('english'))
specialEntitiesRegex = re.compile("&[a-z]+;")

def removeSpecialEntities(s):
    m = specialEntitiesRegex.search(s)
    while (m):
        s = s[:m.start()] + s[m.end():]
        m = specialEntitiesRegex.search(s)
    return s

def getTokens(tweet):
    '''
    Returns a list of tokens after removing punctuation and stopwords + lower-casing
    '''
    # TODO: try stemming the words
    # remove HTML special entities (such as '&gt;') first
    s = removeSpecialEntities(tweet)
    # lower-case so that each use of a word is coalesced, regardless of case
    s = s.lower()
    # remove punctuation
    s = s.translate(punctuationRemover)
    # tokenize
    tokens = s.split()
    # remove stop words
    return list(filter(lambda t: t not in stopWords, tokens))   

class TweetClassifier():
    '''
    train() method determines priors for P(location), P(token | location)
    test() method applies naive Bayes classification to each tweet
    
    TODO - Experiment with the following model parameters:
        1. Stem the tokens vs. don't stem
        2. Threshold for occurrence of word in training corpus (i.e., to exclude rare terms)
        3. Laplace smoothing vs. exclusion of rare or previously unobserved term
        4. Binary appearance of word in tweet vs. including multiple occurrences
    '''
    
    def __init__(self, tokenOccurrenceThreshold = 1):
        '''
        Inputs:
            tokenOccurrenceThreshold = minimum number of occurrences of token 
            for it to be used in predicting location
        '''
        self.tokenOccurrenceThreshold = tokenOccurrenceThreshold
        
        # accumulators
        self.numTweets = 0
        self.tweetCounts = Counter()
        self.wordCounts = Counter()
        self.tokens = defaultdict(Counter)
    
        # probability tables
        self.locationPrior = None # will be a ndarray of log(P(location))
        self.tokenPriors = {} # dictionary: key = token, value = ndarray of P(token|location)
        
        # dictionary to keep track of locations
        self.locations = dict()
        
    def train(self, tweets):
        '''
        Returns dictionary of token/key to [dictionary of locations (keys) to
        likelihood of appearing in a tweet from that location (value)] as value
        
        Input:
            tweets - list of strings. First token = location, remainder = tweet
        '''
        for t in tweets:
            self.numTweets += 1
            loc, tweet = getLocationAndTweet(t)
            self.tweetCounts[loc] += 1
            for token in getTokens(tweet):
                self.wordCount[loc] += 1
                self.tokens[token][loc] += 1                            
        
    def test(self, tweets):
        '''
        Returns list of Prediction objects
        
        Input:
            tweets = list of tweets. First token = location, remainder = tweet
        '''
        self._calculateProbabilities()
        result = []
        for t in tweets:
            loc, tweet = getLocationAndTweet(t)
            prediction = self._predictLocation(tweet)
            result.append(Prediction(prediction, loc, tweet))
        return result
    
    def _calculateProbabilities(self):
        '''
        Calculate the following prior probabilities:
            * Probability of a tweet (regardless of content) being from a location.
              Must be calculated for each location, should sum to 1.0 over all locations
            * Probability that a token will be in a tweet, given a location
              Must be calculated for each token whose count exceed min threshold,
              over all locations
        Token probabilities will omit tokens that occur less than the threshold
        Token probabilities will use LaPlace smoothing to allow predictions to use
            logarithms, which will prevent underflow (see 
        https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html)
        '''
        locationDistribution = []
        for i, location in enumerate(self.tweetCounts):
            self.locations[i] = location
            locationDistribution.append(self.tweetCounts[location] / self.numTweets)
        self.locationPrior = np.array(locationDistribution)
        
        # Laplace smoothing step 1: add number of terms to word count
        sizeVocabulary = len(self.tokens)
        for key in self.wordCount:
            self.WordCount[key] += sizeVocabulary 
        
        # Laplace smoothing step 2: add 1 to number of occurrences for each word, each location
        # will do this while building the probability tables for P(token | location)
        for token in self.tokens:
            wordBag = self.tokens[token]
            if sum([wordBag[k] for k in self.locationPrior]) < self.tokenOccurrenceThreshold:
                continue
            priors = []
            for location in self.tweetCounts:
                priors.append((wordBag[location] + 1) / self.wordCount[location])
            self.tokenPriors[token] = np.array(priors)
                
    
    def _predictLocation(self, tweet):
        tokens = getTokens(tweet)
        numTokens = len(tokens)
        estimates = self.locationPrior.copy()
        for token in tokens:
            tokenPriors = self.tokenPriors.get(token)
            if tokenPriors:
                # multiply by numTokens to help prevent underflow
                estimates *= (tokenPriors * numTokens) 
        return self.locations[np.argmax(estimates)]                    
    
    def top5PerLocation(self):
        '''
        Returns a dictionary:
            key = location
            value = list of 5 words that predict most highly for the location
        '''
        pass