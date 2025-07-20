

import nltk
from nltk import word_tokenize

text = "Narendra Modi is the Prime Minister of India. Barracck Obamo is the president of USA"
word_tokens = word_tokenize(text)
print(word_tokens)
print(len(word_tokens), "\n")

from nltk import sent_tokenize
sent_tokens = sent_tokenize(text)
print(sent_tokens)
print(len(sent_tokens))

#lemmatization

from nltk import WordNetLemmatizer
lemma = WordNetLemmatizer()
lma = []
for word in text:
    lma.append(lemma.lemmatize(word))
    print('\n',lma)

#Regular Expression

text = "Sachin Tendulkar is a creackter.His remuneration is $500."

import re
digit = re.findall('\d+',text)
print(digit)
match = re.match('^His',text)
print(match)
search = re.search('Tendulkar',text)
print(search)
substitute = re.sub("Sachin Tendulkar","Abdul kalam",text)
text1 = re.sub("creackter","great scientist",substitute)
print(text1)