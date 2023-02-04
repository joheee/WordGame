import nltk 
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('webtext')
nltk.download('treebank')

from nltk.book import FreqDist
from nltk.tokenize import word_tokenize
import Riddlez as rz

#frequency distribution
def getMostInputtedWord(text):
    list_text = word_tokenize(text)
    fd = FreqDist(list_text)
    final_result = dict(fd)
    res = max(final_result, key=final_result.get)
    return res, rz.getDefinition(res)

#input harus 4 huruf minimal
def isInputValid(text):
    text = word_tokenize(text)
    if len(text) >= 4:
        return True
    return False