import sys
from utils import * 
from cosin_sim import * 
from w2vec import * 
from segment import * 
from google_translate.run_translate import * 
from comparePairDoc import * 
from pyvi import ViTokenizer as annotator

def document_align_api():

    file_vn_raw = sys.argv[1]
    file_khme_raw = sys.argv[2]
    src_lg = sys.argv[3]

    listDoc_vn_raw = readLinesFromFile(file_vn_raw)
    listDoc_khrme_raw = readLinesFromFile(file_khme_raw)

    #convert doc -->[doc]
    # listDoc_vn_raw = [listDoc_vn_raw]
    # listDoc_khrme_raw = [listDoc_khrme_raw]
    
    writeListDocToFile(listDoc_vn_raw , 'file_vn_raw_indexed.txt')
    writeListDocToFile(listDoc_khrme_raw , 'file_khrme_raw_indexed.txt')

    splitAndWriteDocToFileBySegmentLength(file_in = 'file_khrme_raw_indexed.txt' , file_out = 'data/file_khrme_raw_indexed_segmented.txt' , segmentLength= 800)

    print('translating ......')
    translate_file(file_in = 'data/file_khrme_raw_indexed_segmented.txt' , file_out = 'data/file_khrme_raw_indexed_segmented_translated.txt'  ,src_lg= src_lg , dest_lg='vi')
    
    readAndConcateSegmentToDocFromFile(file_in = 'data/file_khrme_raw_indexed_segmented_translated.txt' , file_out ='data/file_vn_translated_indexed.txt')
    # listDoc_vn_raw = readListDocFromFile(file = "test_raw_vn.txt")


    # w2vecmodel = getWord2Vec()

    # annotator = getAnnotator()

    #resultMatrixSim1  = computeMatrixSimilarityPairListDoc( listDoc_vn_raw , listDoc_vn_translate , annotator , vocabW2vec , handleOOV=False)

    #resultMatrixSim2  = computeMatrixSimilarityPairListDoc( listDoc_vn_raw , listDoc_vn_translate , annotator , vocabW2vec , handleOOV=True)

    # print('computing cosin bag of word .....')
    # result = computeCosinBowPairFile(file_vn_raw , 'data/file_vn_translated_indexed.txt', annotator , w2vecmodel)

    # print(result)

    #print(resultMatrixSim1[0][0])

    #print(resultMatrixSim2[0][0])

    # getPairDocFromResult(resultMatrixSim , listDoc_vn_raw , listDoc_khrme_raw, 'result/resultDocAlign.txt', thresol= 0.9)


if __name__ == "__main__":
    document_align_api()
