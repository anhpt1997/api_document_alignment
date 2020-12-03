import sys
from utils import * 
from cosin_sim import * 
from w2vec import * 
from segment import * 
from translate import * 

def document_align_api():

    file_vn_raw = sys.argv[1]
    file_khme_raw = sys.argv[2]
    file_vn_translate = sys.argv[3]

    listDoc_vn_raw = readListDocFromFile(file_vn_raw)
    listDoc_khrme_raw = readListDocFromFile(file_khme_raw)

    translate(file_in = file_khme_raw , file_out = file_vn_translate)

    listDoc_vn_translate = readListDocFromFile(file_vn_translate)

    # listDoc_vn_raw = readListDocFromFile(file = "test_raw_vn.txt")
    # listDoc_vn_translate = readListDocFromFile(file = "test_translate_vn.txt")

    # vocabW2vec = getWord2Vec()

    # annotator = getAnnotator()

    # resultMatrixSim = computeMatrixSimilarityPairListDoc( listDoc_vn_raw , listDoc_vn_translate , annotator , vocabW2vec)

    # print(resultMatrixSim)

    # getPairDocFromResult()

    # writePairDocToFile()

if __name__ == "__main__":
    document_align_api()