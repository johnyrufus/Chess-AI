# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:41:00 2017

@author: Chris Falter
"""

from TweetClassifier import (
        TweetClassifier, 
        getLocationAndTweet, 
        removeSpecialEntities,
        getTokens
        )

import unittest

class testTweetClassifier(unittest.TestCase):
    
    def test_getLocationAndTweet(self):
        s = 'Washington,_DC Join the New Signature team! See our latest #job opening here:  #Washington, DC #Hiring'
        loc, tweet = getLocationAndTweet(s)
        self.assertEqual(loc, 'Washington,_DC')
        self.assertEqual(tweet, 'Join the New Signature team! See our latest #job opening here:  #Washington, DC #Hiring')
                         
    def test_removeSpecialEntities_MultipleEntities_RemovesAll(self):
        tweet = "Jogging &lt;&gt; running &amp; stick-ball &lt;&gt; baseball"
        actual = removeSpecialEntities(tweet)
        expected = "Jogging  running  stick-ball  baseball"
        self.assertEqual(actual, expected)
        
    def test_removeSpecialEntities_SingleEntity_RemovesEntity(self):
        tweet = "At the corner of 5th Ave &amp; Broadway"
        actual = removeSpecialEntities(tweet)
        expected = "At the corner of 5th Ave  Broadway"
        self.assertEqual(actual, expected)
        
    def test_removeSpecialEntities_NoEntity_ReturnsOriginalTweet(self):
        tweet = "A simple tweet for simple folks"
        actual = removeSpecialEntities(tweet)
        expected = tweet
        self.assertEqual(actual, expected)

    def test_getTokens_RemovesSpecialEntities(self):
        tweet = "jogging &lt;&gt; running &amp; stick-ball &lt;&gt; baseball"
        expected = ['jogging','running','stick-ball','baseball']
        actual = getTokens(tweet)
        self.assertListEqual(expected, actual)

    def test_getTokens_RemovesPunctuation(self):
        tweet = "jogging, running: stick-ball?! baseball."
        expected = ['jogging','running','stick-ball','baseball']
        actual = getTokens(tweet)
        self.assertListEqual(expected, actual)

    def test_getTokens_LowersCase(self):
        tweet = "Jogging, ruNniNg: stick-BAll?! BASEBALL."
        expected = ['jogging','running','stick-ball','baseball']
        actual = getTokens(tweet)
        self.assertListEqual(expected, actual)
        
    def test_getTokens_RemovesStopWords(self):
        tweet = "He hasn't gone Jogging or ruNniNg; and stick-BAll?! No! BASEBALL."
        expected = ['gone','jogging','running','stick-ball','baseball']
        actual = getTokens(tweet)
        self.assertListEqual(expected, actual)

    def test_getTokens_TweetWithAllConditions_PerformsAllOps(self):
        tweet = "He hasn't gone Jogging or ruNniNg; and stick-BAll! &amp; BASEBALL."
        expected = ['gone','jogging','running','stick-ball','baseball']
        actual = getTokens(tweet)
        self.assertListEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()



