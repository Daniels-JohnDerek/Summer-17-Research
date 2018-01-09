#! /usr/bin/python

# Version 2 - Revised printstatement 
# Updated format and only printing words that occur more than 100 times

fileRead = open("MobyDick.txt", mode="r")

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

#V1 Printstatment
#j = 0
#for j in range (len(sortd)):
#    sortedPrint = sortd[j]
#    print ("%s %s" % (sortedPrint, d[sortedPrint]))



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
    
