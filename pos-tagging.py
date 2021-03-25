# import nltk
# ntlk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import nltk

# list of abbreviations of the tag
# https://www.guru99.com/pos-tagging-chunking-nltk.html

def convertTextToArray(text):
    array = text.splitlines()
    return array

def getPOSfromSentence(sentence):
    sentenceArray = convertTextToArray(sentence)
    for sentence in sentenceArray:
        tokenized = nltk.word_tokenize(sentence)
        tag = nltk.pos_tag(tokenized)
        return tag


# ----- Testing -----
tagexample1 = getPOSfromSentence("i am here for you")
print(tagexample1)