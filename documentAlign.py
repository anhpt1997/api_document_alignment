

def computeMatrixSim(listDoc1 , listDoc2):
    
    vocab = readWord2Vec()

    stopWords = readAndNormStopword()

    punc = creatPunc()

    annotator = getAnnotator()
