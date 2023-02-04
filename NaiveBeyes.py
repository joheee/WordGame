from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.book import FreqDist
from nltk.classify import NaiveBayesClassifier, accuracy
import nltk, string, random, pickle, Riddlez as rz, os

negative = brown.sents(categories='romance')
positive = brown.sents(categories='religion')

negative = [[' '.join(i)] for i in negative]
positive = [[' '.join(i)] for i in positive]

negative_without_punc = []
for w in negative:
    temp = w[0].translate(str.maketrans('', '', string.punctuation))
    temp = temp.replace("'", '')
    temp = temp.replace('"', '')
    negative_without_punc.append(temp)

positive_without_punc = []
for w in positive:
    temp = w[0].translate(str.maketrans('', '', string.punctuation))
    temp = temp.replace("'", '')
    temp = temp.replace('"', '')
    positive_without_punc.append(temp)

labeled_sentence = []
for s in negative_without_punc:
    labeled_sentence.append((s, 'neg'))
for s in positive_without_punc:
    labeled_sentence.append((s, 'pos'))

#get 6000 words
list_words = rz.initData()
fd = FreqDist(list_words)
list_words = [word for word in fd.most_common(6000)]

#make dataset
dataset = []
for s, l in labeled_sentence:
    dict = {}
    words = word_tokenize(s)
    for f in list_words:
        key = f
        value = f in words
        dict[key] = value
    dataset.append((dict,l))

#shuffle and divide training with testing ratio
random.shuffle(dataset)
counter = int(len(dataset) * 0.7)
training_data = dataset[:counter]
testing_data = dataset[counter:]

def initNaiveBayes(training_data):
    #naive bayes algorithm
    classifier = NaiveBayesClassifier.train(training_data)
    return classifier

def saveTrainedModel(classifier):
    #save trained model
    file = open('model.pickle', 'wb')
    pickle.dump(classifier, file)
    file.close()
    print('heheheeuy')

def getSavedTrainedModel():

    #if model.pickle is not exists
    if not os.path.exists('model.pickle'):
        saveTrainedModel(initNaiveBayes(training_data))

    #open model.pickle
    file = open('model.pickle', 'rb')
    classifier = pickle.load(file)
    file.close()
    acc = accuracy(classifier, testing_data) * 100
    return acc, len(dataset), len(training_data), len(testing_data)