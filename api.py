import sys
from utils import * 
from cosin_sim import * 
from w2vec import * 
from segment import * 
from google_translate.run_translate import * 

def document_align_api():

    file_vn_raw = sys.argv[1]
    file_khme_raw = sys.argv[2]
    src_lg = sys.argv[3]

    listDoc_vn_raw = readDocFromFile(file_vn_raw)
    listDoc_khrme_raw = readDocFromFile(file_khme_raw)

    #convert doc -->[doc]
    listDoc_vn_raw = [listDoc_vn_raw]
    listDoc_khrme_raw = [listDoc_khrme_raw]

    writeListDocToFile(listDoc_vn_raw , 'file_vn_raw_indexed.txt')
    writeListDocToFile(listDoc_khrme_raw , 'file_khrme_raw_indexed.txt')

    splitAndWriteDocToFileBySegmentLength(file_in = 'file_khrme_raw_indexed.txt' , file_out = 'data/file_khrme_raw_indexed_segmented.txt' , segmentLength= 500)

    translate_file(file_in = 'data/file_khrme_raw_indexed_segmented.txt' , file_out = 'data/file_khrme_raw_indexed_segmented_translated.txt'  ,src_lg= src_lg , dest_lg='vi')

    readAndConcateSegmentToDocFromFile(file_in = 'data/file_khrme_raw_indexed_segmented_translated.txt' , file_out ='data/file_vn_translated_indexed.txt')
    # listDoc_vn_raw = readListDocFromFile(file = "test_raw_vn.txt")
    listDoc_vn_translate = readLinesFromFile('data/file_vn_translated_indexed.txt')

    vocabW2vec = getWord2Vec()

    annotator = getAnnotator()

    resultMatrixSim = computeMatrixSimilarityPairListDoc( listDoc_vn_raw , listDoc_vn_translate , annotator , vocabW2vec)

    print(resultMatrixSim[0][0])

    getPairDocFromResult(resultMatrixSim , listDoc_vn_raw , listDoc_khrme_raw, 'result/resultDocAlign.txt', thresol= 0.9)


if __name__ == "__main__":
    document_align_api()