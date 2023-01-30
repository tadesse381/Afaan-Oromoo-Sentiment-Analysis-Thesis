import l3
c='baraat'
cd=c[-1]
if (cd=='t')|(cd=='k')|(cd=='l'):
    print('Yes')
else:
    print('No')
print(cd)
tsuffixs=['oolee','oolii','oota','oota']
a='oota'
if a in tsuffixs:
    print(0,a)
#print(0,tsuffixs[1])
a='na'
lsffx=len(a)
print(lsffx)
suffix = a[1:lsffx]
print(suffix)

'''inputd="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/examplepos.txt"
output="C:/Users/user/AppData/Local/Programs/Python/Python37-32/MSSAAP 06.27.19/pos.txt"
l3.anal_file("om", inputd,output,root=True,gram=True, citation=True, raw=False)'''
