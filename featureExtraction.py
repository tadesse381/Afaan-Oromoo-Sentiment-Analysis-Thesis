import nltk
import l3
import preprocessing  as pre
intens = open("intensifiers.txt")
intensfr = intens.read()# Use this to read file content as a stream:
intensifiers = intensfr.split()
print(intensifiers)
sent = 'gaarii baayyee gaarumma baayyee haalan gaar fokkisaa hattuu fokkisoo'
tokens = nltk.word_tokenize(sent)
preprocessed_text = pre.main()
for st in preprocessed_text:
    print(st)
length = len(preprocessed_text)
print(length)
print(preprocessed_text[95])
print(preprocessed_text)
intfrs=[word for word in tokens if word in intensifiers]
print(intfrs)
    

import l3
inputd="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/examplepos.txt"
output="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/pos.txt"
l3.anal_file("om", inputd,output, root=False,gram=False, citation=True, raw=False, nbest=1)
