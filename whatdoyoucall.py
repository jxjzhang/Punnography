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
		for word in hlist:
			adjs = []
			nouns = []
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
							
			if len(adjs) > 2:
				l_adjs.append(adjs)
			if len(nouns) > 2:
				l_nouns.append(nouns)
								
		if l_adjs and l_nouns:
			for adjs in l_adjs:
				for nouns in l_nouns:
					for a in range(2, len(adjs)):
						for n in range (2, len(nouns)):
							sim = wn.synset(nouns[1]).shortest_path_distance(wn.synset(adjs[1]),False)
							print adjs[1],nouns[1],sim
							prefix = "What do you call a"
							if adjs[a][0] in ('a','e','i','o','u'):
								prefix = prefix + "n"
							print (prefix + " " + adjs[a] + " " + nouns[n] + "? " + adjs[0] + " " + nouns[0])

if __name__ == "__main__":
    main()