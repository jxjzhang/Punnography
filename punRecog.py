#!/usr/bin/python
#Recognizing puns

import sys, random, nltk, urllib, string
from nltk.corpus import wordnet as wn

def main():
	punIn = raw_input("Pun File: ") # get it it's a pun on "punning" hah hah
	f = open(punIn, 'r')
	for line in f:
		text = nltk.word_tokenize(line)
		print(nltk.pos_tag(text))


# Running the main function
if __name__ == "__main__":
    main()