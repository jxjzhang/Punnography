#!/usr/bin/python
#what do you call a...

import sys, random, nltk, urllib, string
from nltk.corpus import wordnet as wn

def main():
	homophones = raw_input("Homophones file: ")
	f = open(homophones, 'r')
	for line in f:
		hlist = line.rstrip().split(',')
		print hlist
		l_adjs = []
		l_nouns = []
		l_verbs = []
		for word in hlist:
			adjs = []
			nouns = []
			verbs = []
			for synset in wn.synsets(word, 'a'):
				if not adjs:
					adjs.append(word.lower())
					adjs.append(synset.name)
				for lemma in synset.lemmas:
					if lemma.name not in adjs and lemma.name.lower().find(adjs[0]) == -1:
						adjs.append(lemma.name.replace('_',' '))
			
			for synset in wn.synsets(word, 'n'):
				if not nouns:
					nouns.append(word.lower())
					nouns.append(synset.name)
				for lemma in synset.lemmas:
					if lemma.name not in nouns and lemma.name.lower().find(nouns[0]) == -1:
						nouns.append(lemma.name.replace('_',' '))
	
			for synset in wn.synsets(word, 'v'):
				if not verbs:
					verbs.append(word.lower())
					verbs.append(synset.name)
				for lemma in synset.lemmas:
					if lemma.name not in verbs and lemma.name.lower().find(verbs[0]) == -1:
						verbs.append(lemma.name.replace('_',' '))
				
			if len(adjs) > 2:
				l_adjs.append(adjs)
			if len(nouns) > 2:
				l_nouns.append(nouns)
								
		if l_adjs and l_nouns:
			for adjs in l_adjs:
				for nouns in l_nouns:
					for a in range(2, len(adjs)):
						for n in range (2, len(nouns)):
							prefix = "What do you call a"
							if adjs[a][0] in ('a','e','i','o','u'):
								prefix = prefix + "n"
							print (prefix + " " + adjs[a] + " " + nouns[n] + "? " + adjs[0] + " " + nouns[0])

		if len(l_nouns) > 1:
			for nouns1 in l_nouns:
				for nouns2 in l_nouns:
					if set(nouns2) == set(nouns1):
						break
					for n1 in range(2, len(nouns1)):
						for n2 in range (2, len(nouns2)):
							prefix = "What do you call a"
							if nouns1[n1][0] in ('a','e','i','o','u'):
								prefix = prefix + "n"
							print (prefix + " " + nouns1[n1] + "'s favorite " + nouns2[n2] + "? " + nouns1[0])

if __name__ == "__main__":
    main()