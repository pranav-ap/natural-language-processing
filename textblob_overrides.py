from textblob import TextBlob

# in-build classifier
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob("I love this library", analyzer = NaiveBayesAnalyzer())
blob.sentiment

# using different tokenizer
from nltk.tokenize import TabTokenizer
tokenizer = TabTokenizer()
blob = TextBlob("This is\ta rather tabby\tblob.", tokenizer = tokenizer)
blob.tokens

# noun phrase chunkers, POS taggers, parsers can also be overridden this way