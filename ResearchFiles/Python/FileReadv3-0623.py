#! /usr/bin/python

# Version 3
# Fix the problem of having to hardwire the text filename, prompt the user to give filename and error checking


import sys
import os.path

docSearch = input("Please input a file name: ")

searchLen = len(docSearch)
ext = docSearch[-4:]

if ext != '.txt':
    print("Sorry, %s is not a legal file name." % (docSearch))
    sys.exit()

fileCheck = os.path.isfile(docSearch)


if not fileCheck:
    print("Sorry, %s does not exist" % (docSearch))
    sys.exit()

print ("This file exits...")

fileRead = open(docSearch, mode="r")

d = {}
a = {}

for line in fileRead.readlines():

    line = line.replace("\n", "")
    line = line.lower()
    line = line.replace("!", "").replace("#", "").replace("\"", "").replace("$", "").replace("%", "").replace("&", "").replace("'", "").replace("(", "").replace(")", "").replace("*", "").replace("+", "").replace(",", "").replace(".", "").replace("/", "").replace(":", "").replace(";", "").replace("<", "").replace("=", "").replace(">", "").replace("?", "").replace("`", "").replace("{", "").replace("|", "").replace("}", "").replace("~", "")
    #Cleaner way to do this? ^^^
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
l = 0


for l in range(len(sorta) - 1,-1,-1):
    printList = sorta[l]
    if printList[0] >= 100:
        print(printList)


fileRead.close()
    
