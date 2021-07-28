getting started NLTK

- from nltk.book import *:
    text1,2,....9

#searching text
    text.concurdance('word')-concordance view shows us every occurrence of a given word, together with some context

    text.similar('word')

    text.common_contexts(['lsit of words'])-It is one thing to automatically detect that a particular word occurs in a text, and to display some words that appear in the same context

    text.dispersion_plot(['list of words'])

#counting vocabulary
    len(text),sorted(set(text))

    text.count('word')

#frequency distributions
    from nltk.book import *

    s = FreqDist('text')-returns most frequent words
    s.most_common('value')-returns value words
    s['word']-count of word
    s.max()-most frequent word length
    s[3]-count of words of len 3 
    s.freq('word')-frequency of given word in sample
    s.tabulate()-tabulate the freq distribution
    fdist.plot()	graphical plot of the frequency distribution
    fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
    fdist1 |= fdist2	update fdist1 with counts from fdist2
    fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2


#collocations and bigrams
    bigrams - list of word pairs, also known as bigrams
    list(bigrams(['list of words']))

    text.collocations()-collocations are essentially just frequent bigrams

#nltk automatic challenges:

    1.words sense disambiguation: which sense of a word was intended in a given context
    
    a.The lost children were found by the searchers (agentive)
    b.The lost children were found by the mountain (locative)
    c.The lost children were found by the afternoon (temporal)

    2.pronoun resolution: to detect the subjects and objects of verbs

    a.The thieves stole the paintings. They were subsequently sold.
    b.The thieves stole the paintings. They were subsequently caught.
    c.The thieves stole the paintings. They were subsequently found.
    Answering this question involves finding the antecedent of the pronoun they, either thieves or paintings.
    Computational techniques for tackling this problem include anaphora resolution — identifying what a pronoun or noun phrase refers to — and semantic role labeling — identifying how a noun phrase relates to the verb (as agent, patient, instrument, and so on).

    3.generating language ouptut:  question answering and machine translation.

'accessing text corpora'

#gutenburg corpus:
    corpus which contains 25000 free electronic books

    import nltk
    nltk.corpus.gutenburg.fileids() :-return fileids
    nltk.corpus.gutenburg.words('fileid') :-return text in gutenburg files
    gutenburg.raw('fileid') :-return raw form of text without any linguistic processing eg. including spaces between words
    gutenburg.sents() :- divides the text up into its sentences, where each sentence is a list of words

#web text:
    corpos which contain firefox disscussion forum,movie script ,ads etc..

    from nltk.corpus import webtext
    webtext.fileids() :-return fileids

#chat texts:
    contains 15 files each contain several hundred posts on specific date,age specific platform

    from nltk.corpus import nps_chat
    s=nps-chat.fileids()
    s.posts('fileid')

#brown corpus:
    first million-word electronic corpus of English
    corpus contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, and so on

    from nltk.corpus import brown
    brown.categories()
    brown.words()

#reuters corpus:
     Corpus contains 10,788 news documents totaling 1.3 million words. The
     documents have been classified into 90 topics, and grouped into two sets, called "training" and "test";
    used for automaticallyh detect the topic of document.

    from nltk.corpus import reuters

#other language corpus:

#loading own corpus:
    store your files in a directory.set this as corpus_root

    corpus_root='/path'
    from nltk.corpus import PlaintextCorpusReader
    x=PlaintextCorpusReader(corpus_root,'[filedids]') :- or '.*' for all the files in  directory

'conditional frequency distributions'
A conditional frequency distribution is a collection of frequency distributions, each one for a different "condition"


'lexical resources'

#wordslist corpora:

    from nltk.corpus import words
    words.words() :- return 40k words

    from nltk.corpus import stopwords
    stopwords.words('english')

#pronouncing dictionary:

    nltk.corpus.cmudict.entries() :-returns list of phonetic codes of words
    for words,pron in entries: :-where pron resembles phonetic codes
    d = nltk.corpus.cmudict.dict()
    d['word'] :-if word doesnt present gives key error

'wordnet'

#senses and synonyms:

    from nltk.corpus import wordnet as wn
    wn.synsets('word') :-return sunset of words /synonym set-which is collection of synonuyms words
    wn.synste('word.n.01').lemma_names() :-returns collection of words of the synset
    wn.synset('synset').definition() :-return def of all synonym word of synste
    wn.synset.('synset').examples() :-return examples

    'car.n.01.motorcar' :-pairing of a synset with a word is called a lemma
    wn.synset('car.n.01').lemmas() :-return lemma
    wn.lemma('car.n.01.motorcar') :-look up for particular lemma
    wn.lemma('car.n.01.motorcar').synset() :-return synset
    wn.lemma('car.n.01.motorcar').name() :-return name of lemma eg.'motorca'

#hymponyms

    a=wn.synset('car.n.01')
    a.hyponyms()
    a.hypernyms()

'processing raw text'

    import nltk,re,pprint
    from nltk import word_tokenize

#accessing text from web and disk
    You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file.

    from urllib import request
    url='http://www.gutenberg.org/files/2554/2554-0.txt'
    response=request.urlopen('url')
    raw=response.read().decode('utf8')

    token=word_tokenize('text')
    text.find('word') :-return index
    text.rfind('word') :-returns reverse find index

#dealing with html

    url='http://news.bbc.co.uk/2/hi/health/2284783.stm' :- the html must saved as text
    html = request.urlopen(url).read().decode('utf8') :- returns  HTML content in all its glory, including meta tags, an image map, JavaScript, forms, and tables.

    to get text from html we use 'BeautifulSoup'

    from bs4 import BeautifulSoup
    s=BeautifulSoup(html,'html.parser').get_text() :-returns text from above html


'some string functions'

s.find(t)	index of first instance of string t inside s (-1 if not found)
s.rfind(t)	index of last instance of string t inside s (-1 if not found)
s.index(t)	like s.find(t) except it raises ValueError if not found
s.rindex(t)	like s.rfind(t) except it raises ValueError if not found
s.join(text)	combine the words of the text into a string using s as the glue
s.split(t)	split s into a list wherever a t is found (whitespace by default)
s.splitlines()	split s into a list of strings, one per line
s.lower()	a lowercased version of the string s
s.upper()	an uppercased version of the string s
s.title()	a titlecased version of the string s
s.strip()	a copy of s without leading or trailing whitespace
s.replace(t, u)	replace instances of t with u inside s

'some re symbols'

s.find(t)	index of first instance of string t inside s (-1 if not found)
s.rfind(t)	index of last instance of string t inside s (-1 if not found)
s.index(t)	like s.find(t) except it raises ValueError if not found
s.rindex(t)	like s.rfind(t) except it raises ValueError if not found
s.join(text)	combine the words of the text into a string using s as the glue
s.split(t)	split s into a list wherever a t is found (whitespace by default)
s.splitlines()	split s into a list of strings, one per line
s.lower()	a lowercased version of the string s
s.upper()	an uppercased version of the string s
s.title()	a titlecased version of the string s
s.strip()	a copy of s without leading or trailing whitespace
s.replace(t, u)	replace instances of t with u inside s

'nltk re tokenizer'

    nltk.regexp_tokenize('text,pattern') :-similar to re.findall()

'python debbuger'

    import pdb :- debugger which allows you to monitor the execution of your program
                        specify line numbers where execution will stop (i.e. breakpoints), and step through sections of code and inspect the value of variables.
    
