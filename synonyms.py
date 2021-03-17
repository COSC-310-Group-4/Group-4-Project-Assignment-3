import nltk
from nltk.corpus import wordnet

# holds all arrays
keywords = []

# arrays for the keywords used to find which function should be called 
# the number beside each array indicate it's index in keywords
movieSyn = [] #0
directorSyn = [] #1
summarySyn = [] #2
charactersSyn = [] #3
playedSyn = [] #4
longSyn = [] #5
changeSyn = [] #6
nameSyn = [] #7
nevermindSyn = [] #8
workedSyn = [] #9
otherSyn = [] #10
birthdaySyn = [] #11
placeSyn = [] #12
latestSyn = [] #13
biographySyn = [] #14
companySyn = [] #15
producedSyn = [] #16
goodbyeSyn = [] #17

# Gets the synonyms for the specified word and returns the set.
# Also cleans the elements in the array (i.e., "-" or "_")
# is called by the initSyns() function
def getSyn(word):
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
    movieSyn = getSyn("movie")
    keywords.append(movieSyn)

    directorSyn = getSyn("director")
    keywords.append(directorSyn)

    summarySyn = getSyn("summary")
    keywords.append(summarySyn)

    charactersSyn = getSyn("characters")
    keywords.append(charactersSyn)

    playedSyn = getSyn("played")
    keywords.append(playedSyn)

    longSyn = getSyn("long")
    keywords.append(longSyn)

    changeSyn = getSyn("change")
    keywords.append(changeSyn)

    nameSyn = getSyn("name")
    keywords.append(nameSyn)

    nevermindSyn = getSyn("disregard")
    keywords.append(nevermindSyn)

    workedSyn = getSyn("worked")
    keywords.append(workedSyn)

    otherSyn = getSyn("other")
    keywords.append(otherSyn)

    birthdaySyn = getSyn("birthday")
    keywords.append(birthdaySyn)

    placeSyn = getSyn("place")
    keywords.append(placeSyn)

    latestSyn = getSyn("latest")
    keywords.append(latestSyn)

    biographySyn = getSyn("biography")
    keywords.append(biographySyn)

    companySyn = getSyn("company")
    keywords.append(companySyn)

    producedSyn = getSyn("produced")
    keywords.append(producedSyn)

    goodbyeSyn = getSyn("goodbye")
    keywords.append(goodbyeSyn)
    
# Will get the input from IMDBot and use the synonyms to find which function should be called
# if the input contains a synonym for 2 different keywords, throw an error
def synonyms ():
   pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# the code below is used for testing purposes while implementing

initSyns()
