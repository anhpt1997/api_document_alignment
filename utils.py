from handleVnText import * 

def readDocFromFile(file):
    with open(file , 'r') as f:
        data = f.read()
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

def getPairDocFromResult():
    pass 

def writePairDocToFile():
    pass 

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

def splitAndWriteDocToFileBySegmentLength(file_in , file_out , segmentLength = 1000):
    lines  = readLinesFromFile(file_in)
    with open(file_out , 'w') as f:
        for line in lines :
            doc_id , doc_content = line.split("<<<f>>>")[0] , line.split("<<<f>>>")[1]
            listSegmentContent = splitDocToSegment(doc_content , max_segment_size= segmentLength)
            for segment in listSegmentContent:
                f.write(doc_id + "<<<f>>>" + segment + "\n")

def readAndConcateSegmentToDocFromFile(file_in , file_out):
    with open(file_out , "w") as f_w:
        with open(file_in, "r") as f_r:
            result = []
            for i, line in enumerate(f_r):
                print(line)
                doc_id , doc_content = line.split("<<<f>>>")[0] , line.split("<<<f>>>")[1]
                if len(result) == 0:
                    current_idDoc = doc_id
                    result = [doc_content]
                else:
                    if doc_id == current_idDoc:
                        result.append(doc_content)
                    else:
                        #write current doc to file
                        f_w.write(current_idDoc + "<<<f>>>" + " ".join(result) + "\n")
                        result = [doc_content]
                        current_idDoc = doc_id
            f_w.write(current_idDoc + "<<<f>>>" + " ".join(result) + "\n")

    

# listDoc = readListDocFromFileByDelimiter("1.txt")
# writeListDocToFile(listDoc , '2.txt')
# splitAndWriteDocToFileBySegmentLength(file_in = '2.txt' , file_out = '3.txt' , segmentLength=1000)
readAndConcateSegmentToDocFromFile('3.txt','4.txt')