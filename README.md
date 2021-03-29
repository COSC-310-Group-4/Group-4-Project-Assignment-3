# **Movie Chat Bot**

COSC 310 Assignment **3** - Group 4

*This repository is a copied and updated version of the original with the change history and files preserved for refactoring*

## Table of Contents
* [General Information](#general-information)
* [Language and Modules](#language-and-modules)
* [Setup](#setup)
* [Classes](#classes)
* [TODO](#todo)


## General Information

For this project, we created a responsive and interactive chatbot using Python where the chatbot takes on the role of a friend who is very knowledgeable about movies. The chatbot utilizes the IMDbPY library, but the program is designed for the future implementation of a custom API integration as well as a natural language processing library. The current library allows for the chatbot to create connections between different movie attributes and elements such as movie titles, actors, directors, etc. Ultimately, the user can discuss movies with the chatbot and expect to receive information about the movies being asked as well as certain actors, characters, crew members, and directors.

## Language and Modules

- Python 3.6
- IMDbPY Library
- nltk 3.4.4
- spaCy 3.0.5 **with** Pipelines en_core_web_sm 3.0.0
- pyspellchecker 0.6.1 


## Setup

1. In order to use this code to its full extent, ensure you have the required libraries installed, you can do this through pip and python by running

> $ pip install IMDBPy 

> $ pip install spacy

> $ pip install spacy-lookups-data

> $ python -m spacy download en_core_web_sm

> $ pip install pyspellchecker

> $ pip install nltk

We need to also download the corpus necessary for our NLP and program to run. To do this:
> Make sure to "$ pip install nltk" beforehand
> Open python shell
> ">>> import nltk"
> ">>> nltk.download()"
> A new window will open. Under the menu "CORPORA", scroll to find "wordnet", and finally press "download"
> ">>> nltk.download('punkt')"
> ">>> nltk.download('averaged_perceptron_tagger')"

2. Make sure the code will be running on the file directory. To make sure you have it running on the directory, do the following:

> go to settings or (shortcut: ctrl+, )
> type "execute in file dir"
> The first setting right underneath the searchbox should contain a checkbox that says "When executing a file in terminal, whether to use execute the file's directory, instead of the current open folder". 
> Check the box 

3. In order to run the bot, use the following command from within the project main directory.

> $ python IMDBot.py


## Classes

The project has two distinct parts that make it work:

1. The IMDb integration and the functions that allow the bot to output the requested information 
2. The classes that handle natural language processing and allow the bot to better understand the user's inputs

To see the class structure of the IMDb integration, take a look at the [UML Diagram](https://lucid.app/publicSegments/view/aebe824d-31ce-4685-9720-e142ce18f0fb/image.pdf)

### Main Class

#### IMDBot.py

 - This is the main file you run for the bot, it contains the command words and calls the functions that they reference.
 - This class inherits the other four.
 - A limitation of this class for now is that many of the commands are hard coded so errors in spelling or incorrect inputs will not be understood.
 - The class does ensure that any major exceptions are handled gracefully, and quick ctrl+c shutdown has also been implemented

### Commands and IMDbPy integration

#### user.py

- This class gets the name of the current user for use in the interface
- It also allows the user to change their name if requested

#### film.py

- This class handles information about a certain movie and also creates a movie object with all of it's attributes being information about the selected movie
- This class can find the director of a movie, the characters, whether someone  worked in a movie, and a summary of it

#### person.py

- This class handles commands related to people in the movie industry, this includes, actors, directors and other crewmembers
- this class can be used to find the projects a person has worked on as well as general biographical information on them
- it can also check if an individual has worked in a specific movie.

#### company.py

- This class finds production companies and whether they worked on specific movies, and can look for a certain movie in the company's repertoire.


### Natural Language Processing


## TODO

In future iterations, natural language processing will be implemented, as well as a GUI, and custom API implementations.
This may require a full refactor of the project, so it is very much a WIP.
