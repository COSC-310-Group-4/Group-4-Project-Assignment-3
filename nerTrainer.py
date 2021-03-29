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

def trainSpacy(): # This is called in ner.py only. DO NOT call it elsewhere.
    # Load existing spacy model
    nlp = spacy.load('en_core_web_sm')

    # Training Data. Note: when adding data, the end index needs to be +1 than then length of the entity. Use nerTrainDataHelp.py for assistance
    TRAIN_DATA = [
        ("My name is Veronica", {"entities": [(11, 19, "PERSON")]}),
        ("My name is Orvin", {"entities": [(11, 16, "PERSON")]}),
        ("My name is Hal", {"entities": [(11, 14, "PERSON")]}),
        ("My name is Francisco", {"entities": [(11, 20, "PERSON")]}),
        ("My name is Joel", {"entities": [(11, 15, "PERSON")]}),
        ("Who played Neo in The Matrix?", {"entities": [(11, 14, "PERSON"), (18, 28, "WORK_OF_ART")]}),
        ("Who played Wanda Maximoff in The Avengers?", {"entities": [(11, 25, "PERSON"), (29, 41, "WORK_OF_ART")]}),
        ("Who played Wanda in WandaVision?", {"entities": [(11, 16, "PERSON"), (20, 31, "WORK_OF_ART")]}),
        ("Who played Vision in The Avengers?", {"entities": [(11, 17, "PERSON"), (21, 33, "WORK_OF_ART")]}),
        ("Who played Alice in Alice in Wonderland?", {"entities": [(11, 16, "PERSON"), (20, 40, "WORK_OF_ART")]}),
        ("Who played Pepper Potts in Iron Man?", {"entities": [(11, 23, "PERSON"), (27, 35, "WORK_OF_ART")]}),
        ("Who played Happy Hogan in Spider-Man: Homecoming?", {"entities": [(11, 22, "PERSON"), (26, 48, "WORK_OF_ART")]}),
        ("Who played Manfred in Ice Age?", {"entities": [(11, 18, "PERSON"), (22, 29, "WORK_OF_ART")]}),
        ("Who played C-3PO in Rogue One: A Star Wars Story?", {"entities": [(11, 16, "PERSON"), (20, 48, "WORK_OF_ART")]}),
        ("Who played Obi-Wan Kenobi in Star Wars: Episode I - The Phantom Menace?", {"entities": [(11, 25, "PERSON"), (29, 70, "WORK_OF_ART")]}),
        ("Who played Yoda in Star Wars: Episode II - Attack of the Clones?", {"entities": [(11, 15, "PERSON"), (19, 63, "WORK_OF_ART")]}),
        ("Who played Supreme Chancellor Palpatine in Star Wars: Episode III - Revenge of the Sith?", {"entities": [(11, 39, "PERSON"), (43, 87, "WORK_OF_ART")]}),
        ("Which character did Mark Hamill play in Star Wars: Episode IV - A New Hope?", {"entities": [(20, 31, "PERSON"), (40, 74, "WORK_OF_ART")]}),
        ("Which character did Peter Mayhew play in Star Wars: Episode V - The Empire Strikes Back?", {"entities": [(20, 32, "PERSON"), (41, 87, "WORK_OF_ART")]}),
        ("Which character did Kenny Baker play in Star Wars: Episode VI - Return of the Jedi?", {"entities": [(20, 31, "PERSON"), (40, 82, "WORK_OF_ART")]}),
        ("Which character did Lupita Nyong'o play in Star Wars: Episode VII - The Force Awakens?", {"entities": [(20, 34, "PERSON"), (43, 85, "WORK_OF_ART")]}),
        ("Who played Snoke in Star Wars: Episode VIII - The Last Jedi?", {"entities": [(11, 16, "PERSON"), (20, 59, "WORK_OF_ART")]}),
        ("Which character did Jake Gyllenhaal play in Spider-Man: Far From Home?", {"entities": [(20, 35, "PERSON"), (44, 69, "WORK_OF_ART")]}),
        ("Which character did Zendaya play in Spider-Man: Far From Home?", {"entities": [(20, 27, "PERSON"), (36, 61, "WORK_OF_ART")]}),
        ("Which character did John Rhys-Davies play in The Lord of the Rings: The Two Towers?", {"entities": [(20, 36, "PERSON"), (45, 82, "WORK_OF_ART")]}),
        ("Which character did Viggo Mortensen play in The Lord of the Rings: The Fellowship of the Ring?", {"entities": [(20, 35, "PERSON"), (44, 93, "WORK_OF_ART")]}),
        ("Which actor played Spider-Man in Spider-Man: Far from Home?", {"entities": [(19, 29, "PERSON"), (33, 58, "WORK_OF_ART")]}),
        ("Which actor played Jarvis in Iron Man 2?", {"entities": [(19, 25, "PERSON"), (29, 39, "WORK_OF_ART")]}),
        ("Which actor played Deadpool in Deadpool 2?", {"entities": [(19, 27, "PERSON"), (31, 41, "WORK_OF_ART")]}),
        ("Which actor was the voice of Lord Farquaad in Shrek?", {"entities": [(29, 42, "PERSON"), (46, 51, "WORK_OF_ART")]}),
        ("Which actor was the voice of Chef in South Park: Bigger, Longer & Uncut?", {"entities": [(29, 33, "PERSON"), (37, 71, "WORK_OF_ART")]}),                 
        ("Which character did Zendaya play in Spider-Man: Far From Home?", {"entities": [(20, 27, "PERSON"), (36, 61, "WORK_OF_ART")]}),
        ("Which character did Tom Holland play in Spider-Man: No Way Home?", {"entities": [(20, 31, "PERSON"), (40, 63, "WORK_OF_ART")]}),
        ("Which character did Samuel L. Jackson play in Spider-Man: Far From Home?", {"entities": [(20, 37, "PERSON"), (46, 71, "WORK_OF_ART")]}),
        ("Which character did Robert Downey Jr. play in Spider-Man: Homecoming?", {"entities": [(20, 37, "PERSON"), (46, 68, "WORK_OF_ART")]}),
        ("Who was Aunt May in Spider-Man: Into the Spider-Verse?", {"entities": [(8, 16, "PERSON"), (20, 53, "WORK_OF_ART")]}),
        ("Who was The Witch in Brave?", {"entities": [(8, 17, "PERSON"), (21, 26, "WORK_OF_ART")]}),
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
        ("Who directed Terminator 2: Judgment Day?", {"entities": [(13, 39, "WORK_OF_ART")]}),
        ("What is the birthday of Christopher Lloyd", {"entities": [(24, 41, "PERSON")]}),
        ("What is the birthday of Michael J. Fox", {"entities": [(24, 38, "PERSON")]}),
        ("What is the birth place of Crispin Glover", {"entities": [(27, 41, "PERSON")]}),
        ("What is the birth place of Harry Waters Jr.?", {"entities": [(27, 43, "PERSON")]}),
        ("What is the latest movie Daniel Radcliffe was in?", {"entities": [(25, 41, "PERSON")]}),
        ("What is the latest movie Rupert Grint was in?", {"entities": [(25, 37, "PERSON")]}),
        ("What is the latest movie Emma Watson acted in?", {"entities": [(25, 36, "PERSON")]}),
        ("What is the latest movie Tom Felton acted in?", {"entities": [(25, 35, "PERSON")]}),
        ("Check if John Hurt was in Harry Potter and the Sorcerer's Stone", {"entities": [(9, 18, "PERSON"), (26, 63, "WORK_OF_ART")]}),
        ("Check if Julie Walters was in Harry Potter and the Deathly Hallows: Part 1", {"entities": [(9, 22, "PERSON"), (30, 74, "WORK_OF_ART")]}),
        ("Check if Bob Odenkirk was in Incredibles 2", {"entities": [(9, 21, "PERSON"), (29, 42, "WORK_OF_ART")]}),
        ("Check if Chadwick Boseman was in Avengers: End Game.", {"entities": [(9, 25, "PERSON"), (33, 51, "WORK_OF_ART")]}),
        ("Check if Benedict Cumberbatch was in Avengers: End Game", {"entities": [(9, 29, "PERSON"), (37, 55, "WORK_OF_ART")]}),
        ("Check if Anthony Mackie was in Avengers: Infinity War.", {"entities": [(9, 23, "PERSON"), (31, 53, "WORK_OF_ART")]}),
        ("Check if Richard Griffiths was in Harry Potter and the Chamber of Secrets", {"entities": [(9, 26, "PERSON"), (34, 73, "WORK_OF_ART")]}),
        ("What is Elizabeth Olsen's birthday?", {"entities": [(8, 23, "PERSON")]}),
        ("What is Henry Cavill's birthday?", {"entities": [(8, 20, "PERSON")]}),
        ("When is Anya Taylor-Joy's birthday?", {"entities": [(8, 23, "PERSON")]}),
        ("When is Alexander Skarsgard's birthday?", {"entities": [(8, 27, "PERSON")]}),
        ("Give me the bio of Leonardo DiCaprio", {"entities": [(19, 36, "PERSON")]}),
        ("Give me the bio of Joseph Gordon-Levitt", {"entities": [(19, 39, "PERSON")]}),
        ("What is the bio of Elliot Page?", {"entities": [(19, 30, "PERSON")]}),
        ("What is the bio of Michael Caine?", {"entities": [(19, 32, "PERSON")]})
    ]

    # Use the internal training API and run randomized training loop
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"] # Disable all other pipelines
    with nlp.disable_pipes(*other_pipes):  # only train NER - no other pipes
        examples = []
        for text, annots in TRAIN_DATA:
            examples.append(Example.from_dict(nlp.make_doc(text), annots)) # Turn tuples into Example objects
        nlp.initialize(lambda: examples) # Runs an optimizer
        for i in range(20): # Goes through Examples 20 times
            random.shuffle(examples) # randomized training
            for batch in minibatch(examples, size=8): # training in batches
                nlp.update(batch) # updates the nlp
    
    return nlp