import collections
import itertools
import nltk.classify.util, nltk.metrics
from nltk.classify import SklearnClassifier
from nltk.metrics import precision, recall, f_measure
from nltk.corpus import afaan_oromoo_reviews
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def word_feats(words):
	return dict([(word, True) for word in words])

snegids = afaan_oromoo_reviews.fileids('sneg')
negids = afaan_oromoo_reviews.fileids('neg')
sposids = afaan_oromoo_reviews.fileids('spos')
posids = afaan_oromoo_reviews.fileids('pos')
nuetids = afaan_oromoo_reviews.fileids('nuet')

snegfeats = [(word_feats(afaan_oromoo_reviews.words(fileids=[f])), '-2') for f in snegids]
negfeats = [(word_feats(afaan_oromoo_reviews.words(fileids=[f])), '-1') for f in negids]
sposfeats = [(word_feats(afaan_oromoo_reviews.words(fileids=[f])), '+2') for f in sposids]
posfeats = [(word_feats(afaan_oromoo_reviews.words(fileids=[f])), '+1') for f in posids]
nuetfeats = [(word_feats(afaan_oromoo_reviews.words(fileids=[f])), '0') for f in nuetids]
print(sposfeats)
snegcutoff = int(len(snegfeats)*3/4)
negcutoff = int(len(negfeats)*3/4)
sposcutoff = int(len(sposfeats)*3/4)
poscutoff = int(len(posfeats)*3/4)
nuetcutoff = int(len(nuetfeats)*3/4)

trainfeats = snegfeats[:snegcutoff] + negfeats[:negcutoff] + sposfeats[:sposcutoff] + posfeats[:poscutoff] + nuetfeats[:nuetcutoff]
testfeats = snegfeats[snegcutoff:] + negfeats[negcutoff:] + sposfeats[sposcutoff:] + posfeats[poscutoff:] + nuetfeats[nuetcutoff:]
print(trainfeats)
print('train on %d instances, test on %d instances - SVM' % (len(trainfeats), len(testfeats)))

classifier = SklearnClassifier(LinearSVC(), sparse=False)
classifier.train(trainfeats)

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)
 
for i, (feats, label) in enumerate(testfeats):
	refsets[label].add(i)
	observed = classifier.classify(feats)
	testsets[observed].add(i)
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})
a='gowwaa'
print("SVM:",a,'"',classifier.classify(format_sentence(a)),'"') 
#tdnb=[(a,(classifier.classify(format_sentence(a)))]
c=(classifier.classify(format_sentence(a)))
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

nuet_precision = precision(refsets['0'], testsets['0'])
nuet_recall = recall(refsets['0'], testsets['0'])
nuet_fmeasure = f_measure(refsets['0'], testsets['0'])

print(spos_recall,spos_precision,sneg_precision,sneg_recall,neg_precision,neg_recall,pos_precision,pos_recall,pos_fmeasure,nuet_precision,nuet_recall,nuet_fmeasure)
	
print('')
print ('---------------------------------------')
print ('                  SVM                  ')
print ('---------------------------------------')
print ('accuracy:', accuracy)
print ('precision', (spos_precision + sneg_precision + neg_precision + pos_precision+ nuet_precision) / 5)
print ('recall', (spos_recall + sneg_recall + neg_recall + pos_recall + nuet_recall) / 5)
print ('f-measure', (spos_fmeasure + sneg_fmeasure + neg_fmeasure + pos_fmeasure + nuet_fmeasure) / 5)

