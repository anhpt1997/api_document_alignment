import string
import re
import unicodedata

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

with open('stop_word.txt') as f:
	stopWords = f.readlines()
	stopWords = [norm_text(word.replace("\n","")) for word in stopWords]

def removeSpecialCharacter(text):
	text = text.replace("\r", " ")
	text = text.replace("\n"," ")
	text = text.replace("\t"," ")
	text = text.replace("\xa0", " ")
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
	doc = doc.replace("\n","")
	doc = doc.replace("\t","")
	doc = removePunc(doc)
	doc = norm_text(doc)
	doc = removeStopword(doc)
	doc = removeMultiSpaceToSpace(doc)
	return doc 
