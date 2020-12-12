from handleVnText import * 
from sklearn.metrics import accuracy_score

listPuncKhrme =['ៗ', '។' ,'៕']

def splitDocByPunctuation(doc, listPunc, segment_length):
    doc = doc.replace("\n"," ")
    for punc in listPunc:
        doc = doc.replace(punc , "\n")
    listSegment = [ t for t in doc.split("\n") if t != '']
    result = [] 
    for segment in listSegment:
        result += splitDocToSegment(segment , segment_length)
    return result

def concateListtoObtainSegmentLength(listSegment , maxSegmentLength):
    
    if len(listSegment) == 0 :
        return []
    
    if len(listSegment) == 1:
        return listSegment
    
    else:
        start = 0 
        result = []
        temp  = [0]
        currentSumLength = len(listSegment[0])

        for i in range(1 , len(listSegment)):
            if len(listSegment[i]) + currentSumLength <= maxSegmentLength:
                temp.append(i)
                currentSumLength += len(listSegment[i])
            else:
                result.append(" . ".join([ listSegment[t] for t in temp]))
                temp = [i]
                currentSumLength = len(listSegment[i])
        result.append(" . ".join([listSegment[t] for t in temp]))

    return result


def readDocFromFile(file):
    with open(file , 'r') as f:
        data = f.read()
        data = data.replace("\n"," ")
    return data  

def writeDocToFile(data, file):
    with open(file , 'w') as f:
        f.write(data)

def readAndNormStopword():
    with open('stop_word.txt') as f:
        stopWords = f.readlines()
        stopWords = [norm_text(word.replace("\n","")) for word in stopWords]
    return stopWords

def creatPunc():
    punc = set(string.punctuation)
    list_punctuations_out = ['”', '”', "›", "“", '"' ,'...', '…']
    for e_punc in list_punctuations_out:
        punc.add(e_punc)
    return punc

def write_result_array(array , file):
	with open(file , "w") as f:
		result = "\n".join([ " ".join([ str(round(array[i][j] , 2)) for j in range(len(array[i]))])  for i in range(array.shape[0])])
		f.write(result)

def readLinesFromFile(file , delimiter = "\n"):
    with open(file , 'r') as f:
        lines = f.readlines()
        lines = [line.replace("\n","") for line in lines]
    return lines

def splitDocToSegment(doc, max_segment_size):
    characters = list(doc)
    start = 0 
    end = min(max_segment_size , len(characters))
    result = [doc[start:end]]
    while end < len(characters) : 
        start = end 
        end = min(start + max_segment_size , len(characters))
        result.append(doc[start :end])
    return result

def readListDocFromFileByDelimiter(file , delimiter = "#"):
    with open(file , 'r') as f :
        data = f.read()
    listDoc = data.split("#")
    return listDoc

def writeListDocToFile(listDoc , file):
    with open(file , 'w') as f:
        for i , doc in enumerate(listDoc):
            doc = doc.replace("<<<f>>>","")
            f.write( str(i) + "<<<f>>>" + removeSpecialCharacter(doc) + "\n")

def splitAndWriteDocToFileBySegmentLength(file_in , file_out , segmentLength = 500):
    lines  = readLinesFromFile(file_in)
    with open(file_out , 'w') as f:
        for line in lines :
            doc_id , doc_content = line.split("<<<f>>>")[0] , line.split("<<<f>>>")[1]
            _ = splitDocByPunctuation(doc_content, listPunc= listPuncKhrme , segment_length= segmentLength)
            listSegmentContent = concateListtoObtainSegmentLength(_ , maxSegmentLength = segmentLength)
            for segment in listSegmentContent:
                f.write(doc_id + "<<<f>>>" + segment + "\n")

def readAndConcateSegmentToDocFromFile(file_in , file_out):
    with open(file_out , "w") as f_w:
        with open(file_in, "r") as f_r:
            result = []
            for i, line in enumerate(f_r):
                line = line.replace("\n","")
                doc_id , doc_content = line.split("<<<f>>>")[0] , line.split("<<<f>>>")[1]
                if len(result) == 0:
                    current_idDoc = doc_id
                    result = [doc_content]
                else:
                    if doc_id == current_idDoc:
                        result.append(doc_content)
                    else:
                        #write current doc to file
                        f_w.write(" ".join(result) + "\n")
                        result = [doc_content]
                        current_idDoc = doc_id
            f_w.write(" ".join(result) + "\n")

def getPairDocFromResult(resultSimMatrix , listDoc_vn, listDoc_khrme , file_out , thresol = 0.9):
    with open(file_out , "w") as f:
        result = []
        for i in range(len(listDoc_vn)):
            result_temp_i = -1
            current_value_i = thresol
            for j in range(len(listDoc_khrme)):
                if resultSimMatrix[i][j] > current_value_i :
                    result_temp_i = j
                    current_value_i = resultSimMatrix[i][j]
            if result_temp_i > -1:
                result.append((i,result_temp_i))
        print(result)
        for pairIndex in result:
            f.write(listDoc_vn[pairIndex[0]] + "<<<f>>>" + listDoc_khrme[pairIndex[1]]+"\n")

def check_segmentUsingVocabVi(segment , vn_text):
    segment = segment.lower()
    list_word = segment.split("_")
    for word in list_word:
        if norm_text(word.lower()) not in vn_text:
            return False
    return True

def computeScoreThresol(result , label , thresol):
    label_true_flatten = label.flatten()
    label_predict = np.where(result < thresol , 0 , 1)
    label_predict_flatten = label_predict.flatten()
    return accuracy_score(label_true_flatten , label_predict_flatten)

def computeThresolFromResult(result):
    #result = matrix  n x m 
    
    #create matrix true label 
    label_matrix = np.zeros_like(result)
    list_index_label = [np.argmax(row) for row in result]
    for i in range(len(label_matrix)):
        label_matrix[i][list_index_label[i]] =  1
    list_thresol = list(np.arange(0. , 1., 0.02))
    return [ (thres ,computeScoreThresol(result, label_matrix , thres))  for thres in list_thresol]


# if __name__ == "__main__":
#     count = 0 
#     vocabVn = getVocabVn()
#     with open('word.txt' , 'r') as f_r :
#         with open('word_tokenize_vn.txt' , 'w') as f_w:
#             for word in f_r:
#                 count += 1
#                 print(count)
#                 word = word.replace("\n","").strip()
#                 if check_segmentUsingVocabVi(word , vocabVn) == True:
#                     f_w.write(word.lower()+"\n")