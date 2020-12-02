import gensim
from gensim.models import KeyedVectors
from handleVnText import * 

def readWord2Vec():
    word2vec_model = KeyedVectors.load_word2vec_format("../baomoi.model.bin", binary=True)
    return word2vec_model