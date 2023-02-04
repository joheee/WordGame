import nltk, string, random
from nltk.corpus import brown, stopwords, words, wordnet
from nltk.tree import Tree
from nltk.stem import WordNetLemmatizer

nltk.download('brown')

def printArr(arr):
    for w in arr:
        print(w)

def cleanData(list_word):
    #stopwords
    stops = set(stopwords.words('english'))
    quote = ['""',"''",'``','--']
    #separate by stopwords, punctuation, and number
    list_word_after_stopwords = [word for word in list_word if word.lower() not in stops]
    list_word_removed_punctuation = [token for token in list_word_after_stopwords if token not in string.punctuation]
    list_word_removed_punctuation = [token for token in list_word_removed_punctuation if token not in quote]
    list_word_removed_punctuation = [item for item in list_word_removed_punctuation if item.isalpha()]
    return list_word_removed_punctuation

#POS tagging and NER
def cleanChunk(list_word_final):
    chunked = nltk.ne_chunk(nltk.pos_tag(list_word_final))
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        if current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    
    list_word_final = [item for item in list_word_final if item not in continuous_chunk]
    return [s.lower() for s in list_word_final]

#set pos tagging for determine the lemma
def getPos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

#stem or lemma based on user's option
def setLemma(list_word_final):
    lemma = WordNetLemmatizer()
    tagged = nltk.pos_tag(list_word_final)
    container = []
    for word, tag in tagged:
        wntag = getPos(tag)
        if wntag is None:# not supply tag in case of None
            container.append(lemma.lemmatize(word))
        else:
            container.append(lemma.lemmatize(word, pos=wntag))
    return container

#get synonim and antonym
def getSynonimAntonym(list_word_final):
    synonyms = []
    antonyms = []
    for w in list_word_final:
        for syn in wordnet.synsets(w):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    return set(synonyms + antonyms + list_word_final)

def getDefinition(word):
    syns = wordnet.synsets(word)
    if len(syns) is 0:
        return [],[]
    return syns[0].definition(), syns[0].examples()

def initData():
    #load and tokenize with brown
    list_word_news = brown.words(categories='religion')
    list_word_romance = brown.words(categories='romance')

    list_word_final = list_word_news + list_word_romance
    list_word_final = cleanData(list_word_final)

    list_word_final = cleanChunk(list_word_final)
    list_word_final = setLemma(list_word_final)

    list_word_final = getSynonimAntonym(list_word_final)
    list_word_final = cleanData(list_word_final)
    return list_word_final

def getRandomWord(list_words):
    choosen = random.choice(list_words)
    meaning = getDefinition(choosen)
    if len(choosen) < 4 or meaning[0] == '' or len(meaning[1]) == 0:
        return getRandomWord(list_words)
    return choosen, meaning[0], meaning[1]

def getMaskingWord(word):
    i = len(word)
    buff = int(i / 2)
    word = list(word)
    
    idx = set([])
    while True:
        idx.add(random.randint(0,i-1))
        if len(idx) == buff:
            break
    for i in idx:
        word[i] = '_'
    return ''.join(word)