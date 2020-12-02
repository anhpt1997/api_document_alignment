from handleVnText import * 
import pickle
from scipy import spatial
import numpy as np 
from w2vec import * 
from utils import * 
from segment_api import * 

vocab = readWord2Vec()

stopWords = readAndNormStopword()

punc = creatPunc()

annotator = getAnnotator()

def removeStopwordFromListString(list):
    return [t for t in list if t.lower() not in stopWords]

def removePuncFromListString(list):
    return [t for t in list if t not in punc]

text1 = """Cải cách WTO để ứng phó với tình hình mới. Ban Thư ký Tổ chức Thương mại Thế giới (WTO) vừa tổ chức hội thảo trực tuyến với sự tham gia của đại diện cấp cao các nước, tổ chức quốc tế và cộng đồng doanh nghiệp, tổ chức xã hội và giới truyền thông nhằm thảo luận về tác động của WTO trong 25 năm qua. Quá khứ và những vấn đề mà WTO phải giải quyết trong những năm tới để đảm bảo một hệ thống thương mại công bằng. Tại hội thảo, các diễn giả nhấn mạnh hệ thống thương mại thế giới dựa trên quy tắc tiếp tục đóng vai trò quan trọng, thể hiện ở vai trò then chốt của thương mại quốc tế trong việc ứng phó với đại dịch Kovid 19. Hội thảo cũng cho rằng cần ưu tiên cải cách WTO. Diễn giả cũng đề cập đến vai trò của Tổ chức Thương mại Thế giới trong tương lai như thúc đẩy hòa bình, bảo vệ trái đất và hướng tới mục tiêu phát triển bền vững. 
"""

def segment_doc(text1):
	text1 = norm_text(text1)
	text1 = insertSpaceToPunce(text1)
	text1 = removeSpecialCharacter(text1)
	word_segmented_text1 = annotator.tokenize(text1) 
	a = sum(word_segmented_text1 , [])
	a = removeStopwordFromListString(a)
	a = removePuncFromListString(a)
	a = [word.lower() for word in a]
	return a 

def get_listWordByVocab(doc):
	listSegment = segment_doc(doc)
	return [t for t in listSegment if t in vocab]

def cosinSimilarity(vec1 , vec2):
	return 1 - spatial.distance.cosine(vec1, vec2)

def listWordToVec(list_word):
	list_vecto = [vocab[word] for word in list_word]
	list_vecto = np.asarray(list_vecto)
	return np.mean (list_vecto , axis = 0)

def doc2vec(text):
	list_word = get_listWordByVocab(text)
	return listWordToVec(list_word)

def computelistCosinSimilarity(listdoc1 , listDoc2):
	result = np.zeros(shape =(len(listdoc1) , len(listDoc2)))
	for i in range(len(listdoc1)):
		for j in range(len(listDoc2)):
			result[i][j] = cosinSimilarity(doc2vec(listdoc1[i]) , doc2vec(listDoc2[j]))
	return result


with open("../test1/vn_raw.txt" , "r") as f:
	raws = f.readlines()
	raws =[processDoc(raw.replace("\n","")) for raw in raws]

with open("../test1/vn_translate.txt","r") as f:
	translates = f.readlines()
	translates = [processDoc(translate.replace("\n","")) for translate in translates]

# write_result_array(computelistCosinSimilarity(translates , raws) , "result_sentence.txt")

l = get_listWordByVocab(text1)
l2 = segment_doc(text1)
# l2 = get_listWordByVocab(text2)
print(l)
print(l2)
print([t for t in l2 if t not in l])