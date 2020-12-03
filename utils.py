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

def readListDocFromFile(file , delimiter = "\n"):
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

def splitAndWriteDocToFileBySegmentLength():
    pass 

def readAndConcateSegmentToDocFromFile(file):
    pass

listDoc = readListDocFromFileByDelimiter("1.txt")
writeListDocToFile(listDoc , '2.txt')