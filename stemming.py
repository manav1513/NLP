#1. porter stemmer
from nltk.stem import PorterStemmer

words = ["running", "runs", "ran", "runner"]

stemmer = PorterStemmer()
for word in words:
#    print(f"{word} -> {stemmer.stem(word)}")
    pass

#2. regex stemmer

from nltk.stem import RegexpStemmer
rule = r"ing$"
reg = RegexpStemmer(rule)
for word in words:
  stemmed_word = rule.stem(word)
  print(f" {word} -> {stemmed_word}")


#3.Snowball stemmer

from nltk.stem import SnowballStemmer

engl = SnowballStemmer("english")
for word in words:
  stemmed_word = engl.stem(word)
  print(f" {word} -> {stemmed_word}")


#4. lancaster stemmer
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()
for word in words:
  stemmed_word = lancaster.stem(word)
  print(f" {word} -> {stemmed_word}")
  