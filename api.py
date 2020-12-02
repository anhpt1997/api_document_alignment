import sys
from utils import * 
from cosin_sim import * 

def document_align_api():

    file_vn_raw = sys.argv[1]
    file_khme_raw = sys.argv[2]

    listDoc_vn_raw = readListDocFromFile(file_vn_raw)
    listDoc_khrme_raw = readListDocFromFile(file_khme_raw)

    tranlate(listDoc_khrme_raw)

    listDoc_vn_translate = readListDocFromFile(file_vn_translate)

    resultMatrixSim = computeMatrixSimilarity(file_vn_raw , file_vn_translate)

    getPairDocFromResult()

    writePairDocToFile()

if __name__ == "__main__":
    document_align_api()