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
# t0 = time.time()

# TODO: For integration, this should be done when the program first loads so that spacy is trained before user interaction.
# Load pre-existing spacy model and train it. This will take a few seconds. Calls from nerTrainer.py
nlp = nerTrainer.trainSpacy()

# Get the pipeline component
ner = nlp.get_pipe("ner")

# Method takes user input, finds all PERSON names, and returns them as an array of strings
def getPersonNames(text):
    doc = nlp(text) # Process text
    people = [] # Create blank array
    for ent in doc.ents: # Iterate through entities
        if(ent.label_ == "PERSON"): # Find person entities
            people.append(ent.text) # Add them to the array
    return people

# Method takes user input, finds all WORK OF ART (movie) names, and returns them as an array of strings
def getMovieNames(text):
    doc = nlp(text)
    worksOfArt = []
    for ent in doc.ents:
        if(ent.label_ == "WORK_OF_ART"):
            worksOfArt.append(ent.text)
    return worksOfArt 

# Method takes user input, finds all ORG (companies), and returns them as an array of strings.
def getOrgNames(text):
    doc = nlp(text)
    orgs = []
    for ent in doc.ents:
        if(ent.label_ == "ORG"):
            orgs.append(ent.text)
    return orgs

# Method takes user input, finds all entities, and returns entities as an array of strings. Used for spelling mistakes and synonym recognition.
def listEntities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append(ent.text)
    return entities

# TODO: DELETE LATER. FOR TESTING ONLY.
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
#         # print("People: ")
#         # print(getPersonNames(text))
#         # print("Works: ")
#         # print(getMovieNames(text))
#         # print("Organizations:")
#         # print(getOrgNames(text))

# print("Exit")