import nltk, string, urllib, re, unicodedata
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn


def main():
	word = raw_input("Enter word: ")
	mword = wn.morphy(word)
	if mword:
		word = mword
	print "Searching Wiktionary on:", word
	url = "http://en.wiktionary.org/wiki/" + word
	rawhtml = urllib.urlopen(url)
	soup = BeautifulSoup(rawhtml)
	wordcloud = []
	wordcloud_slang = []


	for link in soup.find_all('a'):
		href = link.get('href')
		title = link.get('title')
		parent = link.parent
		headline = None
		language = None
		h4heading = None

		if href is not None and title is not None:
			metadata = 0
			if parent and parent.name == 'span':
				c = parent.get('class')
				if c:
					c = unicodedata.normalize('NFKD',parent.get('class')[0]).encode('ascii','ignore')
				if c == 'ib-content':
					metadata = 1
			
			if metadata == 0 and \
				href.startswith('/wiki/') and \
				(href.find('#') == -1 or href.find('#English') != -1) and \
				href.lower().find('wiktionary') == -1 and \
				href.find(':') == -1 and \
				title.lower() != word.lower() and \
				href.find('%') == -1 and title.find('[') == -1 and \
				title.lower() != 'wikipedia':
				
				while (parent):
					if (parent.name != 'li'):
						parent = parent.parent
					else:
						break
				if parent:
					h4heading = parent.find_previous('h4')
					headline = parent.find_previous('h3')
					language = parent.find_previous('h2')
					if headline:
						headline = headline.span
						if headline:
							headline = headline.get('id')
					if language:
						language = language.span
						if language:
							language = language.get('id')
					if h4heading:
						h4heading = h4heading.span
						if h4heading:
							h4heading = h4heading.get('id')
			
				slang = 0
				tag = None
				title = unicodedata.normalize('NFKD',title).encode('ascii','ignore')
				if (parent):
					for tag in parent.find_all('a'):
						tag = tag.get('href')
						if (tag == '/wiki/Appendix:Glossary#slang' or tag == '/wiki/Appendix:Glossary#vulgar'):
							slang = 1
					
				if (headline and headline != 'Pronunciation' and headline != 'Anagrams') \
					and (language is None or language == 'English') \
					and (h4heading is None or not h4heading.lower().startswith('translation')):
					if slang:
						wordcloud_slang.append(title)

					wordcloud.append(title)
				#print language, headline, h4heading, title

	print wordcloud_slang
	print wordcloud

if __name__ == "__main__":
    main()