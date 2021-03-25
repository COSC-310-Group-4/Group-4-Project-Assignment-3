# Installations:
# pip install ntlk (if not already installed)
# In Python:
# >>> import nltk
# >>> nltk.download()
# Download window opens, under corpus, download wordnet

import nltk
from nltk.corpus import wordnet

# takes the sentance the user inputs as well as a list of entities from NER 
# and returns an array of all words in the user input that does not include words in
# the list of entities. 
def getArray(input, entities):
    if (" " in input):
        arr = input.split(" ")
        for i in entities:
            for j in arr:
                if i == j:
                    arr.remove(j)
        return arr
    else:
        return input

# gets all the synonyms for a specified word and returns an array of those synonyms
def getSyn(word):
    synonyms = []

    # for each element in the synonym set for the specified word, the "name" attribute
    # is appended to the synonyms array
    for i in wordnet.synsets(word):
        for j in i.lemmas():
            synonyms.append(j.name())

    # removes special characters that wordnet uses for synonyms that are 2 words
    for i in synonyms:
        if "_" in i:
            new = i.replace("_", " ")
            synonyms.append(new)
            synonyms.remove(i)
        elif "-" in i:
            new = i.replace("-", " ")
            synonyms.append(new)
            synonyms.remove(i)
    
    # returns the synonyms array
    return synonyms

# if the keyword specified to call each function is a synonym for the input the user
# entered, the function returns 0 (it has been found) else, it return 1 (not found)
# arr = the user input broken up into an array; w = keyword being looked for
def findSyns(arr, w):
    s = []
    found = 1
    
    # if w is in arr, return 0
    # else find the synonyms for each word in arr and if the synonyms contain w, return 0
    if (arr.__contains__(w)):
        found = 0
    else:
        for i in range(len(arr)):
            word = arr[i]
            s = getSyn(word)
            if (s.__contains__(w)): # changed back to s.__contains__(w) because w.__contains__(s) returned an error
                found = 0
                break
    
    return found

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Used for testing purposes:
# input = "Tell me the characters"
# entities = ['The Matrix']

# a = getArray(input, entities)
# print(a)

# res = findSyns(a, "summary")
#print(res)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# the below code is how synonyms would be implemented into IMDBot:
# entities = ["The Avengers"]
# user_input = getArray(input.lower(), entities)

# if (findSyns(user_input, "characters") == 0):
     # call findMove(user_Name)
    # print("Ok, let's talk about a movie")
# elif(findSyns(user_input, "director") == 0):
#     # check if movie in locals(), 
#     # call findDirector(movie)
#     # if movie not in locals(), display error message
#     print("director")
#     pass
# elif (findSyns(user_input, "summary") == 0):
#     # check if movie in locals(), 
#     # call giveSummary(movie)
#     # if movie not in locals(), display error message
#     print("summary")
#     pass
# elif (findSyns(user_input, "characters") == 0):
#     # check if movie in locals(), 
#     # call showCharacters(movie)
#     # if movie not in locals(), display error message
#     print("characters")
#     pass
# # ... etc ...
# else:
#     #display error msg
    # print("Sorry, i didn't quite get that")
#     pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Limitations:
#   - synonyms are limited by the synonyms in wordnet
#   - slang cannot be used
#   - some keywords have the same synonyms (i.e, "role" is a synonym for "character" and "worked")
#       this can be conflicting depending on what the user wants to ask the chatbot