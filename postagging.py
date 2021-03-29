# import nltk
# ntlk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import nltk

# list of abbreviations of the tag
# https://www.guru99.com/pos-tagging-chunking-nltk.html

def convertTextToArray(text):
    array = text.splitlines()
    return array

# Regular method to find the POS from a sentence
# Returns an array containing of (word, part-of-speech) in each index
def getPosSentence(sentence):
    tokenized = nltk.word_tokenize(sentence)
    tag = nltk.pos_tag(tokenized)

    return tag

# Method to find the POS in the IMDBot.py
# i.e: this skips the entityArray
# returns an array containing of (word, part-of-speech) in each index
def getPosSentenceEntity(sentence, entityArray):
    
    newSentence = ""
    # Create the sentence array
    for word in sentence.split():
        if word not in entityArray:
            newSentence += word + " "
    
    # print(newSentence)
    tag = getPosSentence(newSentence)

    return tag

# find the Part-of-speech of a certain words from a tagged array
# taggedArray = array that is returned from getPosSentence or getPosSentenceEntity
# word = the word target 
# return the pos if the word is found in the sentence, otherwise return None
def findPOSofWord(taggedArray,word):
    for tuples in taggedArray:
        if tuples[0] == word :
            return tuples[1]
        
    return None


# ----- Testing -----
# tagexample1 = getPosSentence("i am here for you?")
# print(tagexample1)

# entityArray = ["Zendaya", "Spider-Man"]
# tagexample2 = getPosSentenceEntity("Who played Zendaya in Spider-Man",entityArray)
# print(tagexample2)

# entityArray = ["Frozen"]
# tagexample3 = getPosSentenceEntity("Who produced the movie Frozen",entityArray)
# print(tagexample3)
# print(findPOSofWord(tagexample3, "produced"))

