import nltk
import random
from nltk.corpus import movie_reviews, stopwords

documents = [(set(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

stop_words = stopwords.words('english')

all_words = []

for w in movie_reviews.words():
    if w not in stop_words:
        all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = all_words.most_common(3000)


def find_features(review_words):
    features = {}
    for w in word_features:
        # check if word available in review_words
        features[w] = (w in review_words)

    return features


featuresets = [(find_features(review_words), category) 
                for (review_words, category) in documents]


training_set = featuresets[:1900]
test_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

accuracy = nltk.classify.accuracy(classifier, test_set) * 100

classifier.show_most_informative_features(15)


