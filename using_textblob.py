from textblob import TextBlob, Word

text = TextBlob("""Tom Rhodes, a touring comedian for more than 30 years and
                the host of the Tom Rhodes Radio podcast, joins Joey Diaz
                and Lee Syatt LIVE in studio.""")

# POS tagging
text.tags

# noun phrase extraction
text.noun_phrases
# text.noun_phrases.count()

# sentiment analysis
text.sentiment

# words and sentences
text.words
text.sentences

# word inflection and lemmatization
text.words[4].singularize()
text.words[4].pluralize()
text.words[4].lemmatize()

# wordnet
Word('hack').synsets
Word('hack').definitions

# correction
TextBlob("I havv goood speling!").correct()
Word('falibility').spellcheck() # returns (word, confidence)

# translation
text.detect_language()

from textblob.exceptions import TranslatorError, NotTranslated

try:
  print(text.translate(to = 'es'))
except TranslatorError as e:
  print(e)
except NotTranslated as e:
  print(e)

# n-grams
text.ngrams(n = 3)

