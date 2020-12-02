from scipy import spatial
from w2vec import * 

def cosinSimilarity(vec1 , vec2):
	return 1 - spatial.distance.cosine(vec1, vec2)

def computeMatrixSimilarity(listdoc1 , listDoc2, annotator , vocab):
	result = np.zeros(shape =(len(listdoc1) , len(listDoc2)))
	for i in range(len(listdoc1)):
		for j in range(len(listDoc2)):
			vec1 = doc2vec(listdoc1[i] , annotator , vocab)
			vec2 = doc2vec(listDoc2[j] , annotator , vocab)
			result[i][j] = cosinSimilarity(vec1 , vec2)
	return result