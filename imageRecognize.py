from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image


def whatNumIsThis(filePath):
    matchedArr=[]
    loadExamps=open('numArraEx.txt','r').read()
    loadExamps=loadExamps.split('\n')

    i=Image.open(filePath)
    iar=np.array(i)
    iar1=iar.tolist()
    inQuestion=str(iar1)
    for eachExample in loadExamps:
        if len(eachExample)>3:
            splitEx=eachExample.split('::')
            currentNum=splitEx[0]
            currentArray=splitEx[1]

            eachPixEx=currentArray.split('],')
            eachPixInQ=inQuestion.split('],')
            x=0
            while x<len(eachPixEx):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedArr.append(int(currentNum))
                x+=1
    print(matchedArr)
    x=Counter(matchedArr)
    print(x)
    showRecordinGraph(x,iar)

def showRecordinGraph(sortedArray,numpyArrayOfImage):
    graphx = []
    graphy = []
    for eachThing in sortedArray:
        graphx.append(eachThing)
        graphy.append(sortedArray[eachThing])
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)
    ax1.imshow(numpyArrayOfImage)
    ax2.bar(graphx, graphy, align="center")
   # plt.ylim(450)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()

whatNumIsThis('images/numbers/3.1.png')


