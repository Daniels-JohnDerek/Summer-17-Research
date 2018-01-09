#! /usr/bin/python

# Earlier expermental version

import string

fileRead = open("MobyDick.txt", mode="r")

d = {}
a = {}

for line in fileRead.readlines():

    line = line.replace("\n", "")
    line = line.lower()
    table = str.maketrans({key: None for key in string.punctuation})
    line = line.translate(table)
    line = line.split(" ")
    x = 0

    lineCount = len(line)

    for x in range(lineCount):
        key = line[x]
    
        if key in d: 
            stringCount = d[key]
            d[key] = stringCount + 1

        else:
            d[key] = 1

sortd = sorted(d)
j = 0
k = 1


for j in range (len(sortd)):
    sortedPrint = sortd[j]


for k in range (len(sortd)):
    word = sortd[k]
    wordCount = d[word]
    if wordCount not in a.keys():
        a[wordCount] = []
    newWordList = [word]
    oldWords = a[wordCount]
    wordList = oldWords + newWordList
    a[wordCount] = wordList

sorta = sorted(a.items())
l = 0

for l in range(len(sorta) - 1,-1,-1):
    printList = sorta[l]
    if printList[0] >= 100:
        print(printList)
    
fileRead.close()
    
