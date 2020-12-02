from handleVnText import * 
import pickle
import numpy as np 
from w2vec import * 
from utils import * 
from segment_api import * 

vocab = readWord2Vec()

keys = vocab.wv.vocab

annotator = getAnnotator()

text1 = """Cải cách WTO để ứng phó với tình hình mới. Ban Thư ký Tổ chức Thương mại Thế giới (WTO) vừa tổ chức hội thảo trực tuyến với sự tham gia của đại diện cấp cao các nước, tổ chức quốc tế và cộng đồng doanh nghiệp, tổ chức xã hội và giới truyền thông nhằm thảo luận về tác động của WTO trong 25 năm qua. Quá khứ và những vấn đề mà WTO phải giải quyết trong những năm tới để đảm bảo một hệ thống thương mại công bằng. Tại hội thảo, các diễn giả nhấn mạnh hệ thống thương mại thế giới dựa trên quy tắc tiếp tục đóng vai trò quan trọng, thể hiện ở vai trò then chốt của thương mại quốc tế trong việc ứng phó với đại dịch Kovid 19. Hội thảo cũng cho rằng cần ưu tiên cải cách WTO. Diễn giả cũng đề cập đến vai trò của Tổ chức Thương mại Thế giới trong tương lai như thúc đẩy hòa bình, bảo vệ trái đất và hướng tới mục tiêu phát triển bền vững. 
"""

seg = segment_doc(text1 , annotator)

s2 = get_listWordByVocab(text1 , annotator , keys)

# with open("../test1/vn_raw.txt" , "r") as f:
# 	raws = f.readlines()
# 	raws =[processDoc(raw.replace("\n","")) for raw in raws]

# with open("../test1/vn_translate.txt","r") as f:
# 	translates = f.readlines()
# 	translates = [processDoc(translate.replace("\n","")) for translate in translates]

# write_result_array(computelistCosinSimilarity(translates , raws) , "result_sentence.txt")

# l = get_listWordByVocab(text1)
# l2 = segment_doc(text1)
# l2 = get_listWordByVocab(text2)
print(seg)
print(s2)