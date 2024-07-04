# Import libraries
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()


pos_tags = ["v", "n", "a", "r"] 
text = "They are running very fast today."
tokens = word_tokenize(text)

if pos_tags:
  
  lemmatized_words = [lemmatizer.lemmatize(token, pos) for token, pos in zip(tokens, pos_tags)]
else:
  lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]

print(f"Original Text: {text}")
print(f"Lemmatized Text: {' '.join(lemmatized_words)}")
