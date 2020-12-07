import string
import re
import unicodedata
from utils import * 

def norm_text(text):
	text = unicodedata.normalize('NFC', text)
	text = re.sub(r"òa", "oà", text)
	text = re.sub(r"óa", "oá", text)
	text = re.sub(r"ỏa", "oả", text)
	text = re.sub(r"õa", "oã", text)
	text = re.sub(r"ọa", "oạ", text)
	text = re.sub(r"òe", "oè", text)
	text = re.sub(r"óe", "oé", text)
	text = re.sub(r"ỏe", "oẻ", text)
	text = re.sub(r"õe", "oẽ", text)
	text = re.sub(r"ọe", "oẹ", text)
	text = re.sub(r"ùy", "uỳ", text)
	text = re.sub(r"úy", "uý", text)
	text = re.sub(r"ủy", "uỷ", text)
	text = re.sub(r"ũy", "uỹ", text)
	text = re.sub(r"ụy", "uỵ", text)
	text = re.sub(r"Ủy", "Uỷ", text)
	return text


# Storing the sets of punctuation in variable result
punc = set(string.punctuation)
list_punctuations_out = ['”', '”', "›", "“", '"' ,'...', '…']
for e_punc in list_punctuations_out:
	punc.add(e_punc)

def getVocabVn():
    with open('all-vietnam.txt' , 'r') as f:
        words = f.readlines()
        words =[norm_text(word.replace("\n",""))  for word in words]
    return words

vocabVn = getVocabVn()

with open('stop_word.txt') as f:
	stopWords = f.readlines()
	stopWords = [norm_text(word.replace("\n","")) for word in stopWords]

def removeSpecialCharacter(text):
	text = text.replace("\r", " ")
	text = text.replace("\n"," ")
	text = text.replace("\t"," ")
	text = text.replace("\xa0", " ")
	text = text.replace("\u200b" , " ")
	text = removeMultiSpaceToSpace(text)
	return text

def removeMultiSpaceToSpace(string):
	return re.sub(' +', ' ', string)

def removeStopword(doc):
	tokens = doc.split()
	return " ".join([word for word in tokens if word not in stopWords])

def insertSpaceToPunce(string):
	result = ""
	for c in string:
		if c not in punc:
			result += c
		else:
			result += " " + c + " "
	return result	

def removePunc(string):
	result = ""
	for c in string:
		if c not in punc:
			result += c
		else:
			result += " "
	return result

def processDoc(doc):
	doc = doc.lower()
	doc = removeSpecialCharacter(doc)
	doc = removePunc(doc)
	doc = norm_text(doc)
	doc = removeStopword(doc)
	doc = removeMultiSpaceToSpace(doc)
	return doc 

def removeStopwordFromListString(list):
    return [t for t in list if t.lower() not in stopWords]

def removePuncFromListString(list):
    return [t for t in list if t not in punc]

def segment_doc(text1 , annotator):
	text1 = norm_text(text1)
	text1 = insertSpaceToPunce(text1)
	text1 = removeSpecialCharacter(text1)
	word_segmented_text1 = annotator.tokenize(text1) 
	a = sum(word_segmented_text1 , [])
	a = removeStopwordFromListString(a)
	a = removePuncFromListString(a)
	a = [word.lower() for word in a]
	return a

def handleOOV(doc):
    words = doc.split()
    result = []
    for word in words:
        if word in vocabVn:
            result.append(word)
        else:
            result += list(word)
    return result


