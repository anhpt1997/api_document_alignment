import gensim
from gensim.models import KeyedVectors
from handleVnText import * 
import numpy as np 

def getWord2Vec():
    word2vec_model = KeyedVectors.load_word2vec_format("../baomoi.model.bin", binary=True)
    return word2vec_model

def get_listWordByVocab(doc , annotator , vocab):
	listSegment = segment_doc(doc , annotator)
	return [t for t in listSegment ]

# def listWordToVec(list_word , vocab):
# 	list_vecto = [vocab.wv[word] for word in list_word if word in vocab.vocab ]
# 	list_vecto = np.asarray(list_vecto)
# 	return np.mean (list_vecto , axis = 0)
def listWordToVec(list_word , vocab , handleOOV = False):
	if handleOOV == False:
		list_vecto = [vocab.wv[word] for word in list_word if word in vocab.vocab ]
		if len(list_vecto) == 0:
			return np.zeros_like(vocab.wv['a'])
		else:
			list_vecto = np.asarray(list_vecto)
			return np.mean (list_vecto , axis = 0)
	else:
		result = np.zeros_like(vocab.wv['a'])
		count = 0 
		for word in list_word:
			if word in vocab.vocab:
				result += vocab.wv[word]
				count += 1
			else:
				#word is oov
				word = word.replace("_", " ")
				vecOOV = wordOOVtovec(word , vocab)
				print('vec ooV ', vecOOV)
				if len(vecOOV) != 0:
					count += 1 
					result += vecOOV
		return result / count 

def doc2vec(text, annotator , vocab , handleOOV = False):
	list_word = get_listWordByVocab(text, annotator , vocab)
	return listWordToVec(list_word , vocab , handleOOV=handleOOV)

def wordOOVtovec(word, vocab):
	listchar = list(word)
	listvecto = [vocab.wv[c] for c in listchar if c in vocab.vocab] 
	if len(listvecto) == 0 :
		return []
	else:
		return np.mean(np.asarray([vocab.wv[c] for c in listchar if c in vocab.vocab] )  , axis = 0 )



