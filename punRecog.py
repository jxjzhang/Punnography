#!/usr/bin/python
#Recognizing puns

import sys, random, nltk, urllib, string
from nltk.corpus import wordnet as wn

# Narrow focus down to noun and verb homonyms?
# Need to include adverb and adjective that map to noun/verb homonyms
# POS tagger goes by what it expects - even gibberish can be "properly" tagged
# Definitely can use a reversal of expectations to identify puns here, perhaps?

# Start with sentences that are definitely puns

def main():
	punIn = raw_input("Pun File: ") # get it it's a pun on "punning" hah hah
	f = open(punIn, 'r')
	wordpos = 0
	for line in f:
		origSent = "Original sentence: " + line
		print(origSent)
		text = nltk.word_tokenize(line)
		textTag = nltk.pos_tag(text)
		print(textTag)
		for word in text:
			print(word)
			word = nltk.word_tokenize(word)
			wordTag = nltk.pos_tag(word)
			if (textTag[wordpos][1] != wordTag[0][1]):
				diff = "Difference spotted at " + wordTag[0][0]
				print(diff)
			wordpos += 1
		wordpos = 0


# Running the main function
if __name__ == "__main__":
    main()