import nltk
import re
additional_stopwords = """case my there judge judgment court"""
# Split the the additional stopwords string on each word and then add
# those words to the NLTK stopwords list
stoplist = additional_stopwords.split()
text = "baay'ee abebe my there"
formalized_sentence = re.sub("baay'ee",'baayyee',text)#Replace 100% with the 'hedduu' word
print(formalized_sentence)
# Apply the stoplist to the text
clean = [word for word in text.split() if word not in stoplist]
print(clean)
