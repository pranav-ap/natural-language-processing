from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = stopwords.words('english')

example = 'this is an example sentence.'
words = word_tokenize(example)

filtered_sentence = [w for w in words if w not in stop_words]
