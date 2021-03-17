import nltk
from nltk.corpus import wordnet

# holds all arrays
keywords = []

# arrays for the keywords used to find which function should be called 
movieSyn = []
directorSyn = []
summarySyn = []
charactersSyn = []
playedSyn = []
longSyn = []
changeSyn = []
nameSyn = []
nevermindSyn = []
roleSyn = []
otherSyn = []
birthdaySyn = []
placeSyn = []
latestSyn = []
biographySyn = []
companySyn = []
producedSyn = []
goodbyeSyn = []

# Gets the synonyms for the specified word and returns the set.
# Also cleans the elements in the array (i.e., "-" or "_")
# is called by the initSyns() function
def getsyn(word):
    synonyms = []

    for i in wordnet.synsets(word):
        for j in i.lemmas():
            synonyms.append(j.name())

    for i in synonyms:
        if "_" in i:
            new = i.replace("_", " ")
            synonyms.append(new)
            synonyms.remove(i)
        elif "-" in i:
            new = i.replace("-", " ")
            synonyms.append(new)
            synonyms.remove(i)

    return set(synonyms)

# initializes all the arrays with their synonyms and appends them to the keywords array
# called by the synonyms() function
def initSyns():
    movieSyn = getsyn("movie")
    keywords.append(movieSyn)

# Will get the input from IMDBot and use the synonyms to find which function should be called
def synonyms ():
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# the code below is used for testing purposes while implementing
s = getsyn("angry")

input = "playactor"

for i in s:
    if input.lower().__contains__(i):
        print("why?")

if input.lower().__contains__("playact"):
    print("works")