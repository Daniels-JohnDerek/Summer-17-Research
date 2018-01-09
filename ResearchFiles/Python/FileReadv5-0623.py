#! /usr/bin/python

# Version 5 - Checking file and directory
# Allow the user to type either the name of a single file, or the name of a directory
# Updated printing format

import string
import sys
import os.path
import os

#Change to raw-input for use in sunlab/terminal
docSearch = raw_input("Please input a file or directory name: ")

docList = []
ext = docSearch[-4:]
pathFormat = ""

if ext == '.txt':
    fileCheck = os.path.isfile(docSearch)
    
    if not fileCheck:
        print("Sorry, %s does not exist" % (docSearch))
        sys.exit()

    docList.append(docSearch)
    print ("processing " + docSearch)
    pathFormat = docSearch

# Search that directory and all of its subdirectories for any file that ends in ".txt" 
# Process each of these files in turn, accumulating all of the statistics together    
else:
    folderCheck = os.path.exists(docSearch)
    fileCheck = os.path.isfile(docSearch)

    if (not fileCheck) and (not folderCheck):
        print("Sorry, %s does not exist" % (docSearch))
        sys.exit()


    #Get the file names
    for root, dirnames, filenames in os.walk(docSearch):
        for name in filenames:
            #Remember to change this back to .txt
            fileExt = name[-4:]
            if fileExt == '.txt':
                pathFormat = ("%s/%s" % (root,name))
                docList.append(pathFormat)
                print ("processing " + pathFormat)

docCounter = 0 
totLineCounter = 0
totWordCounter = 0
a = {}


for file in docList:

    pathFormat = docList[docCounter]
    print(pathFormat)
    fileRead = open(pathFormat, mode="r")
    d = {}
    docCounter += 1

    for line in fileRead.readlines():
        
        totLineCounter += 1
        line = line.replace("\n", "")
        line = line.lower()
        line = line.replace("!", "").replace("#", "").replace("'\'", "").replace("$", "").replace("%", "").replace("&", "").replace("'", "").replace("(", "").replace(")", "").replace("*", "").replace("+", "").replace(",", "").replace(".", "").replace("/", "").replace(":", "").replace(";", "").replace("<", "").replace("=", "").replace(">", "").replace("?", "").replace("`", "").replace("{", "").replace("|", "").replace("}", "").replace("~", "")
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
                d[key] = 1


    sortd = sorted(d)
    # ^^^ sortd is a list but d is a dictionary

    """V1 Printstatment
    j = 0
    for j in range (len(sortd)):
        sortedPrint = sortd[j]
        print ("%s %s" % (sortedPrint, d[sortedPrint]))
    """


    k = 1
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

    """v2 -v4 Printstatment
    l = 0
    for l in range(len(sorta) - 1,-1,-1):
        printList = sorta[l]
        if printList[0] >= 100:
            print(printList)
    """


    fileRead.close()


print ("I processed %d total files, %d total text lines, and %d total words, of which there were %d different words." % (len(docList),totLineCounter,totWordCounter,len(sorta)))

print ("The 100 most common words I found were: ")

printOrder = 1
for l in range(len(sorta) - 1, len(sorta) - 101, -1):
    printList = sorta[l]
    print("%d. %s" % (printOrder,printList))
    printOrder += 1

        
