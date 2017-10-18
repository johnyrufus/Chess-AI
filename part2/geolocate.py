#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:44:07 2017

@author: Chris Falter 
"""
import nltk
import sys
from TweetClassifier import TweetClassifier


def getLocation(tweet):
    pass



def main():
    # make sure the list of stop words is available
    #nltk.download("stopwords")
    
    #trainPath, testPath, outputPath = sys.argv[1], sys.argv[2], sys.argv[3]
    trainPath, testPath, thresholdOccurrences = sys.argv[1], sys.argv[2], int(sys.argv[3])
    classifier = TweetClassifier(thresholdOccurrences)
    with open(trainPath, 'r', encoding='latin1', newline='\n') as trainTweets:
        classifier.train(trainTweets)
    with open(testPath, 'r', encoding='latin1', newline='\n') as testTweets:
        predictions = classifier.predict(testTweets)
    
    # print the predictions in required format
    correct = sum([p.predicted == p.actual for p in predictions])
    print("Accuracy = " + str(correct / len(predictions)))
    
    top5PerLocation = classifier.top5PerLocation()
    # print top 5 predicted words per location
    

if __name__ == "__main__":
    main()
