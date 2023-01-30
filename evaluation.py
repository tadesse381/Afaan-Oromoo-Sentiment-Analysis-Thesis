import tkinter
from tkinter import*
from tkinter import scrolledtext
import matplotlib.pyplot as plt
import numpy as np
import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier, MaxentClassifier, SklearnClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.metrics.scores import (precision, recall)
from nltk.metrics.scores import (accuracy, precision, recall, f_measure,
                                          log_likelihood, approxrand)
from nltk.tokenize import word_tokenize
import nltk.classify
from sklearn.svm import LinearSVC
from nltk.metrics import precision, recall, f_measure
def classifierAlgorithm(textinput,clalgo):
    with open("D:\Senti-Corpus\sentiment_data\spos.txt", 'r') as filehandle:
        strong_positive = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_sps = [((spsnt), '+2') for spsnt in strong_positive]
        total_sent = [((spsnt), '+2') for spsnt in strong_positive]
        filehandle.close()
    with open("D:\Senti-Corpus\sentiment_data\pos.txt", 'r') as filehandle:
        positive = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_ps = [((spsnt), '+1') for spsnt in positive]
        for i in range(len(dc_ps)):
            total_sent.append(dc_ps[i])
        filehandle.close()
    with open("D:\Senti-Corpus\sentiment_data\sneg.txt", 'r') as filehandle:
        strong_negative = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_sng = [((spsnt), '-2') for spsnt in strong_negative]
        for k in range(len(dc_sng)):
            total_sent.append(dc_sng[k])
        filehandle.close()
    #Code to open negative sentences
    with open("D:\Senti-Corpus\sentiment_data\\neg.txt", 'r') as filehandle:
        negative = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_ng = [((spsnt), '-1') for spsnt in negative]
        for z in range(len(dc_ng)):
            total_sent.append(dc_ng[z])
        filehandle.close()

    sposfeats = dc_sps
    posfeats = dc_ps
    snegfeats = dc_sng
    negfeats = dc_ng
    snegcutoff = int(len(snegfeats)*3.2/4)
    negcutoff = int(len(negfeats)*3.2/4)
    sposcutoff = int(len(sposfeats)*3.2/4)
    poscutoff = int(len(posfeats)*3.2/4)
    trainfeats = snegfeats[:snegcutoff] + negfeats[:negcutoff] + sposfeats[:sposcutoff] + posfeats[:poscutoff]
    testfeats = snegfeats[snegcutoff:] + negfeats[negcutoff:] + sposfeats[sposcutoff:] + posfeats[poscutoff:]
    print(len(trainfeats))
    #print(trainfeats)
    print(len(testfeats ))
    #print(testfeats)
    # Step 2
    dictionary = set(word.lower() for passage in trainfeats for word
    in word_tokenize(passage[0]))
    # Step 3
    t = [({word: (word in word_tokenize(x[0])) for word in
    dictionary}, x[1]) for x in trainfeats]
    # Step 4 – the classifier is trained with sample data
    if clalgo==2:
         classifier = nltk.NaiveBayesClassifier.train(t)
         #classifierm = nltk.MaxentClassifier.train(t)
    elif clalgo==3:
         classifier = nltk.classify.SklearnClassifier(LinearSVC())
         classifier.train(t)
    elif clalgo==4:
         classifier = MaxentClassifier.train(t,algorithm='gis',trace=0,max_iter=10,min_lldelta=0.5)
    # Step 2
    dic = set(word.lower() for passage in testfeats for word
    in word_tokenize(passage[0]))
    # Step 3
    tt = [({word: (word in word_tokenize(x[0])) for word in
    dic}, x[1]) for x in testfeats]
    test_data_features = {word.lower(): (word in word_tokenize(textinput.lower())) for word in dictionary}
    #-------------------------------------NB----------
    tdnb=[(textinput,(classifier.classify(test_data_features)))
    ]
    # Step 22
    dc = set(word.lower() for passage in tdnb for word
    in word_tokenize(passage[0]))
    # Step 33
    tddnb = [({word: (word in word_tokenize(x[0])) for word in
    dc}, x[1]) for x in tdnb]
    #----------------------------------------
    #--------------------------svm-----------------
    tdsvm=[(textinput,(classifier.classify(test_data_features)))
    ]

    # Step 22
    dcsvm = set(word.lower() for passage in tdsvm for word
    in word_tokenize(passage[0]))
    # Step 33
    tddsvm = [({word: (word in word_tokenize(x[0])) for word in
    dcsvm}, x[1]) for x in tdsvm]
    #----------------------------------------------------
    #--------------------------Max-----------------
    tdmax=[(textinput,(classifier.classify(test_data_features)))
    ]

    # Step 22
    dcmax = set(word.lower() for passage in tdmax for word
    in word_tokenize(passage[0]))
    # Step 33
    tddmax = [({word: (word in word_tokenize(x[0])) for word in
    dcmax}, x[1]) for x in tdmax]
    #----------------------------------------------------
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    for i, (feats, label) in enumerate(tt):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)
    spos_precision = precision(refsets['+2'], testsets['+2'])
    spos_recall = recall(refsets['+2'], testsets['+2'])
    spos_fmeasure = f_measure(refsets['+2'], testsets['+2'])

    pos_precision = precision(refsets['+1'], testsets['+1'])
    pos_recall = recall(refsets['+1'], testsets['+1'])
    pos_fmeasure = f_measure(refsets['+1'], testsets['+1'])

    sneg_precision = precision(refsets['-2'], testsets['-2'])
    sneg_recall = recall(refsets['-2'], testsets['-2'])
    sneg_fmeasure =  f_measure(refsets['-2'], testsets['-2'])

    neg_precision = precision(refsets['-1'], testsets['-1'])
    neg_recall = recall(refsets['-1'], testsets['-1'])
    neg_fmeasure =  f_measure(refsets['-1'], testsets['-1'])
    print(0,spos_precision,spos_recall,spos_recall,spos_fmeasure,pos_precision,pos_recall,pos_fmeasure,sneg_precision,sneg_recall,sneg_fmeasure,neg_precision,neg_recall,neg_fmeasure)
    #print("NB:",textinput,'"',classifier.classify(test_data_features),'"')
    #print("SVM:",textinput,'"',classifier.classify(test_data_features),'"')
    #print("Max:",textinput,'"',classifier.classify(test_data_features),'"')
    #print("Maxet:",c,'"',classifierm.classify(test_data_features),'"')
    #classifier.show_most_informative_features()
    '''print("Accuracy SVM:",nltk.classify.accuracy(classifiersvm, tt))
    print("Accuracy Maxent:",nltk.classify.accuracy(classifier, tt))'''
    acc = nltk.classify.accuracy(classifier, tt)
    prcn = ((spos_precision + sneg_precision + neg_precision + pos_precision) / 4)
    rcll = ((spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure) / 4)
    fmsr = ((spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure) / 4)
    plt.style.use('ggplot')
    x = ['Accuracy', 'Precision', 'Recall', 'F-Measure']
    g = [acc,prcn,rcll,fmsr]
    x_pos = np.arange(len(x))
    plt.bar(x_pos, g, color='#7ed6df')
    plt.xlabel("Evaluation")
    plt.ylabel("g")
    plt.title("Multi Scale sentiment Analysis for Afaan Oromo Posts")
    plt.xticks(x_pos, x)
    plt.show()
    '''
    print ('---------------------------------------')
    print ('             Evaluation               ')
    print ('---------------------------------------')
    print("Accuracy:",nltk.classify.accuracy(classifier, tt))
    print ('precision', (spos_precision + sneg_precision + neg_precision + pos_precision) / 4)
    print ('recall', (spos_recall + sneg_recall + neg_recall + pos_recall) / 4)
    print ('f-measure', (spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure) / 4)'''
    #out = classifier.classify(test_data_features)
    return textinput, out

