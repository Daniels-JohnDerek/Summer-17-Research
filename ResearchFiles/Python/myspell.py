#! /usr/bin/python

# Spell Check
# Program will check percentage of words that are found in a dictionary to test how well pdftotext worked
# Takes the name of a text file to spell check as one input, and the name of an output file as another input
# Return number of words tested and percentage spelled correctly

import string
import sys
import os.path
import os

inputFile = sys.argv[1]
outputFile = sys.argv[2]

fileCheck = os.path.isfile(inputFile)

if not fileCheck:
    print("Sorry, %s does not exist" % (inputFile))
    sys.exit()

dictList = []
dictionaryFile = open("/usr/share/dict/words", mode = 'r')

for line in dictionaryFile.readlines():
    line = line.lower()
    line = line.replace("\n", "")
    dictList.append(line)

dictionaryFile.close()
inputList = []
wordCounter = 0

fileRead = open(inputFile, mode = "r")

for line in fileRead.readlines():
    line = line.replace("\n", "")
    line = line.lower()
    line = line.replace("!", "").replace("#", "").replace("\"", "").replace("$", "").replace("%", "").replace("&", "").replace("'","").replace("(", "").replace(")", "").replace("*", "").replace("+", "").replace(",", "").replace(".", "").replace("/", "").replace(":", "").replace(";", "").replace("<", "").replace("=", "").replace(">", "").replace("?", "").replace("`", "").replace("{", "").replace("|", "").replace("}", "").replace("~", "").replace("\r", "")
    line = line.split(" ")
    lineCount = len(line)
    
    for x in range(lineCount):
        inputList.append(line[x])
        wordCounter += 1

fileRead.close()
correctSpelled = 0

for word in inputList:
    if word in dictList:
        correctSpelled += 1

spellAccurary = (wordCounter/correctSpelled)

finalOutput = "%d\n%f\n" % (wordCounter, spellAccurary)

os.system("touch " + outputFile)
fileWrite = open(outputFile, mode = "w")

fileWrite.write(str(finalOutput))
