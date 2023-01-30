sentiment_list = open("adjvrt_lists.txt")
sentiments = sentiment_list.read()# Use this to read file content as a stream:
sentlists = sentiments.split()
rtendwitht=list()
totalrtendwitht=list()
tsuffixs=['nna','nnu','dha','dhe','dhu','chisiise','chisiisa','chisisa','chisiisan','chisiste','chisisna','chisistan','chiise','chiisan','chiisna','chiistan','chiisne']
tvowelsuffix=['iinsa','iisa','noo']
for rt in  sentlists:
    endcharrt=rt[-1]
    if endcharrt=='t':
        rtendwitht.append(rt)
for rttwrd in rtendwitht:
    print(rttwrd)
    horsiisat=list()
    ntrtwrd=rttwrd[0:(len(rttwrd)-1)]
    horsiisat.append(rttwrd)
    for sfx in tsuffixs:
        horsiisat.append(ntrtwrd+sfx)
    for vsfx in tvowelsuffix:
        horsiisat.append(ntrtwrd+vsfx)
    totalrtendwitht.append(horsiisat)
print(totalrtendwitht)
