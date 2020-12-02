def readDocFromFile(file):
    with open(file , 'r') as f:
        data = f.read()
    return data  

def writeDocToFile(data, file):
    with open(file , 'w') as f:
        f.write(data)
    