from nltk.stem import PorterStemmer

words = ['run', 'running', 'runner', 'ran', 'runs']

ps = PorterStemmer()

word_stems = list(map(lambda w: ps.stem(w), words))
