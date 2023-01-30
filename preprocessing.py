import nltk
import re
import string
import io
def Tokenization():
        corpus = open('ch.txt',encoding='utf-8')
        corpusfile = corpus.read();
        corpus.close()
        an_exact_year_symbol_romoved_sentence = corpusfile.replace('(?)', '') #(?) remover
        accronmies_removed_sentence=re.sub(r"\b[A-Z][a-zA-Z\.]*[A-Z]\b\.?",'',an_exact_year_symbol_romoved_sentence)#Accronomy remover
        foriegn_langs_replaced_sentence = re.sub('Dr.','Dooktara ',accronmies_removed_sentence)#Replace Dr. with the 'Dooktara' word
        formalized_sentence = re.sub('100%','hedduu',foriegn_langs_replaced_sentence)#Replace 100% with the 'hedduu' word
        times_removed_sentence = re.sub('\d+:\d+','',formalized_sentence) #Time Remover
        decimals_removed_sentence = re.sub("[-+]?\d*\.\d+",'',times_removed_sentence) #Decimal and Sub-Topic Numbers Remover
        topics_removed_sentence = re.sub("[-+]?\d+\.",'',decimals_removed_sentence) #Topic Numbers Remover
        number_removed_sentence = re.sub(r'\d+', '', topics_removed_sentence) #Numbers remover
        #Jump the first tokens and apply the following
        #named_entity_removed_sentence = re.sub(r"(?<!\.\s)(?!^)\b([A-Z]\w*(?:\s+[A-Z]\w*)*)", '', number_removed_sentence)
        tokinized_sentence = re.findall(r"\w+[^.!?]*[.!?]", number_removed_sentence)  # match sentences ending with . ? !
        return tokinized_sentence
def numberofLines(toke_of_sentence):
        num_lines = 0
        for line in toke_of_sentence:
                num_lines +=line.count('.') + line.count('!') + line.count('?')
        total_lines = num_lines
        return total_lines
def RemoveSymbolsPunctuations(snt):
        string = ''.join(char for char in snt if char not in '!()[]{};:"“\,<>.”/?@#$%^&*_~+')
        return string
def stopwordRemovals(words):
        stop_word_file = open("stopwords.txt")
        stopwords = stop_word_file.read()# Use this to read file content as a stream:
        stoplist = stopwords.split()
        words = words.split()
        clean = [word for word in words if word.lower() not in stoplist]
        return clean
def textNormalization(clean_sentence):
        r = str =  ' '.join(clean_sentence)
        case_folded_sentence = r.lower() #Case folding(lower casing)
        space_removed_sentence = re.sub(r"\s+"," ", case_folded_sentence, flags = re.I)#Space...Normalization
        baay_norm = re.sub("baay'ee|baay`een|baayyeen|baay`isee|baayyisee|baay`ee|baay`eetti|baay`inaan|baayyeetti|baayyinaan","baayyee",space_removed_sentence)#Apohostrophe Normalization
        negatio_normalized = re.sub("baattu|baattus|baattanis|baattanillee|baattellee|baattullee|baattan|baatan|baatte|baattanis|baatteef|baattanif|baatus","baatu",baay_norm,re.IGNORECASE)#Negation Normalization
        normalized = re.sub("baleddu|bayeettii","bareeddu",negatio_normalized)#Apohostrophe Normalization
        return normalized
def main():
        i = 0
        ls = list()
        syb_pnc_removed = list()
        tokenized_sentences = Tokenization()
        total_num_line = numberofLines(tokenized_sentences)
        #print(total_num_line)
        for sentence in tokenized_sentences:
                symbols_punctuations_removal = RemoveSymbolsPunctuations(sentence)
                syb_pnc_removed.append(symbols_punctuations_removal)
                stp = stopwordRemovals(symbols_punctuations_removal)
                normalization = textNormalization(stp)
                ls.append(normalization)
                #print(normalization)
        return syb_pnc_removed,ls
#main()
