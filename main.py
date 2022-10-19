import os
from PIL import Image, ImageDraw, ImageFont

from dataTreatment import jsonNextLine, entryNextEntity, writeToFile, getNextLine
from textPreparation import nextText


def getAllowedChars():
    with open('allowedCharsList .txt') as topo_file:
        for text in topo_file:
            chars = text
    chars = text.split(' ')
    return chars


def isValidWord(allowedChars, word):
    if len(word) == 0:
        return False
    accepted = True
    for letter in word:
        if letter in allowedChars:
            pass
        else:
            accepted = False
    if not accepted:
        pass
    return accepted


def getToPop(allowedChars, word):
    toPop = []
    for i in range(len(word)):
        letter = word[i]
        if letter in allowedChars:

            pass
        else:
            toPop.append(i)

    return toPop


def validateWord(allowedChars, word):
    toPop = getToPop(allowedChars, word)
    if len(toPop) == 0:
        return word
    word = list(word)
    word.pop(toPop[0])
    if len(toPop) == 1:
        return ''.join(word)
    else:
        return validateWord(allowedChars, ''.join(word))


def writeWordsToFile():
    valid = 0
    invalid = 0
    allowedChars = getAllowedChars()
    articleTitleGenerator = jsonNextLine()
    f = open('wordsToDraw.txt', 'w')
    while True:
        try:
            title = next(articleTitleGenerator)
            wordGenerator = entryNextEntity(title)
            while True:
                try:
                    rawWord = next(wordGenerator)
                    validatedWord = validateWord(allowedChars, rawWord)
                    if isValidWord(allowedChars, validatedWord):
                        f.write(validatedWord + '\n')
                        valid = valid + 1
                    else:
                        invalid = invalid + 1
                except StopIteration:
                    break
        except StopIteration:
            break
    print('valid' + str(valid))
    print('invalid' + str(invalid))


def main():
    writeWordsToFile()


def test():
    allowedChars = getAllowedChars()
    # letter = 'ر'

    # print(letter in allowedChars)

    print(validateWord(allowedChars, 'لـ”عين'))


if __name__ == '__main__':
    main()
