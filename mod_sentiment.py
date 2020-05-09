# -*- coding: utf-8 -*-
"""
Created on Sat May  9 07:43:03 2020

@author: Das
"""
# Importing Essential Libraries
import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from nltk.tokenize import word_tokenize

#reading file
positiv = open("dataset/positive.txt","r").read()
negativ = open("dataset/negative.txt","r").read()

#list for feature
all_words = []
final = []

#"j" for adjectives by this we're allowing type Adjectives only 
#j is adject , r is adverb, v is verb
allwd_word = ["J"]

for p in positiv.split('\n'):
    final.append( (p, "pos") ) #adding positive label to data
    words = word_tokenize(p)	#tokenizing 
    pos = nltk.pos_tag(words) #
    for w in pos:
        if w[1][0] in allwd_word:
            all_words.append(w[0].lower())
            
            
for p in negativ.split('\n'):
    final.append( (p, "neg") ) #adding negative label to data
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allwd_word:
            all_words.append(w[0].lower())
            
all_words = nltk.FreqDist(all_words) #frequency to the words i.e. count 

#limiting features for better results 
word_feat = list(all_words.keys())[:5000]

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_feat:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in final]

#shuffling features as the first half is positive and second is negative
random.shuffle(featuresets)

#dividing features to training and test set
testing_set = featuresets[10000:]  #10000 for training 
training_set = featuresets[:10000]  # rest 664 for testing

#applying MultinomialNB to training and testing its accuracy
#gives accuracy = 71-72%
"""MNB_clf = SklearnClassifier(MultinomialNB())
MNB_clf.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_clf, testing_set))*100)
"""
#applying BernoulliNB to training and testing its accuracy
#gives accuracy = 72-74%
BNB_clf = SklearnClassifier(BernoulliNB())
BNB_clf.train(training_set)
#print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BNB_clf, testing_set))*100)

#applying Decision Tree to training and testing its accuracy
#gives accuracy = 62-65%
"""dct_clf = SklearnClassifier(DecisionTreeClassifier())
dct_clf.train(training_set)
print("Decision Tree Classifier accuracy percent:", (nltk.classify.accuracy(dct_clf, testing_set))*100)"""

def sentiment(text):
    feats = find_features(text)
    v = BNB_clf.classify(feats)
    return v
