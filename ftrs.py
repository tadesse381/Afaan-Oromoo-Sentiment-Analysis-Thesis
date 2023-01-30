import nltk
import re
import preprocessing  as pre
import l3 as pos
import string
import ast
import json
def posTagging():
    adj_lists = open("adjective_lists.txt")
    adjectives = adj_lists.read()# Use this to read file content as a stream:
    adjective_lists = adjectives.split()
    sentiment_list = open("adjvrt_lists.txt")
    sentiments = sentiment_list.read()# Use this to read file content as a stream:
    sentlists = sentiments.split()
    noun_suffixs = open("noun_suffixs.txt")
    nsuffixs = noun_suffixs.read()# Use this to read file content as a stream:
    nnsuffixs = nsuffixs.split()
    verb_suffixs = open("verb_suffixs.txt")
    vsuffixs = verb_suffixs.read()# Use this to read file content as a stream:
    vvsuffixs = vsuffixs.split()
    intens = open("intensifiers.txt")
    intensfr = intens.read()# Use this to read file content as a stream:
    intensifiers = intensfr.split()
    #Please made them lower case
    preprocessed_text = pre.main()
    st=list()
 #---------------------------Prefix Remover(Reduplication Remover)-----------------------------------
    for x in range(len(preprocessed_text)):
        lsprfx=list()
        for char in preprocessed_text[x].split():
            if(len(char)>4):
                if(char[3]==char[2]==char[0] and char[4]==char[1]):
                    lsprfx.append(char[3:len(char)])
                elif(char[0]==char[2]) and ((char[1]=="'")|(char[1]=='`')):
                    lsprfx.append(char[2:len(char)])
                elif (char[0]==char[3]) and (char[1]==char[4]) and (char[2]==char[5]):
                    lsprfx.append(char[3:len(char)])
                else:
                    lsprfx.append(char)
            else:
                lsprfx.append(char)
        #print(lsprfx)
        st.append(lsprfx)
 #---------------------------Prefix Remover(Reduplication Remover)-----------------------------------
    print(st)
    lword=list()
    lrootword=list()
    def rtfinder(wrd):
        flag = False
        r = str()
        for root in sentlists:
            if(wrd.startswith(root))==True:
                flag = True
                r = root
                break
        return flag, r
    for sent in st:
        lswd=list()
        lsrt=list()
        lswdo=list()
        lsrto=list()
        for wrd in sent:
            if wrd in intensifiers:
                lswd.append('('+"'"+wrd +"'"+","+"'"+'ADV'+"'"+')')
                lsrt.append('('+"'"+wrd +"'"+","+"'"+'ADV'+"'"+')')
            elif wrd=='hin':
                lswd.append('('+"'"+wrd +"'"+","+"'"+'NG'+"'"+')')
                lsrt.append('('+"'"+wrd +"'"+","+"'"+'NG'+"'"+')')            
            elif wrd in adjective_lists:
                for adjrt in sentlists:
                    if(wrd.startswith(adjrt))==True:
                        lswd.append('('+"'"+wrd+"'"+","+"'"+'ADJ'+"'"+')')
                        lsrt.append('('+"'"+adjrt+"'"+","+"'"+'ADJ'+"'"+')')
                        break
            else:
                flag,root = rtfinder(wrd)
                if (flag is True):
                        wln = len(wrd)
                        rln = len(root)
                        suffix = wrd[rln:wln]
                        spcasennsuffixs=['toota','toolee','toolii','lan','ran','man','li','ri','mi','keen','geen','deen','reen','been','neen','reen','been','neen','ka','ga','da','ra','ba','na']
                        if suffix in nnsuffixs:
                                lswd.append('('+"'"+wrd +"'"+","+"'"+'NN'+"'"+')')
                                lsrt.append('('+"'"+root +"'"+","+"'"+'NN'+"'"+')')
                        elif suffix in spcasennsuffixs:
                            lswd.append('('+"'"+wrd +"'"+","+"'"+'NN'+"'"+')')
                            lsrt.append('('+"'"+root +"'"+","+"'"+'NN'+"'"+')')
                        elif suffix in vvsuffixs:
                            lswd.append('('+"'"+wrd +"'"+","+"'"+'VV'+"'"+')')
                            lsrt.append('('+"'"+root +"'"+","+"'"+'VV'+"'"+')')
                        else:
                            lswd.append('('+"'"+wrd+"'"+","+"'"+'DF'+"'"+')')
                            lsrt.append('('+"'"+wrd+"'"+","+"'"+'DF'+"'"+')')
                            break
                else:
                    for rt in  sentlists:
                        endcharrt=rt[-1]
                        if endcharrt=='t':
                            tsuffixs=['nna','nnu','dha','dhe','dhu','chisiise','chisiisa','chisisa','chisiisan','chisiste','chisisna','chisistan','chiise','chiisan','chiisna','chiistan','chiisne']
                            tvowelsuffix=['iinsa','iisa','noo']
                            tword=list()
                            horsiisat=list()
                            tword.append(rt)
                            for twrd in tword:
                                ntwrd=rt[0:(len(twrd)-1)]
                                for sfx in tsuffixs:
                                    horsiisat.append(ntwrd+sfx)
                                for vsfx in tvowelsuffix:
                                    horsiisat.append(twrd+vsfx)
                                if wrd in horsiisat:
                                    lswd.append('('+"'"+wrd+"'"+","+"'"+'VV'+"'"+')')
                                    lsrt.append('('+"'"+rt+"'"+","+"'"+'VV'+"'"+')')
                                    break
                                else:
                                    lswd.append('('+"'"+wrd+"'"+","+"'"+'DF'+"'"+')')
                                    lsrt.append('('+"'"+wrd+"'"+","+"'"+'DF'+"'"+')')
                                    break
            break
        lword.append((lswd))
        lrootword.append((lsrt))
    return lword,lrootword,st
