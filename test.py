
from utils import * 
from w2vec import * 
from handleVnText import *
from segment import * 
from comparePairDoc import * 

w2vecmodel = getWord2Vec()
annotator  = getAnnotator()

path_src = 'test_raw_vn.txt'
path_tgt = 'data/file_vn_translated_indexed.txt'
src = readAndProcessDocForCosinBoW(path_src)
tgt = readAndProcessDocForCosinBoW(path_tgt)
# list_src = [t.strip() for t in src.split()]
# list_tgt = [t.strip() for t in tgt.split()]
# a = [t for t in list_src if t not in w2vecmodel.vocab]
# b = [t for t in list_tgt if t not in w2vecmodel.vocab]

print(compute_rouge_document(src , tgt))
# print(a)
# print(b)
# print([t for t in list_src if t not in list_tgt])
# print(len([t for t in list_src if t not in list_tgt]) , len(list_src))
#doc = readDocFromFile(path)
#list_segment = segment_doc(doc , annotator)
#print(list_segment)
#print( 'oov ' ,  [word  for word in list_segment if word not  in w2vecmodel.vocab])
#print('quân_ủy' in w2vecmodel.vocab)
#segment = 'kề_vai'
#print ( 'kề_vai'  in w2vecmodel.vocab , 'sát_cánh' in w2vecmodel.vocab)
#a = sum( [ wordPieceForSegment(segment , w2vecmodel.vocab) for segment in list_segment] , [])
#print(a)
#print('oov ', [word  for word in a  if word not  in w2vecmodel.vocab])
