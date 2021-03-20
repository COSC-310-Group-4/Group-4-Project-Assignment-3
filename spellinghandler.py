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

createDictionary("words.txt")

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
def fixSentence(sentence):
    words = sentence.split() # Convert the sentence into array of words
    newsentence = ""

    for word in words:
        wrongword = spell.unknown([word])
        if wrongword != None:
            word = fixWord(word)
        
        newsentence += word + " " 
            
    return newsentence

# Offer correction by IMDBot instead
def offerCorrection(sentence):
    newsentence = fixSentence(sentence)
    print("IMDBot: Do you mean " + newsentence + "?")


# --------------Testing------------ #

print(fixWord("egt"))
print(fixWord("wnat"))
sen = "egt me an egg please"
sen2 = "i wnat to f1nd a movii called froxen"
print(fixSentence(sen))
offerCorrection(sen)
print(fixSentence(sen2))