def hornMorpho(sentence_list):
    hrnlist=list()
    for sentence in sentence_list:
        findelete = open('posin.txt', 'r+')
        findelete.truncate(0)
        foutdelete = open('posout.txt', 'r+')
        foutdelete.truncate(0)
        #c=['bareedaa','gammannee','gadhee','bagadha']
        sentence_string=" ".join(sentence)
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
        hrnlist.append(dict_from_file[1])
    return hrnlist
def tagIdentifier(hrno,wtkzd_rb,rtkzd_rb):
    tagout=list()
    for k in range(len(wtkzd_rb)):
        a=hrno[k]
        b=wtkzd_rb[k]
        c=rtkzd_rb[k]
        z=0
        finaltag=list()
        for z in range(len(a)):
            aa=a[z]
            bb=ast.literal_eval(b[z])
            cc=ast.literal_eval(c[z])
            #print(aa)
            #print(bb)
            #print(cc)
            if(bb[1]=='ADV'):
                 finaltag.append(cc[0]+'/'+bb[1])
            elif(bb[1]=='ADJ'):
                 finaltag.append(cc[0]+'/'+bb[1])
            elif(bb[1]=='NG'):
                 finaltag.append(cc[0]+'/'+bb[1])
            elif(aa[1].rstrip()==bb[1]):
                 finaltag.append(cc[0]+'/'+bb[1])
            else:
                if(aa[1]!=bb[1] and bb[1]!='DF'):
                    finaltag.append(cc[0]+'/'+bb[1])
            z=z+1
        tagout.append(finaltag)
        k=k+1
    for v in range(len(tagout)):
        print(tagout[v])
'''        for taglist in wtkzd_rb[0]:
            taggedword=ast.literal_eval(taglist)
            print(taggedword[0],taggedword[1],"------------")
            print("----------------------")
        for hrn in hrno[k]:
            print(hrn,'NEWLINE')'''
def main():
   tokenizeed_word, tokenized_root,st = posTagging()
   horntagged=hornMorpho(st)
   tagIdentifier(horntagged,tokenizeed_word,tokenized_root)
   #print(horntagged)
   print(tokenizeed_word)
   print(tokenized_root)
main()
