sentiment_list = open("adjvrt_lists.txt")
sentiments = sentiment_list.read()# Use this to read file content as a stream:
sentlists = sentiments.split()
wrddd='boo`aniiru'
for rt in  sentlists:
    endcharrt=rt[-1]
    endcharrtdouble=rt[-2]+rt[-1]
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
        for hrs in horsiisat:
            if wrddd==hrs:
                print(wrddd,'VV',rt,'VV')
    dhhhudha_suffixs=['atini','achise','achisa','achisan','achiste','achisna','achistan','aniiru','anna','anne','annu','ata','atani','ate','atine','atte','attu','attan','atu']
    if endcharrtdouble=='dh':
        dha=list()
        horsiisdha=list()
        dha.append(rt)
        for dhasuffix in dhhhudha_suffixs:
            horsiisdha.append(rt+dhasuffix)
        print(horsiisdha)
    if endcharrt=='h':
        h=list()
        horsiish=list()
        h.append(rt)
        print('new',h)
        for hsuffix in dhhhudha_suffixs:
            horsiish.append(rt+hsuffix)
        print(horsiish)
    if endcharrt=='`':
        hudha=list()
        horsiishudha=list()
        hudha.append(rt)
        print(hudha,000)
        for hudhasuffix in dhhhudha_suffixs:
            horsiishudha.append(rt+hudhasuffix)
        #print(horsiishudha)
        for hrshudha in horsiishudha:
            if wrddd==hrshudha:
                print(wrddd,'VV',rt,'VV')
