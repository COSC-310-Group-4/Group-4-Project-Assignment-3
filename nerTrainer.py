# This trains the current spacy NER for out chatbot

# spaCy supports these entity types:
# PERSON, NORP (nationalities, religious and political groups), FAC (buildings, airports etc.),
# ORG (organizations), GPE (countries, cities etc.), LOC (mountain ranges, water bodies etc.),
# PRODUCT (products), EVENT (event names), WORK_OF_ART (books, song titles), LAW (legal document titles),
# LANGUAGE (named languages), DATE, TIME, PERCENT, MONEY, QUANTITY, ORDINAL and CARDINAL.

# We are training and using PERSON, WORK_OF_ART, and ORG

import spacy
import random
from spacy.tokens import Doc
from spacy.training import Example
from spacy.util import minibatch
from spacy.language import Language

def trainSpacy(): # This is called in ner.py DO NOT call it elsewhere.
    # Load existing spacy model
    nlp = spacy.load('en_core_web_sm')
    
    # Training Data. Note: when adding data, the end index needs to be +1 than then length of the entity. Use nerTrainDataHelp.py for assistance
    TRAIN_DATA = [("Who played Neo in The Matrix?", {"entities": [(11, 14, "PERSON"), (18, 28, "WORK_OF_ART")]}),
                ("Who played Wanda Maximoff in The Avengers?", {"entities": [(11, 25, "PERSON"), (29, 41, "WORK_OF_ART")]}),
                ("Who played Wanda in WandaVision?", {"entities": [(11, 16, "PERSON"), (20, 31, "WORK_OF_ART")]}),
                ("Who played Vision in The Avengers?", {"entities": [(11, 17, "PERSON"), (21, 33, "WORK_OF_ART")]}),
                ("Which actor played Jarvis in Iron Man 2?", {"entities": [(19, 25, "PERSON"), (29, 39, "WORK_OF_ART")]}),
                ("Who played Pepper Potts in Iron Man?", {"entities": [(11, 23, "PERSON"), (27, 35, "WORK_OF_ART")]}),
                ("Who played Happy Hogan in Spider-Man: Homecoming?", {"entities": [(11, 22, "PERSON"), (26, 48, "WORK_OF_ART")]}),
                ("Which actor played Spider-Man in Spider-Man: Far from Home?", {"entities": [(19, 29, "PERSON"), (33, 58, "WORK_OF_ART")]}),
                ("Who played Manfred in Ice Age?", {"entities": [(11, 18, "PERSON"), (22, 29, "WORK_OF_ART")]}),
                ("Which actor played Deadpool in Deadpool 2?", {"entities": [(19, 27, "PERSON"), (31, 41, "WORK_OF_ART")]}),
                ("Which actor was the voice of Lord Farquaad in Shrek?", {"entities": [(29, 42, "PERSON"), (46, 51, "WORK_OF_ART")]}),
                ("Which actor was the voice of Chef in South Park: Bigger, Longer & Uncut?", {"entities": [(29, 33, "PERSON"), (37, 71, "WORK_OF_ART")]}),                 
                ("Who was The Witch in Brave?", {"entities": [(8, 17, "PERSON"), (21, 26, "WORK_OF_ART")]}),
                ("Who was Aunt May in Spider-Man: Into the Spider-Verse?", {"entities": [(8, 16, "PERSON"), (20, 53, "WORK_OF_ART")]}),
                ("Who played Maui in Moana?", {"entities": [(11, 15, "PERSON"), (19, 24, "WORK_OF_ART")]}),
                ("Who are the characters in Frozen?", {"entities": [(26, 32, "WORK_OF_ART")]}),
                ("Who are the characters in A Series of Unfortunate Events?", {"entities": [(26, 56, "WORK_OF_ART")]}),
                ("Can you tell me which actor played Captain America in the movie Captain America: The First Avenger?", {"entities": [(35, 50, "PERSON"), (64, 98, "WORK_OF_ART")]}),
                ("Can you tell me who played Nick Fury in Avengers: Infinity War?", {"entities": [(27, 36, "PERSON"), (40, 62, "WORK_OF_ART")]}),
                ("Do you know which actor played Elastigirl in Incredibles 2?", {"entities": [(31, 41, "PERSON"), (45, 58, "WORK_OF_ART")]}),
                ("Do you know which actor played Mystique in X-Men?", {"entities": [(31, 39, "PERSON"), (43, 48, "WORK_OF_ART")]}),
                ("What role did Chris Hemsworth play in Avengers: Age of Ultron?", {"entities": [(14, 29, "PERSON"), (38, 61, "WORK_OF_ART")]}),
                ("What role did Ryan Reynolds play in Pokémon Detective Pikachu?", {"entities": [(14, 27, "PERSON"), (36, 61, "WORK_OF_ART")]}),
                ("How long was Thor: The Dark World?", {"entities": [(13, 33, "WORK_OF_ART")]}),
                ("How long was Titanic?", {"entities": [(13, 20, "WORK_OF_ART")]}),
                ("What was the runtime of The Dark Knight?", {"entities": [(24, 39, "WORK_OF_ART")]}),
                ("What was the runtime of Batman Begins?", {"entities": [(24, 37, "WORK_OF_ART")]}),
                ("What other movie was Sean Bean in?", {"entities": [(21, 30, "PERSON")]}),
                ("What other movie was Billy Boyd in?", {"entities": [(21, 31, "PERSON")]}),
                ("What is the production company of Moana?", {"entities": [(34, 39, "WORK_OF_ART")]}),
                ("What is the production company of The Lord of the Rings: The Return of the King", {"entities": [(34, 79, "WORK_OF_ART")]}),
                ("What were the production companies of Harry Potter and the Sorcerer's Stone?", {"entities": [(38, 75, "WORK_OF_ART")]}),
                ("What were the production companies of Star Wars: Episode V - The Empire Strikes Back?", {"entities": [(38, 84, "WORK_OF_ART")]}),
                ("What other movies does Michael Cera take part in?", {"entities": [(23, 35, "PERSON")]}),
                ("What other movies does Jonah Hill act in?", {"entities": [(23, 33, "PERSON")]}),
                ("What other movies did Marvel Studios produce?", {"entities": [(22, 36, "ORG")]}),
                ("What other movies did Hurwitz Creative produce?", {"entities": [(22, 38, "ORG")]}),
                ("What movies did New Line Cinema produce?", {"entities": [(16, 31, "ORG")]}),
                ("What movies did Walt Disney Animation Studios produce?", {"entities": [(16, 45, "ORG")]}),
                ("What other movies did Paramount Pictures make?", {"entities": [(22, 40, "ORG")]}),
                ("What other movies did DreamWorks Animation make?", {"entities": [(22, 42, "ORG")]}),
                ("Which production company made Star Wars: Episode I - The Phantom Menace?", {"entities": [(30, 71, "WORK_OF_ART")]}),
                ("Which production company made Ratatouille?", {"entities": [(30, 41, "WORK_OF_ART")]}),
                ("Who directed Shaun of the Dead?", {"entities": [(13, 30, "WORK_OF_ART")]}),
                ("Who directed Terminator 2: Judgment Day?", {"entities": [(13, 39, "WORK_OF_ART")]})
    ]

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        examples = []
        for text, annots in TRAIN_DATA:
            examples.append(Example.from_dict(nlp.make_doc(text), annots))

        optimizer = nlp.initialize(lambda: examples)
        for i in range(20):
            random.shuffle(examples)
            for batch in minibatch(examples, size=8):
                nlp.update(batch)
    
    return nlp