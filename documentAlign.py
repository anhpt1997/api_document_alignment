from handleVnText import * 
import pickle
import numpy as np 
from w2vec import * 
from utils import * 
from segment_api import * 

def computeMatrixSim(listDoc1 , listDoc2):

    vocab = readWord2Vec()

    stopWords = readAndNormStopword()

    punc = creatPunc()

    annotator = getAnnotator()

    s2 = get_listWordByVocab(text1 , annotator , keys)