def main():
    window= tkinter.Tk()
    # to rename the title of the window
    window.title("MSSAAP")
    # pack is used to show the object in the window

    def function():
        pass

    # creating a root menu to insert all the sub menus
    root_menu = tkinter.Menu(window)
    window.config(menu = root_menu)

    # creating sub menus in the root menu
    file_menu = tkinter.Menu(root_menu) # it intializes a new su menu in the root menu
    root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
    file_menu.add_command(label = "New file.....", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
    file_menu.add_command(label = "Open files", command = function)
    file_menu.add_separator() # it adds a line after the 'Open files' option
    file_menu.add_command(label = "Exit", command = window.quit)

    # creting another sub menu
    edit_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label = "Edit", menu = edit_menu)
    edit_menu.add_command(label = "Undo", command = function)
    edit_menu.add_command(label = "Redo", command = function)
    black= Label(window, text = "Machine Learning Based", foreground="white", bg="black", height=2,justify=LEFT,font=('Verdana', 12, 'bold', 'italic'))
    black.pack(fill='x')
    red = Label(window,text = "Multi Scale Sentiment Analysis for",foreground="black", bg="red", height=2,font=('Verdana', 12, 'bold', 'italic'))
    red.pack(fill='x')
    white = Label(window,text = "Afaan Oromoo Posts",foreground="red",  bg="white", height=2,font=('Verdana', 12, 'bold', 'italic'))
    white.pack(fill='x')
    lbl = Label(text="Yaada Keessan Galchaa:",font=('Verdana', 12, 'bold', 'italic'))
    lbl.pack()
    lbl.place(x=0,y=200)
    def algorithmGram():
            txti=text.get("1.0",END)
            clalgo=v0.get()
            sr,out= classifierAlgorithm(txti,clalgo)
            #txtresult.delete(0,END)
            txtresult.insert("1.0",sr+':'+ out)
            return
    def clearText():
        text.delete('1.0', END)
        txtresult.delete("1.0", END)
    text = scrolledtext.ScrolledText(window, height=15, width=60)
    s = tkinter.Scrollbar(window)
    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    s.config(command=text.yview)
    text.config(yscrollcommand=s.set)
    text.focus_set()
    text.pack()
    text.place(x=220,y=150)
    lbl1 = Label(text="Algoorizimii Filadhaa:",font=('Verdana', 12, 'bold', 'italic'))
    lbl1.pack()
    lbl1.place(x=0, y=425)
    txtresult = scrolledtext.ScrolledText(window,width=30, height=10)
    txtresult.pack()
    txtresult.place(x=730,y=200)
    txtresult
    v0=IntVar()
    v0.set(2)
    r1=Radiobutton(window, text="Naive Bayes", variable=v0,value=2,font=('Verdana', 10))
    r2=Radiobutton(window, text="Support Vector Machine", variable=v0,value=3,font=('Verdana', 10))
    r3=Radiobutton(window, text="Maximum Entropy", variable=v0,value=4,font=('Verdana', 10))
    r1.pack()
    r1.place(x=220, y=425)
    r2.pack()
    r2.place(x=350, y=425)
    r3.pack()
    r3.place(x=560, y=425)
    b1 = Button(window, text ="Qoqqodi",width=10, font=('Verdana', 10), command=algorithmGram)
    b2 = Button(window, text ="Haqi",width=10,font=('Verdana', 10), command = clearText)
    b3 = Button(window, text ="Cufi",width=10,font=('Verdana', 10), command = window.destroy)
    b1.pack()
    b1.place(x=220, y=500)
    b2.pack()
    b2.place(x=350, y=500)
    b3.pack()
    b3.place(x=560, y=500)
    window.geometry('1000x600')
    window.mainloop()
main()

