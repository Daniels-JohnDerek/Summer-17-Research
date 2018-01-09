#! /usr/bin/python

# Version 9

import string
import sys
import os.path
import os

#Change to raw_input for use in sunlab/terminal
docSearch = raw_input("Please input a file or directory name: ")

docList = []
ext = docSearch[-4:]
ext = ext.lower()
pathFormat = ""
txtDocs = []



if ext == '.txt':
    fileCheck = os.path.isfile(docSearch)
    
    if not fileCheck:
        print("Sorry, %s does not exist" % (docSearch))
        sys.exit()

    docList.append(docSearch)
    print ("processing " + docSearch)
    pathFormat = docSearch

elif ext == '.pdf':
    fileCheck = os.path.isfile(docSearch)

    if not fileCheck:
        print("Sorry, %s does not exist" % (docSearch))
        sys.exit()

    txtFile = "1.txt"
    txtDocs.append(txtFile)
    pdfSearch = "pdftotext -q " + docSearch + " " + txtFile
    os.system(pdfSearch)
    docSearch2 = docSearch[:-4] + ".txt"
    print("processing " + txtFile + "(derived from " +  docSearch2 +  ")")
    pathFormat = txtFile
    docList.append(txtFile)
    
    
else:
    folderCheck = os.path.exists(docSearch)
    fileCheck = os.path.isfile(docSearch)

    if (not fileCheck) and (not folderCheck):
        print("Sorry, %s does not exist" % (docSearch))
        sys.exit()

    textCounter = 0
    pdfCounter = 0
    #Get the file names
    for root, dirnames, filenames in os.walk(docSearch):
        for name in filenames:
            #Remember to change this back to .txt
            fileExt = name[-4:]
            fileExt = fileExt.lower()
            if fileExt == '.txt':
                textCounter += 1
                pathFormat = ("%s/%s" % (root,name))
                docList.append(pathFormat)
                print ("processing " + pathFormat)

            elif fileExt == '.pdf':
                pdfCounter += 1
                txtFile = str(pdfCounter) + ".txt"
                txtDocs.append(txtFile)
                pathFormat = ("%s/%s" % (root,name))
                pdfSearch = "pdftotext -q " + pathFormat  + " " + txtFile
                os.system(pdfSearch)
                docSearch2 = pathFormat[:-4] + ".txt"
                print("processing " + docSearch2  + "(derived from " + pathFormat  + ")")
                docList.append(txtFile)
                

docCounter = 0 
uniqWords = 0
totLineCounter = 0
totWordCounter = 0
a = {}
d = {}
stopWords = []

stopRead = open("../Data/stopwords", mode='r')

for line in stopRead.readlines():
    line = line.replace("\n", "")
    stopWords.append(line)

stopRead.close()

for file in docList:


    pathFormat = docList[docCounter]
    fileRead = open(pathFormat, mode="r")
    docCounter += 1

    for line in fileRead.readlines():
        
        totLineCounter += 1
        line = line.replace("\n", "")
        line = line.lower()
        line = line.replace("!", "").replace("#", "").replace("\"", "").replace("$", "").replace("%", "").replace("&", "").replace("'", "").replace("(", "").replace(")", "").replace("*", "").replace("+", "").replace(",", "").replace(".", "").replace("/", "").replace(":", "").replace(";", "").replace("<", "").replace("=", "").replace(">", "").replace("?", "").replace("`", "").replace("{", "").replace("|", "").replace("}", "").replace("~", "").replace("\r", "")
        #Cleaner way to do this? ^^^
        line = line.split(" ")
        x = 0

        lineCount = len(line)
        totWordCounter += lineCount

        for x in range(lineCount):
            key = line[x]
        
            if key in d: 
                stringCount = d[key]
                d[key] = stringCount + 1

            else:
                if key not in stopWords:
                   d[key] = 1
                   uniqWords += 1


    sortd = sorted(d)
    # ^^^ sortd is a list but d is a dictionary

    fileRead.close()

    """V1 Printstatment
    j = 0
    for j in range (len(sortd)):
        sortedPrint = sortd[j]
        print ("%s %s" % (sortedPrint, d[sortedPrint]))
    """



k = 0
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

    
"""
    l = 0
    for l in range(len(sorta) - 1,-1,-1): 
        printList = sorta[l]
        if printList[0] >= 100:
            print(printList)
"""

    

print ("I processed %d total text files and %d total PDF files.\nI processed  %d total text lines, and %d total words, of which there were %d different non-stop words." % (textCounter,pdfCounter,totLineCounter,totWordCounter,uniqWords))

print ("The 100 most common non-stop  words I found were: ")

printOrder = 1
for l in range(len(sorta) - 1, len(sorta) - 101, -1):
    printList = sorta[l]
    print("%d. %s" % (printOrder,printList))
    printOrder += 1
     

for file in txtDocs:
    os.system("rm " +  file)

