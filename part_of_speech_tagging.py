import nltk
from nltk.tokenize import word_tokenize

example = 'this is an example sentence.'
words = word_tokenize(example)

word_tags = nltk.pos_tag(words)
