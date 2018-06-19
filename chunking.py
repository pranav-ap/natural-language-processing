import nltk
from nltk.tokenize import word_tokenize

sentence = "the little yellow dog barked at the cat"
words = word_tokenize(sentence)

word_tags = nltk.pos_tag(words)

#Define your grammar using regular expressions
grammar = ('''NP: {<DT>?<JJ>*<NN>} # NP''')

chunkParser = nltk.RegexpParser(grammar)

chunked = chunkParser.parse(word_tags)
chunked.draw()
