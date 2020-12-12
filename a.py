import sys
from pyvi import ViTokenizer
# def isDoc(line):
#     if line == '\n':
#         return True 
#     else:
#         line = line.replace("\n","").strip()
#         if '------' in line:
#             return False
#         else:
#             return True 

# f_in = sys.argv[1]
# f_out = sys.argv[2]
# def read_listDocFromFile(path_in , path_out):
#     current_doc = []
#     with open(path_in , 'r') as f_in:
#         with open(path_out , 'w') as f_out:
#             for line in f_in:
#                 if isDoc(line) == True:
#                     current_doc.append(line.replace("\n",""))
#                 else:
#                     if len(current_doc) > 0 :
#                         f_out.write(" ".join(current_doc) + "\n")
#                     current_doc = []
#             f_out.write(" ".join(current_doc))

# read_listDocFromFile(f_in , f_out)
# def b(file):
#     count = 0 
#     with open(file , 'r') as f_r:
#         for line in f_r :
#             if '----------' in line :
#                 count += 1
#                 print(line)
#                 print(count)
#     print('count ', count)

#b(f_in)
print(ViTokenizer.tokenize(u"Trường đại học bách khoa hà nội"))