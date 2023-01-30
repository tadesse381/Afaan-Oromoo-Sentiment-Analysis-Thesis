import tkinter
from tkinter import*
from tkinter import scrolledtext
import collections
import itertools
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import afaan_oromoo_reviews
from nltk.metrics import precision, recall, f_measure
from nltk.util import trigrams
from nltk.classify import SklearnClassifier
from sklearn.svm import LinearSVC, SVC
from nltk.classify import MaxentClassifier
def classifierAlgorithm(textinput,clalgo,gram):
        print(clalgo,gram)
        #Unigrams
        def word_feats(words):
                return dict([(word, True) for word in words])
        #Bigrams
        def bigrams(nltk_tokens):
            bigram=(list(nltk.bigrams(nltk_tokens)))
            return dict([(bigram[i], True) for i in range(len(bigram))])
        #Trigrams
        def trigrams(nltk_tokens):
            trigram=(list(nltk.trigrams(nltk_tokens)))
            return dict([(trigram[i], True) for i in range(len(trigram))])
        #Code to open strong positive sentences 
        with open("D:\Senti-Corpus\sentiment_data\spos.txt", 'r') as filehandle:
            strong_positive = [current_place.rstrip() for current_place in filehandle.readlines()]
            if gram==11:
                    dc_sps = [(word_feats(nltk.word_tokenize(spsnt)), '+2') for spsnt in strong_positive]
            '''elif gram==22:
                    dc_sps = [(bigrams(nltk.word_tokenize(spsnt)), '+2') for spsnt in strong_positive]
            elif gram==33:
                    dc_sps = [(trigrams(nltk.word_tokenize(spsnt)), '+2') for spsnt in strong_positive]
            filehandle.close()'''
        #Code to open positive sentences 
        with open("D:\Senti-Corpus\sentiment_data\pos.txt", 'r') as filehandle:
            positive = [current_place.rstrip() for current_place in filehandle.readlines()]
            if gram==11:
                    dc_ps = [(word_feats(nltk.word_tokenize(spsnt)), '+1') for spsnt in positive]
           '''elif gram==22:
                    dc_ps = [(bigrams(nltk.word_tokenize(spsnt)), '+1') for spsnt in positive]
            elif gram==33:
                    dc_ps = [(trigrams(nltk.word_tokenize(spsnt)), '+1') for spsnt in positive]
            filehandle.close()'''
        #Code to open strong negative sentences 
        with open("D:\Senti-Corpus\sentiment_data\sneg.txt", 'r') as filehandle:
            strong_negative = [current_place.rstrip() for current_place in filehandle.readlines()]
            dc_sng = [(word_feats(nltk.word_tokenize(spsnt)), '-2') for spsnt in strong_negative]
            if gram==11:
                    dc_sng = [(word_feats(nltk.word_tokenize(spsnt)), '-2') for spsnt in strong_negative]
            '''elif gram==22:
                    dc_sng = [(bigrams(nltk.word_tokenize(spsnt)), '-2') for spsnt in strong_negative]
            elif gram==33:
                    dc_sng = [(trigrams(nltk.word_tokenize(spsnt)), '-2') for spsnt in strong_negative]
            filehandle.close()'''
        #Code to open negative sentences
        with open("D:\Senti-Corpus\sentiment_data\\neg.txt", 'r') as filehandle:
            negative = [current_place.rstrip() for current_place in filehandle.readlines()]
            if gram==11:
                    dc_ng = [(word_feats(nltk.word_tokenize(spsnt)), '-1') for spsnt in negative]
            '''elif gram==22:
                    dc_ng = [(bigrams(nltk.word_tokenize(spsnt)), '-1') for spsnt in negative]
            elif gram==33:
                    dc_ng = [(trigrams(nltk.word_tokenize(spsnt)), '-1') for spsnt in negative]
            filehandle.close()'''
        '''#Code to open nuetral sentences
        with open("D:\Senti Corpus\sentiment_data\sneg.txt", 'r') as filehandle:
            neut = [current_place.rstrip() for current_place in filehandle.readlines()]
            dc_nuet = [(word_feats(nltk.word_tokenize(spsnt)), '0') for spsnt in neut]
            if gram==11:
                    dc_nuet = [(word_feats(nltk.word_tokenize(spsnt)), '0') for spsnt in neut]
            elif gram==22:
                    dc_nuet = [(bigrams(nltk.word_tokenize(spsnt)), '0') for spsnt in neut]
            elif gram==33:
                    dc_nuet = [(trigrams(nltk.word_tokenize(spsnt)), '0') for spsnt in neut]
            filehandle.close()'''
        sposfeats = dc_sps
        posfeats = dc_ps
        snegfeats = dc_sng
        negfeats = dc_ng
        #nuetfeats = dc_nuet
        #print('Neutral Sentence',nuetfeats)
        snegcutoff = int(len(snegfeats)*3/4)
        negcutoff = int(len(negfeats)*3/4)
        sposcutoff = int(len(sposfeats)*3/4)
        poscutoff = int(len(posfeats)*3/4)
        #nuetcutoff = int(len(nuetfeats)*3/4)
        #print('Neutral',nuetcutoff)
        trainfeats=sposfeats + posfeats + snegfeats + negfeats
        #trainfeats = snegfeats[:snegcutoff] + negfeats[:negcutoff] + sposfeats[:sposcutoff] + posfeats[:poscutoff]
        testfeats = snegfeats[snegcutoff:] + negfeats[negcutoff:] + sposfeats[sposcutoff:] + posfeats[poscutoff:]
        print(trainfeats)
        print('train on %d instances, test on %d instances - SVM' % (len(trainfeats), len(testfeats)))
        if clalgo==2:
                classifier = NaiveBayesClassifier.train(trainfeats)
        '''elif clalgo==3:
                classifier = NaiveBayesClassifier.train(trainfeats)
                classifier = SklearnClassifier(LinearSVC(), sparse=False)
                classifier.train(trainfeats)
        elif clalgo==4:
                classifier = NaiveBayesClassifier.train(trainfeats)
                classifier = MaxentClassifier.train(trainfeats, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 1)'''
        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)
         
        for i, (feats, label) in enumerate(testfeats):
                refsets[label].add(i)
                observed = classifier.classify(feats)
                testsets[observed].add(i)
        accuracy = nltk.classify.util.accuracy(classifier, testfeats)
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

        '''nuet_precision = precision(refsets['0'], testsets['0'])
        nuet_recall = recall(refsets['0'], testsets['0'])
        nuet_fmeasure = f_measure(refsets['0'], testsets['0'])'''

        print(spos_recall,spos_precision,sneg_precision,sneg_recall,neg_precision,neg_recall,pos_precision,pos_recall,pos_fmeasure)
        input_sentence=textinput
        print(input_sentence)
        sr=classifier.classify(word_feats(input_sentence))
        out=(input_sentence+": ("+classifier.classify(word_feats(input_sentence))+")")		
        #txtresult.insert(0,sr)
        print("SVM:",input_sentence,'"',classifier.classify(word_feats(input_sentence)),'"')		
        print('')
        print ('---------------------------------------')
        print ('             NAIVE BAYES               ')
        print ('---------------------------------------')
        print ('accuracy:', accuracy)
        #classifier.show_most_informative_features()
        print ('precision', (spos_precision + sneg_precision + neg_precision + pos_precision) / 4)
        print ('recall', (spos_recall + sneg_recall + neg_recall + pos_recall) / 4)
        print ('f-measure', (spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure) / 4)
        #classifier.show_most_informative_features()
        return sr,out
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
            txtresult.insert("1.0",out)
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


