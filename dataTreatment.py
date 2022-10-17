import json


def jsonNextLine():
    f = open('data.json')
    data = json.load(f)
    for article in data:
        yield article['title']
    f.close()

def getNextLine(filePath):
    f = open(filePath, "r")
    yield f.readline()

def entryNextEntity(line):
    for word in line.split(' '):
        yield word


def writeToFile(filePath, entry):
    f = open(filePath, "a")
    f.write(entry)
    f.close()
