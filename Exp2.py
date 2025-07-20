import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag, word_tokenize

# Download required NLTK data (only needed once)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopwords Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("After Stopwords Removal:", filtered_tokens)

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print("After Stemming:", stemmed_tokens)

# POS Tagging
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)
