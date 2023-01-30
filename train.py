import tkinter
from tkinter import*
from tkinter import scrolledtext
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
def classifierAlgorithm(textinput,clalgo,gram):
    train = [("fayyad du`.","-1"),
             ("gaar baatu","-1"),
             ("salph","-1"),
             ("dadhab","-1"),
             ("jibb","-1"),
             ("abaar","-1"),
             ("sabboon miti","-1"),
             ("sob","-1"),
             ("diin","-1"),
             ("hin beek hin qab","-1"),
             ("faayid hin qab","-1"),
             ("tajaajil hin komat","-1"),
             ("gaar baatu","-1"),("","-1"),
             ("goww","-1"),
             ("hin milkoof","-1"),
             ("diin","-1"),
             ("diin goww","-1"),
             ("gadh","-1"),
             ("baayyee jibb","-2"),
             ("if guddaa sodaa","-2"),
             ("baayyee aar","-2"),
             ("baayyee dadhab","-2"),
             ("baayyee aar","-2"),
             ("olaan hedduu hidh cimaa","-2"),
             ("baayyee gadd","-2"),
             ("baayyee gadd dhugaa hin","-2"),
             ("gadd baayyee dhugaa","-2"),
             ("gadd baayyee dhugaa","-2"),
             ("baayyee qaal","-2"),
             ("baayyee qaal","-2"),
             ("hedduun gadd","-2"),
             ("baayyee fokkis","-2"),
             ("baayyee madeess","-2"),
             ("dhugaa falm diin miti","+2"),
             ("baayyee baayyee bareed","+2"),
             ("baayyee miidhag","+2"),
             ("tol guutummaadhumatti miidhag","+2"),
             ("baayyee gaar bareed qab","+2"),
             ("baayyee bareed gaar","+2"),
             ("hedduu gaar bilchaat","+2"),
             ("baayyee eebbis eebba","+2"),
             ("dhugaa jaalal dhugaa","+2"),
             ("bareed dhugaa","+2"),
             ("baayyee tol","+2"),
             ("baayyee miidhag galat","+2"),
             ("hedduu tol","+2"),
             ("baayyee bareed qab","+2"),
             ("bareed baayyee tol","+2"),
             ("hedduu jaalla","+2"),
             ("baayyee jaalla","+2"),
             ("guddina caalaatti gabbis baayyee murteessaa","+2"),
             ("baayyee milkoof","+2"),
             ("baayyee cimaa","+2"),
             ("dhugaa qab","+2"),
             ("haalaan bareed","+2"),
             ("baayyee tol jab","+2"),
             ("qash baayyee tol","+2"),
             ("baayyee baayyee galat","+2"),
             ("nag","+1"),
             ("milkoof","+1"),
             ("gaar","+1"),
             ("gammad","+1"),
             ("rakk miti","+1"),
             ("gaar","+1"),
             ("bareed","+1"),
             ("bareed","+1"),
             ("bareed","+1"),
             ("gaar","+1"),
             ("gaar qab","+1"),
             ("gaar","+1"),
             ("gammachiis","+1"),
             ("gaar","+1"),
             ("bareed","+1"),
             ("gaar","+1"),
             ("bareed qab","+1"),
             ("darar hin","+1"),
             ("bareed","+1"),
             ("miidhag","+1"),
             ("goot","+1"),
             ("ulf jaallat","+1"),
             ("haq","+1"),
             ("jab","+1"),]
    test_data =[
        ("gaar baatu","-1"),
        ("salph","-1"),
        ("dadhab","-1"),
        ("hin milkoof","-1"),
        ("jibb","-1"),
        ("baayyee qaal","-2"),
        ("baayyee qaal","-2"),
        ("hedduun gadd","-2"),
        ("baayyee fokkis","-2"),
        ("baayyee madeess","-2"),
        ("bareed","+1"),
        ("gaar","+1"),
        ("gaar qab","+1"),
        ("gaar","+1"),
        ("gammachiis","+1"),
        ("baayyee milkoof","+2"),
        ("baayyee cimaa","+2"),
        ("dhugaa qab","+2"),
        ("haalaan bareed","+2"),
        ("baayyee tol jab","+2"),
        ("qash baayyee tol","+2"),
        ]
    with open("D:\Senti-Corpus\sentiment_data\spos.txt", 'r') as filehandle:
        strong_positive = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_sps = [((spsnt), '+2') for spsnt in strong_positive]
        filehandle.close()
    with open("D:\Senti-Corpus\sentiment_data\pos.txt", 'r') as filehandle:
        positive = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_ps = [((spsnt), '+1') for spsnt in positive]
        for i in range(len(dc_ps)):
            dc_sps.append(dc_ps[i])
        filehandle.close()
    with open("D:\Senti-Corpus\sentiment_data\sneg.txt", 'r') as filehandle:
        strong_negative = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_sng = [((spsnt), '-2') for spsnt in strong_negative]
        for k in range(len(dc_sng)):
            dc_sps.append(dc_sng[k])
        filehandle.close()
    #Code to open negative sentences
    with open("D:\Senti-Corpus\sentiment_data\\neg.txt", 'r') as filehandle:
        negative = [current_place.rstrip() for current_place in filehandle.readlines()]
        dc_ng = [((spsnt), '-1') for spsnt in negative]
        for z in range(len(dc_ng)):
            dc_sps.append(dc_ng[z])
        filehandle.close()
    # Step 2
    dictionary = set(word.lower() for passage in dc_sps for word
    in word_tokenize(passage[0]))
    # Step 3
    t = [({word: (word in word_tokenize(x[0])) for word in
    dictionary}, x[1]) for x in dc_sps]
    # Step 4 – the classifier is trained with sample data
    classifier = nltk.NaiveBayesClassifier.train(t)
    #classifierm = nltk.MaxentClassifier.train(t)
    classifiersvm = nltk.classify.SklearnClassifier(LinearSVC())
    classifiersvm.train(t)
    me_classifier=MaxentClassifier.train(t,algorithm='gis',trace=0,max_iter=10,min_lldelta=0.5)
    # Step 2
    dic = set(word.lower() for passage in test_data for word
    in word_tokenize(passage[0]))
    # Step 3
    tt = [({word: (word in word_tokenize(x[0])) for word in
    dic}, x[1]) for x in test_data]
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
    tdsvm=[(textinput,(classifiersvm.classify(test_data_features)))
    ]

    # Step 22
    dcsvm = set(word.lower() for passage in tdsvm for word
    in word_tokenize(passage[0]))
    # Step 33
    tddsvm = [({word: (word in word_tokenize(x[0])) for word in
    dcsvm}, x[1]) for x in tdsvm]
    #----------------------------------------------------
    #--------------------------Max-----------------
    tdmax=[(textinput,(me_classifier.classify(test_data_features)))
    ]

    # Step 22
    dcmax = set(word.lower() for passage in tdmax for word
    in word_tokenize(passage[0]))
    # Step 33
    tddmax = [({word: (word in word_tokenize(x[0])) for word in
    dcmax}, x[1]) for x in tdmax]
    #----------------------------------------------------
    '''refsets = collections.defaultdict(set)
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
    neg_fmeasure =  f_measure(refsets['-1'], testsets['-1'])'''
    #print(0,spos_precision,spos_recall,spos_recall,spos_fmeasure,pos_precision,pos_recall,pos_fmeasure,sneg_precision,sneg_recall,sneg_fmeasure,neg_precision,neg_recall,neg_fmeasure)
    '''print("NB:",textinput,'"',classifier.classify(test_data_features),'"')
    print("SVM:",textinput,'"',classifiersvm.classify(test_data_features),'"')
    print("Max:",textinput,'"',me_classifier.classify(test_data_features),'"')
    #print("Maxet:",c,'"',classifierm.classify(test_data_features),'"')
    #classifier.show_most_informative_features()
    print("Accuracy NB:",nltk.classify.accuracy(classifier, tt))
    print("Accuracy SVM:",nltk.classify.accuracy(classifiersvm, tt))
    print("Accuracy Maxent:",nltk.classify.accuracy(me_classifier, tt))
    #print("Input-Accuracy nb:",nltk.classify.accuracy(classifier, tddnb))
    #print("Input-Accuracy SVM:",nltk.classify.accuracy(classifiersvm, tddsvm))
    #print("Input-Accuracy Maxent:",nltk.classify.accuracy(me_classifier, tddmax))
    print ('---------------------------------------')
    print ('             Evaluation               ')
    print ('---------------------------------------')
    print ('precision', (spos_precision + sneg_precision + neg_precision + pos_precision) / 4)
    print ('recall', (spos_recall + sneg_recall + neg_recall + pos_recall) / 4)
    print ('f-measure', (spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure) / 4)'''
    out = classifier.classify(test_data_features)
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
            gram=ch1.get()
            sr,out= classifierAlgorithm(txti,clalgo,gram)
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
    lbg = Label(text="N-Grams:",font=('Verdana', 12, 'bold', 'italic'))
    lbg.pack()
    lbg.place(x=0, y=500)
    ch1 = IntVar()
    ch1.set(11)
    c1 = Checkbutton(window, text = "Unigram", variable = ch1,onvalue = 11,font=('Verdana', 10))
    c2 = Checkbutton(window, text = "Bigram", variable = ch1,onvalue = 22,font=('Verdana', 10))
    c3 = Checkbutton(window, text = "Trigram", variable = ch1,onvalue = 33,font=('Verdana', 10))
    c1.pack()
    c1.place(x=220, y=500)
    c2.pack()
    c2.place(x=350, y=500)
    c3.pack()
    c3.place(x=560, y=500)
    b1 = Button(window, text ="Qoqqodi",width=10, font=('Verdana', 10), command=algorithmGram)
    b2 = Button(window, text ="Haqi",width=10,font=('Verdana', 10), command = clearText)
    b3 = Button(window, text ="Cufi",width=10,font=('Verdana', 10), command = window.destroy)
    b1.pack()
    b1.place(x=220, y=600)
    b2.pack()
    b2.place(x=400, y=600)
    b3.pack()
    b3.place(x=580, y=600)
    window.geometry('1000x1000')
    window.mainloop()
main()

