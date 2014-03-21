#!/usr/bin/python
#Recognizing puns

import sys, random, nltk, urllib, string, json
from nltk.corpus import wordnet as wn

# Narrow focus down to noun and verb homonyms?
# Need to include adverb and adjective that map to noun/verb homonyms
# POS tagger goes by what it expects - even gibberish can be "properly" tagged
# Definitely can use a reversal of expectations to identify puns here, perhaps?
# May need a list of homophones to run through ConceptNet

# Start with sentences that are definitely puns


# Checks a word for potentially relevant concepts
# Adds this word, with its associated concepts, to an ongoing dictionary
# Scrapes JSON data from http://conceptnet5.media.mit.edu/data/5.1/c/en/
# TODO: Figure out how to represent the dictionary inputs
# TODO: Try/Catch?
def conceptCheck(firstWord, secondWord):
	print "Searching ConceptNet on: " + firstWord + " and " + secondWord
	url = "http://conceptnet5.media.mit.edu/data/5.2/assoc/c/en/" + firstWord + "?filter=/c/en/" + secondWord + "&limit=1"
	rawhtml = urllib.urlopen(url)
	jsonWord = json.loads(rawhtml.read())
	for score in jsonWord['similar']:
		print(score)


# Checks each word in a sentence against its expected POS vs how it appears on 
# its own
# If a word's POS differs against its expected POS, add it to a dictionary
# TODO: Figure out how to represent the dictionary inputs
def POSCheck(sentence):
	wordpos = 0
	origSent = "Original sentence: " + sentence
	print(origSent)
	text = nltk.word_tokenize(sentence)
	textTag = nltk.pos_tag(text)
	print(textTag)
	posList = []
	for word in text:
		word = nltk.word_tokenize(word)
		wordTag = nltk.pos_tag(word)
		if (wordTag[0][1][:2] != textTag[wordpos][1][:2]):
			#print "Difference spotted at: " + wordTag[0][0]
			#print(wordTag[0][1])
			#print(textTag[wordpos][1])
			posList += word
			mword = wn.morphy(word[0])
			if (mword != word[0]):
				posList.append(mword)
		wordpos += 1
	print("\n")
	return posList


# Checks each word in a sentence to see if a homophone exists
# If a word has a homophone, add it to an array. Return this array of
# words that have a homophone
def homophoneCheck(sentence):
	homophones = "homophone_list.txt"
	f = open(homophones, 'r')
	text = nltk.word_tokenize(sentence)
	hfound = []
	for line in f:
		hlist = line.rstrip().split('/')
		for word in text:
			# morphing a word down to its base word (eg. "dyed" to "dye")
			mword = wn.morphy(word)
			if (word in hlist):
				hlist.remove(word)
				hfound += hlist
			elif (mword in hlist):
				hlist.remove(mword)
				hfound += hlist
	return hfound


# Extracts the important parts of speech from the sentence
# Typically focuses on verbs, nouns, adjectives, and adverbs
def POSextract(sentence):
	wordpos = 0
	text = nltk.word_tokenize(sentence)
	textTag = nltk.pos_tag(text)
	posExt = []
	for word in text:
		word = nltk.word_tokenize(word)
		if ((textTag[wordpos][1][:2] == 'NN') or
			(textTag[wordpos][1][:2] == 'VB') or
			(textTag[wordpos][1][:2] == 'JJ')):
			posExt += word
		wordpos += 1
	print(posExt)
	return posExt


# Main function
def main():
	punIn = raw_input("Pun File: ") # get it it's a pun on "punning" hah hah
	f = open(punIn, 'r')
	for line in f:
		posList = POSCheck(line) # returns a list of words that stood out in the POS tagging
		hList = homophoneCheck(line) # returns a list of homophones, along with the original word from the sentence
		print(posList)
		print(hList)
		extText = POSextract(line) # returns a list with all of the important words extracted
		for word in extText:
			for i in range(0, len(hList)):
				conceptCheck(word, hList[i])


# Running the main function
if __name__ == "__main__":
    main()