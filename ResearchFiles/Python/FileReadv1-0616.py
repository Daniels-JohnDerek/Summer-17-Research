#! /usr/bin/python

# Verson 1 - reads in file simple.txt, line by line removes punctuation, splits line, and counts words
# Then for each word in line, checks if exists in dictionary, if exists increment counts, else creats entry
# Sort dictionary then prints


fileRead = open("simple.txt", mode="r")

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
j = 0

for j in range (len(sortd)):
    sortedPrint = sortd[j]
    print ("%s %s" % (sortedPrint, d[sortedPrint]))

fileRead.close()
    
