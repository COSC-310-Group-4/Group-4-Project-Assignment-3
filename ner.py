# Named Entity Recognition
# README: Make sure you install the following before trying to run ner.py for the first time
#   1) pip install -U spacy
#   2) pip install spacy-lookups-data
#   3) python -m spacy download en_core_web_sm

import spacy
import nerTrainer
from spacy.language import Language
import time

# TODO: DELETE LATER. FOR TESTING ONLY
print("Loading spaCy...")
t0 = time.time()

# Load pre-existing spacy model and train it. This will take a few seconds. Calls from nerTrainer.py
nlp = nerTrainer.trainSpacy()

# TODO: DELETE LATER. FOR TESTING ONLY.
t1 = time.time()
print('Loading completed in ' + "{:.1f}".format(t1-t0) + ' seconds.')

# Get the pipeline component
ner = nlp.get_pipe("ner")

# Method takes user input, finds all PERSON names, and returns them as an array of strings
def getPersonName(text):
    doc = nlp(text) # Process text
    person = []
    for ent in doc.ents: # Iterate through entities
        if(ent.label_ == "PERSON"): # Find person entities
            person.append(ent.text)
    return " ".join(person)

# Method takes user input, finds all WORK OF ART (movie) names, and returns them as an array of strings
def getMovieName(text):
    doc = nlp(text)
    workOfArt = []
    for ent in doc.ents:
        if(ent.label_ == "WORK_OF_ART"):
            workOfArt.append(ent.text)
    return " ".join(workOfArt)

# Method takes user input, finds all ORG (companies), and returns them as an array of strings.
def getOrgName(text):
    doc = nlp(text)
    org = []
    for ent in doc.ents:
        if(ent.label_ == "ORG"):
            org.append(ent.text)
    return " ".join(org)

# Method takes user input, finds all entities, and returns entities as an array of strings. Used for spelling mistakes and synonym recognition.
def listEntities(text):
    doc = nlp(text) # Process text
    entities = [] # Create blank array
    for ent in doc.ents: # Iterate through entities
        entities.append(ent.text) # Add all entities to the array
    return entities # return an array of entity strings

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FOR TESTING ONLY.
# t1 = time.time()
# print("Load time: " + str(t1-t0))
# while True:
#     print("Give me a sentence, and I'll list the people, movies, and organizations in what you said.")
#     text = input(f'You: ')
#     if text.lower() == "exit":
#         break
#     else:
#         print("Entities: ", end="")
#         print(listEntities(text))
#         print("People: ", end="")
#         print(getPersonName(text))
#         print("Works: ", end="")
#         print(getMovieName(text))
#         print("Organizations: ", end="")
#         print(getOrgName(text))
# print("Exit")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -