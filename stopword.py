import nltk
import io
file11 = open("stopwords.txt") 
stopwords = file11.read()# Use this to read file content as a stream:
stp=stopwords.split() 
file1 = open("test.txt") 
line = file1.read()# Use this to read file content as a stream: 
words = line.split() 
for r in words: 
    if not r in stp: 
        appendFile = open('ab.txt','a') 
        appendFile.write(" "+r) 
        appendFile.close() 
