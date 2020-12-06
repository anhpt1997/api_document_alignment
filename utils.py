from handleVnText import * 

listPuncKhrme =['ៗ', '។' ,'៕']


def splitDocByPunctuation(doc, listPunc, segment_length):
    doc = doc.replace("\n","")
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

def splitAndWriteDocToFileBySegmentLength(file_in , file_out , segmentLength = 1000):
    lines  = readLinesFromFile(file_in)
    with open(file_out , 'w') as f:
        for line in lines :
            doc_id , doc_content = line.split("<<<f>>>")[0] , line.split("<<<f>>>")[1]
            _ = splitDocByPunctuation(doc_content, listPunc= listPuncKhrme , segment_length= segmentLength)
            listSegmentContent = concateListtoObtainSegmentLength(_ , maxSegmentLength = 1000)
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



# string = """នារសៀលថ្ងៃទី៤ ធ្នូ ឧបនាយករដ្ឋមន្រ្តីនិងជារដ្ឋមន្រ្តីការបរទេសវៀត ណាមលោក Pham Binh Minh និងរដ្ឋមន្ត្រីការបរទេសន័រវេស លោកស្រី Marie Eriksen Soreide បានជួបពិភាក្សាការងារតាមប្រព័ន្ធវីដេអូ អំពីស្ថាន ភាពទំនាក់ទំនងរវាងប្រទេសទាំងពីរ និងកិច្ចសហប្រតិបត្តិការនៅក្រុម ប្រឹក្សាសន្តិសុខអង្គការសហប្រជាជាតិក្នុងឆ្នាំ២០២១ ពេលដែលន័រវេសចាប់ ផ្ដើមកាន់តំណែងជាសមាជិកមិនអចិន្រ្តៃយ៍នៃក្រុមប្រឹក្សាសន្តិសុខ។ ភាគី ទាំងពីរបានវាយតម្លៃខ្ពស់ចំពោះការអភិវឌ្ឍនៃទំនាក់ទំនងទ្វេភាគីនាពេល កន្លងមក ព្រមទាំងឯកភាពលើការថែរក្សានិងពង្រីកកិច្ចសហប្រតិបត្តិការ លើវិស័យសេដ្ឋកិច្ច ពាណិជ្ជកម្ម វិនិយោគ ជាពិសេសគឺវិស័យដែល ប្រទេសទាំងពីរមានឧត្តមភាពដូចជា ការចិញ្ចឹមជលផល ថាមពលស្អាត ការស្រាវជ្រាវវិទ្យាសាស្ត្រសមុទ្រ កិច្ចការពារបរិស្ថានសមុទ្រ និងប្រេង ឧស្ម័ន ជាដើម។ រដ្ឋមន្រ្តីការបរទេសទាំងពីររូបបានអះអាងថា ភាគីទាំងពីរ នឹងបន្តរក្សានិងបង្កើនយន្តការពិគ្រោះយោបល់ សំដៅចែករំលែកព័ត៌មាន ទស្សនៈទៅវិញទៅមក ស្វែងរកសម្លេងរួមនិងជំរុញការមូលមតិឯកឆន្ទ ក្នុង ការដោះស្រាយបញ្ហានានានៅក្នុងក្របខ័ណ្ឌក្រុមប្រឹក្សាសន្តិសុខអ.ស.បផងដែរ៕"""

# listSegment  = splitDocByPunctuation(string , listPunc , 1000)
# for i, segment in enumerate(listSegment):
#     print( i, "   ", segment, len(segment))

# listSegment = ['abc','def','fdfsd','frgthjkli']
# print(concateListtoObtainSegmentLength(listSegment , 10))