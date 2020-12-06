from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import rouge
import numpy as np
from handleVnText import * 

def get_cosine_sim(text): 
	vectors = [t for t in get_vectors(text)]
	return cosine_similarity(vectors)
	
def get_vectors(text):
	vectorizer = CountVectorizer(text)
	vectorizer.fit(text)
	return vectorizer.transform(text).toarray()

def compute_cosine_simListDoc(list1 , list2):
	result = np.zeros(shape = (len(list1) , len(list2)))
	for i in range(len(list1)):
		for j in range(len(list2)):
			result[i][j] = get_cosine_sim([ list1[i] , list2[j]  ])[0,1]
	return result

def computeCosinBowPairDoc(doc1, doc2):
	return get_cosine_sim( [doc1 , doc2])[0,1]

def readAndProcessDocForCosinBoW(file):
	with open(file, "r") as f:
		text = f.read()
		text = processDoc(text.replace("\n",""))
	return text

def computeCosinBowPairFile(file_1 , file_2):
	doc_1 = readAndProcessDocForCosinBoW(file_1)
	doc_2 = readAndProcessDocForCosinBoW(file_2)
	return computeCosinBowPairDoc(doc_1 , doc_2)

def jaccard_similarity(list1, list2):
	s1 = set(list1)
	s2 = set(list2)
	return float(len(s1.intersection(s2)) / len(s1.union(s2)))

def jaccardSimPairDoc(doc1 , doc2):
	list1 = doc1.split()
	list2= doc2.split()
	return jaccard_similarity(list1 , list2)

def jaccardSimListDoc(listDoc1, listDoc2):
	result = np.zeros(shape = (len(listDoc1) , len(listDoc2)))
	for i in range(len(listDoc1)):
		for j in range(len(listDoc2)):
			result[i][j] = jaccardSimPairDoc(listDoc1[i],listDoc2[j])
	return result

def compute_rouge_document(string1 , string2 ):
	evaluator = rouge.Rouge(metrics=['rouge-n'],
						   max_n=2,
						   limit_length=True,
						   length_limit=1000)
	scores = evaluator.get_scores(string1, string2)
	return scores['rouge-1']['f']

def compute_rouge_listDoc( list1 , list2):

	result = np.zeros(shape = (len(list1), len(list2)))
	for i in range(len(list1)):
		for j in range(len(list2)):
			result[i][j] = compute_rouge_document(list1[i] , list2[j])
	return result



# with open("test1/vn_translate.txt","r") as f:
# 	translates = f.readlines()
# 	translates = [processDoc(translate.replace("\n","")) for translate in translates]


# def write_result_array(array , file):

# 	with open(file , "w") as f:
# 		result = "\n".join([ " ".join([ str(round(array[i][j] , 2)) for j in range(len(array[i]))])  for i in range(array.shape[0])])
# 		f.write(result)

# write_result_array(compute_cosine_simListDoc(translates , raws) , "test1/result_test_1.txt")