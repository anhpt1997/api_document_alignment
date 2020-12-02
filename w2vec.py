import gensim
from gensim.models import KeyedVectors
from handleVnText import * 
import numpy as np 

def readWord2Vec():
    word2vec_model = KeyedVectors.load_word2vec_format("../baomoi.model.bin", binary=True)
    return word2vec_model

def get_listWordByVocab(doc , annotator , vocab):
	listSegment = segment_doc(doc , annotator)
	return [t for t in listSegment if t in vocab.wv.vocab]

def listWordToVec(list_word , vocab):
	list_vecto = [vocab.wv[word] for word in list_word]
	list_vecto = np.asarray(list_vecto)
	return np.mean (list_vecto , axis = 0)

def doc2vec(text, annotator , vocab):
	list_word = get_listWordByVocab(text, annotator , vocab)
	return listWordToVec(list_word , vocab)


