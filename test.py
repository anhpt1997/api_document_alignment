
from utils import * 
from w2vec import * 
from handleVnText import *
from comparePairDoc import * 
import numpy as np 
from pyvi import ViTokenizer as annotator

w2vecmodel = getWord2Vec()
"""
path_src = 'test_raw_vn.txt'
path_tgt = 'data/file_vn_translated_indexed.txt'
text1 = readAndProcessDocForCosinBoW(path_src)
text2 = readAndProcessDocForCosinBoW(path_tgt)
score_1 = computeCosinBowPairDoc(text1 , text2)
print('score 1 ', score_1)

text3 = readDocFromFile(path_src)
text4 = readDocFromFile(path_tgt)
list_word_src = get_listWordByVocab(text3 , annotator , w2vecmodel)
list_word_tgt = get_listWordByVocab(text4 , annotator , w2vecmodel)
print(list_word_src)
print(list_word_tgt)
score_2 = computeCosinBowPairDoc(" ".join(list_word_src) , " ".join(list_word_tgt))
print(score_2)
"""
import sys 
def main():
    f_1 = sys.argv[1]
    f_2 = sys.argv[2]
    f_3 = sys.argv[3]
    count = 0 
    with open(f_3 , 'w' ) as f_w:
        with open(f_1 , 'r') as f_src:
            for src in f_src:
                count += 1
                print('count' , count)
                temp = [] 
                src = handleDocUsingVocab(src, annotator , w2vecmodel)
                with open(f_2 , 'r') as f_tgt:
                    for tgt in f_tgt:
                        tgt = handleDocUsingVocab(tgt, annotator , w2vecmodel)
                        temp.append(str(computeCosinBowPairDoc(src , tgt)))
                    f_w.write( " ".join(temp) + "\n")
# data = np.loadtxt('result.txt')
# print(data)
# for row in data:
#     print(sorted(row , reverse=True)[:5])
if __name__ == "__main__":
    main()