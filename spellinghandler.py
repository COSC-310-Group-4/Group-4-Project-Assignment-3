# Installation Instructions:
# pip install pyspellchecker

import string
from spellchecker import SpellChecker

# Create a dictionary of some mispelled words as key, and correct word as value
# This is because some words are not flagged as mispelled by pyspellchecker 
# for example "wnat" is not fixed to "want"
dictionary = {}

def createDictionary(file):
    f = open(file)
    for line in f:
        (key,val) = line.split()
        dictionary[key] = val

createDictionary("./words.txt") # TODO: This line is giving Veronica errors and not sure why

# Instantiate a SpellChecker object
spell = SpellChecker()

# Fix a word by first checking in the dictionary, if it doesn't exist use pyspellchecker
def fixWord(word):
    for key in dictionary:
        if word == key:
            return dictionary[key]
        else:
            return spell.correction(word)

# Fix a complete sentence
# sentence = sentence to be fixed
# entityArray = array of entities extracted from named-entity recognition
def fixSentence(sentence, entityArray):

    punctuation = None #
    if sentence[-1] in string.punctuation: # remove punctuation at the very end of the string
        punctuation = sentence[-1]
        sentence = sentence[:-1]

    words = sentence.split() # Convert the sentence into array of words
    newsentence = ""
    mistakeFound = False # keep track if the user input contains spelling mistake
    
    
    for word in words:
        
        if word in entityArray:
            newsentence += word + " "
        else:
            wrongword = spell.unknown([word]) # assign the mispelled word to wrongword variable

            if (len(wrongword)==1): # if wrong word exists, fix the word
                word = fixWord(word)
                mistakeFound = True

            newsentence += word + " " 

    if punctuation != None:
        newsentence += punctuation

    if mistakeFound == True:
        print("IMDBot: ----- Spelling error found, below is the fixed sentence -----")
        print("IMDBot: " + newsentence)

    return newsentence

# Offer correction by IMDBot instead
def offerCorrection(sentence,entityArray):
    newsentence = fixSentence(sentence, entityArray)
    print("IMDBot: Do you mean " + newsentence + "?")


# --------------Testing------------ #

# print(fixWord("egt"))
# print(fixWord("wnat"))

# entityArray = ["Zendaya","Spider-man"]
# print(fixSentence("Whof plaked Zendaya inm Spider-man?",entityArray))