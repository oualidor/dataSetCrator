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


def validateWord(allowedChars, word):

    accepted = True
    word = word[0:len(word)-1]
    print(word)
    for letter in word:
        if letter in allowedChars:
            pass
        else:
            accepted = False
    return accepted


def main():
    allowedChars = getAllowedChars()
    width = 400;
    height = 200
    back_ground_color = (255, 255, 255)
    textColor = (0, 0, 0)
    fontsDirectory = "fonts"
    outPutDirectory = "createResult"
    fonts = os.listdir(fontsDirectory)
    textToCreate = 100
    j = 0
    for fontName in fonts:

        print(fontName)
        font = ImageFont.truetype(fontsDirectory + "/" + fontName, size=60)
        fontBaseName = fontName[0:len(fontName) - 4]
        try:
            os.mkdir(outPutDirectory + "/" + fontBaseName)
        except:
            print('hihi')
            pass
        with open('wordsList.txt') as topo_file:
            for text in topo_file:
                if validateWord(allowedChars, text):
                    im = Image.new("RGB", (width, height), back_ground_color)
                    canvas = ImageDraw.Draw(im)
                    canvas.text((20, 20), text, fill=textColor, font=font, direction="rtl")
                    im.save(outPutDirectory + "/" + fontBaseName + "/" + str(j) + ".png")
                    lineToWrite = outPutDirectory + "/" + fontBaseName + "/" + str(j) + ".png," + text
                    writeToFile('words.txt', lineToWrite)
                    j = j + 1
                else:
                    print('ignoring: ' + text)


def test():
    t = ['a', 'b']
    if 'c' in t:
        print('in')


main()
