from textblob import TextBlob

train = [
  ('I love this sandwich.', 'pos'),
  ('this is an amazing place!', 'pos'),
  ('I feel very good about these beers.', 'pos'),
  ('this is my best work.', 'pos'),
  ("what an awesome view", 'pos'),
  ('I do not like this restaurant', 'neg'),
  ('I am tired of this stuff.', 'neg'),
  ("I can't deal with this", 'neg'),
  ('he is my sworn enemy!', 'neg'),
  ('my boss is horrible.', 'neg')
]

test = [
  ('the beer was good.', 'pos'),
  ('I do not enjoy my job', 'neg'),
  ("I ain't feeling dandy today.", 'neg'),
  ("I feel amazing!", 'pos'),
  ('Gary is a friend of mine.', 'pos'),
  ("I can't believe I'm doing this.", 'neg')
]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

# classify method
print(cl.classify("This is amazing!"))

# probablity of class
prob_dist = cl.prob_classify("This one's a doozy.")
prob_dist.max()

round(prob_dist.prob("pos"), 2)
round(prob_dist.prob("neg"), 2)

# classify text blob
blob = TextBlob("I have good spelling!", classifier = cl)
blob.classify()

cl.accuracy(test)
cl.show_informative_features(5)

new_data = [
  ('She is my best friend.', 'pos'),
  ("I'm happy to have a new friend.", 'pos'),
  ("Stay thirsty, my friend.", 'pos'),
  ("He ain't from around here.", 'neg')
]

cl.update(new_data)
cl.accuracy(test)

