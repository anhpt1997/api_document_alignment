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
