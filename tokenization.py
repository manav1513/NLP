corpus = """This can be a fun and engaging way to start. You can
 find collections of movie subtitles online in various languages. 
 This corpus offers a mix of dialogue, descriptions, and emotions, making
   it good for tasks like sentiment analysis or named entity recognition (NER)."""

from nltk.tokenize import sent_tokenize
documents = sent_tokenize(corpus)
# print(documents)

from nltk.tokenize import word_tokenize
doc = word_tokenize(corpus)
#print(doc)

for sent in documents:
    words = word_tokenize(sent)
    print(words)
#from nltk.tokenize import wordpunct_tokenize

from nltk.tokenize import TreebankWordDetokenizer
tok = TreebankWordDetokenizer()
tok.tokenize(corpus)
