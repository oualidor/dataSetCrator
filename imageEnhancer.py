import cv2
import numpy as np
import os
from PIL import Image


def blankLinesDetector(im):
    toDelete = []
    textStart = 0
    textEnd = 0
    for h in range(len(im)):
        currentLine = im[h]
        delete = True
        for w in range(len(currentLine)):
            currentPixel = currentLine[w]
            if currentPixel != 255:
                delete = False
                break
        if delete:
            toDelete.append(h)
    return toDelete


def blankColumnsDetector(im):
    toDelete = []
    for w in range(len(im[0])):
        delete = True
        for h in range(len(im)):
            currentPixel = im[h][w]
            if currentPixel != 255:
                delete = False
                break

        if delete:
            toDelete.append(w)
        else:
            break
    for w in range(len(im[0]) -1, -1, -1):
        delete = True
        for h in range(len(im)):
            currentPixel = im[h][w]
            if currentPixel != 255:
                delete = False
                break

        if delete:
            toDelete.append(w)
        else:
            break
    return toDelete



def getImageOnly(img, columns, lines):
    newImg = np.delete(img, lines, 0)
    newImg = np.delete(newImg, columns, 1)
    return newImg


def main():
    inputDir = 'createResult'
    outPutDirectory = 'enhancerResult'
    for r, d, f in os.walk(inputDir):
        for file in f:
            if '.png' in file:
                imagePath = os.path.join(r, file)
                im = cv2.imread(imagePath)
                im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                linesToDelete = blankLinesDetector(im)
                columnsToDelete = blankColumnsDetector(im)
                image = getImageOnly(im, columnsToDelete, linesToDelete)
                image = Image.fromarray(image)
                # OutPut
                outPutPath = outPutDirectory + '/' + r.split('/')[1]
                try:
                    os.mkdir(outPutPath)
                except:
                    pass

                image.save(outPutPath + '/' + file)


if __name__ == '__main__':
    main()
