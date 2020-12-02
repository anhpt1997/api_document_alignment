import numpy as np

def read_w2vec(file_w2vec):
    with open(file_w2vec , "r") as f:
        word2vecs = f.readlines()
        word2vecs = [w.replace("\n","") for w in word2vecs]
    vocab = {}
    for line in word2vecs:
        vocab[line.split('<<<f>>>')[0]] = np.array([float(t) for t in line.split("<<<f>>>")[1].split()])
    return vocab

# import pickle
# pickle.dump(read_w2vec('w2vec.txt'),open('dic_w2vec','wb'))