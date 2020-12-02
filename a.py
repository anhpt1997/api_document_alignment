import gensim
from gensim.models import KeyedVectors
from handleVnText import * 

# with open("w2vec.txt","w") as f:
#     result = []
#     for i, key in enumerate(keys) : 
#         print(i)
#         result.append(norm_text(key) + '<<<f>>>' + " ".join([str(t) for t in word2vec_model.wv[key]]))
#     f.write("\n".join(result))

def readWord2Vec():
	word2vec_model = KeyedVectors.load_word2vec_format("baomoi.model.bin", binary=True)
	vocab = word2vec_model.wv.vocab
	keys = list(vocab.keys())
	return keys
