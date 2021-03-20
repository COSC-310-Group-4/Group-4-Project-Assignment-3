# Named Entity Recognition
# README: Make sure you install the following before trying to run ner.py for the first time
#   1) pip install -U spacy
#   2) pip install spacy-lookups-data
#   3) python -m spacy download en_core_web_sm

import spacy
import nerTrainer

# TODO: DELETE LATER. FOR TESTING ONLY
print("Loading spaCy...")

# TODO: For integration, this should be done first so that spacy is trained before user interaction.
# Load pre-existing spacy model and train it. This might take a few seconds. Calls from nerTrainer.py
nlp = nerTrainer.trainSpacy()

# Get the pipeline component
ner = nlp.get_pipe("ner")

# Method to find and return an array of PERSON entities from text
def getPeople(text):
    doc = nlp(text) # Process text
    people = [] # Create blank array
    for ent in doc.ents: # Iterate through entities
        if(ent.label_ == "PERSON"): # Find person entities
            people.append(ent.text) # Add them to the array
    return people # if none are found, will return an empty array

# Method to find and return an array of WORK_OF_ART entities from text
def getWorksOfArt(text):
    doc = nlp(text)
    worksOfArt = []
    for ent in doc.ents:
        if(ent.label_ == "WORK_OF_ART"):
            worksOfArt.append(ent.text)
    return worksOfArt # if none are found, will return an empty array

def getOrganizations(text):
    doc = nlp(text)
    orgs = []
    for ent in doc.ents:
        if(ent.label_ == "ORG"):
            orgs.append(ent.text)
    return orgs # if none are found, will return an empty array

# Method for listing all entities in text
def listEntities(text):
    doc = nlp(text) # Process the text
    entities = []
    for ent in doc.ents: # Iterate over the entities
        entity = (ent.label_, ent.text, ent.start, ent.end)
        entities.append(entity)
    return entities

# TODO: DELETE LATER. FOR TESTING ONLY.
# while True:
#     print("Give me a sentence, and I'll list the people and works of art in what you said.")
#     text = input(f'You: ')
#     if text.lower() == "exit":
#         break
#     else:
#         print(listEntities(text))
#         print("People: ")
#         print(getPeople(text))
#         print("Works: ")
#         print(getWorksOfArt(text))
#         print("Organizations:")
#         print(getOrganizations(text))
# print("Exit")