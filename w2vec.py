import gensim
from gensim.models import KeyedVectors
from handleVnText import * 
import numpy as np 

def getWord2Vec():
    word2vec_model = KeyedVectors.load_word2vec_format("../baomoi.model.bin", binary=True)
    return word2vec_model

def get_listWordByVocab(doc , annotator , vocab):
	listSegment = segment_doc(doc , annotator)
	return sum( [ wordPieceForSegment(segment , vocab.vocab) for segment in listSegment] , [])

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
				#print('vec ooV ', vecOOV)
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

def wordPieceForSegment(segment , vocab_words):

    def splitSegmentToPairSegment(list_word , vocab_words):
        # a_b_c --> a_b and c with a_b in vocab , c in vocab
        #print('len segment ', len(list_word))
        if len(list_word) == 0:
            return 0 
        reverse_list_word = list_word[::-1]
        split_index = 0
        for i in range(len(list_word)):
            if "_".join(reverse_list_word[i:][::-1]) in vocab_words:
                break
        return i
    
    if len(segment.split("_")) == 0:
        return []
    
    if len(segment.split("_")) == 1:
        return [segment]

    return_index = -1
    sub_segments = []
    next_segment = segment.split("_")
    while len(next_segment) != 0 and len(next_segment) != 1:
        next_index = splitSegmentToPairSegment(next_segment , vocab_words)
        sub_segments.append(next_segment[:len(next_segment)-next_index])
        next_segment = next_segment[len(next_segment)-next_index : ]
    if len(next_segment) != 0:
        sub_segments.append(next_segment)
   
    return [ "_".join(subsegment)  for subsegment in sub_segments]
