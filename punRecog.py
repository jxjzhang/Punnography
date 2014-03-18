#!/usr/bin/python
#Recognizing puns

import sys, random, nltk, urllib, string, json
from nltk.corpus import wordnet as wn

# Narrow focus down to noun and verb homonyms?
# Need to include adverb and adjective that map to noun/verb homonyms
# POS tagger goes by what it expects - even gibberish can be "properly" tagged
# Definitely can use a reversal of expectations to identify puns here, perhaps?

# Start with sentences that are definitely puns


# Checks a given word for potentially relevant concepts
# Adds this word, with its associated concepts, to an ongoing dictionary
#def conceptCheck:

# Checks each word in a sentence against its expected POS vs how it appears on 
# its own
# If a word's POS differs against its expected POS, add it to a dictionary
def POSCheck(sentence):
	wordpos = 0
	origSent = "Original sentence: " + sentence
	print(origSent)
	text = nltk.word_tokenize(sentence)
	textTag = nltk.pos_tag(text)
	print(textTag)
	for word in text:
		word = nltk.word_tokenize(word)
		wordTag = nltk.pos_tag(word)
		if (wordTag[0][1][:2] != textTag[wordpos][1][:2]):
			diff = "Difference spotted at: " + wordTag[0][0]
			print(diff)
			print(wordTag[0][1])
			print(textTag[wordpos][1])
		wordpos += 1
	print("\n")

def main():
	punIn = raw_input("Pun File: ") # get it it's a pun on "punning" hah hah
	f = open(punIn, 'r')
	for line in f:
		POSCheck(line)


# Running the main function
if __name__ == "__main__":
    main()