import nltk
import re
def sentenceTokinization():
        corpus = open('corpus.txt')
        corpusfile = corpus.read();
        tokinized_sentence = re.findall(r"\w+[^.!?]*[.!?]", corpusfile)  # match sentences ending with . !
        num_lines = 0
        for line in tokinized_sentence:
                num_lines +=line.count('.') + line.count('!') + line.count('?')
        total_lines = num_lines
        print(total_lines)
        i=0
        while i<total_lines:
                print(tokinized_sentence[i].split())
                i=i+1
def main():
        s=sentenceTokinization()
main()
