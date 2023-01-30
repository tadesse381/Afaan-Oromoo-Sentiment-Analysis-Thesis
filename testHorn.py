import l3 as pos
import re
import nltk
import json
findelete = open('posin.txt', 'r+')
findelete.truncate(0)
foutdelete = open('posout.txt', 'r+')
foutdelete.truncate(0)
c=['bareedaa','gammannee','gadhee','bagadha']
sentence_string=" ".join(c)
inputd="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/posin.txt"
output="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/posout.txt"
appendFile = open('posin.txt','a')
appendFile.write(sentence_string)
appendFile.close()
pos.anal_file("om", inputd,output,root=False,gram=False, citation=True, raw=False, nbest=1)
posoutsent = open("posout.txt")
tagged_sent = posoutsent.read()# Use this to read file content as a stream:
with open('posout.txt','r') as inf:
    dict_from_file = eval(inf.read())
print(dict_from_file[1][0])
'''my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
import itertools      
d ={'1':['a','b','c']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
'''
