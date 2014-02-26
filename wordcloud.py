import nltk, string, urllib, re, unicodedata
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn


def main():
	word = raw_input("Enter word: ")
	word = wn.morphy(word)
	print word
	url = "http://en.wiktionary.org/wiki/" + word
	rawhtml = urllib.urlopen(url)
	soup = BeautifulSoup(rawhtml)
	wordcloud = []

	for link in soup.find_all('a'):
		href = link.get('href')
		title = link.get('title')
		if href is not None and title is not None:
			if href.startswith('/wiki/') and (href.find('#') == -1 or href.find('#English') != -1) and href.lower().find('wiktionary') == -1 and href.find(':') == -1 and title.lower() != word.lower() and href.find('%') == -1 and title.find('[') == -1 and title.lower() != 'wikipedia':
				wordcloud.append(unicodedata.normalize('NFKD',title).encode('ascii','ignore'))

	print wordcloud

if __name__ == "__main__":
    main()