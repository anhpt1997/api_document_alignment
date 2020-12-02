from vncorenlp import VnCoreNLP

def getAnnotator():
    annotator = VnCoreNLP(address="http://127.0.0.1", port=9000) 
    return annotator