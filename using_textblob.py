from textblob import TextBlob

text = TextBlob("""Tom Rhodes, a touring comedian for more than 30 years and
                the host of the Tom Rhodes Radio podcast, joins Joey Diaz
                and Lee Syatt LIVE in studio.""")

# POS tagging
text.tags

# noun phrase extraction
text.noun_phrases
text.noun_phrases.count()

# sentiment analysis
text.sentiment

# words and sentences
text.words
text.sentences

text.words.count()

# word inflection and lemmatization
text.words[1].singularize()
text.words[1].pluralize()
text.words[1].lemmatize()

text.words.pluralize()

# wordnet
from textblob.wordnet import VERB
Word('hack').synsets
Word('hack').definitions

# correction
TextBlob("I havv goood speling!").correct()
Word('falibility').spellcheck() # returns (word, confidence)

# translation
text.detect_language()

try:
  text.translate(to = 'es')
except TranslatorError as e:
  print(e)
except NotTranslated as e:
  print(e)

# n-grams
text.ngrams(n = 3)

