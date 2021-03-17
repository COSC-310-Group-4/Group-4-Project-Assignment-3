import nltk
from nltk.corpus import wordnet

# Gets the synonyms for the specified word and returns the set.
# Also cleans the elements in the array (i.e., "-" or "_")
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
    return synonyms

# initializes all the arrays with their synonyms 
movieSyn = getSyn("movie")
directorSyn = getSyn("director")
summarySyn = getSyn("summary")
charactersSyn = getSyn("characters")
playedSyn = getSyn("played")
longSyn = getSyn("long")
changeSyn = getSyn("change")
nameSyn = getSyn("name")
nevermindSyn = getSyn("disregard")
workedSyn = getSyn("worked")
otherSyn = getSyn("other")
birthdaySyn = getSyn("birthday")
placeSyn = getSyn("place")
latestSyn = getSyn("latest")
biographySyn = getSyn("biography")
companySyn = getSyn("company")
producedSyn = getSyn("produced")
goodbyeSyn = getSyn("goodbye")
    
# takes in the user input and an array (one of the ones initialized previousny)
# compares them and returns 0 or 1 which will indicate which function should be called
def getLocation(input, arr):
    for i in arr:
        if input.__contains__(i):
            return 0
    return 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# the code below is used for testing purposes while implementing
# this would be implemented in IMDBot (replacing what is currently there)
input = "lets talk about a film"
userName = "Monica"

if (getLocation(input, movieSyn) == 0):
    #call findMovie(userName)
    pass
elif (getLocation(input, directorSyn) == 0):
    #check if movie is in locals,
    #call findDirector(movie) if movie is in locals
    #else print error message
    pass
elif (getLocation(input, summarySyn) == 0):
    #check if movie is in locals,
    #call giveSummary(movie) if movie is in locals
    #else print error message
    pass
elif (getLocation(input, charactersSyn) == 0):
    #check if movie is in locals,
    #call showCharacters(movie) if movie is in locals
    #else print error message
    pass
elif (getLocation(input, playedSyn) == 0):
    #check if movie is in locals,
    #splits string where necessary to get character name
    #call whoPlayed(movie, character) if movie is in locals
    #else print error message
    pass
#continues exactly like this until all the synonym arrays have been checked
else:
    #print error message
    pass

# limitation:
#   - synonyms are limited by the synonyms in wordnet
#   - slang cannot be used
#   - can't handle an input having the same synonym for multiple keywords

