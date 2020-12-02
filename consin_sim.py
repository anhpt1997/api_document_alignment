from scipy import spatial


def cosinSimilarity(vec1 , vec2):
	return 1 - spatial.distance.cosine(vec1, vec2)

def computelistCosinSimilarity(listdoc1 , listDoc2):
	result = np.zeros(shape =(len(listdoc1) , len(listDoc2)))
	for i in range(len(listdoc1)):
		for j in range(len(listDoc2)):
			result[i][j] = cosinSimilarity(doc2vec(listdoc1[i]) , doc2vec(listDoc2[j]))
	return result