# **Movie Chat Bot**
COSC 310 Assignment - Group 4

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

## Setup

1. Ensure you have the IMDbPY library installed, you can do this through pip by running

> $ pip install IMDBPy

2. In order to run the bot, use the following command from within the project main directory.

> $ python IMDBot.py


## Classes

The project has been separated into 5 classes to organize the functions. 

To see the class structure, take a look at the [UML Diagram](https://lucid.app/publicSegments/view/aebe824d-31ce-4685-9720-e142ce18f0fb/image.pdf)

### 1. IMDBot.py

 - This is the main file you run for the bot, it contains the command words and calls the functions that they reference.
 - This class inherits the other four.
 - A limitation of this class for now is that many of the commands are hard coded so errors in spelling or incorrect inputs will not be understood.
 - The class does ensure that any major exceptions are handled gracefully, and quick ctrl+c shutdown has also been implemented

### 2. user.py

- This class gets the name of the current user for use in the interface
- It also allows the user to change their name if requested

### 3. film.py

- This class handles information about a certain movie and also creates a movie object with all of it's attributes being information about the selected movie
- This class can find the director of a movie, the characters, whether someone  worked in a movie, and a summary of it

### 4. person.py

- This class handles commands related to people in the movie industry, this includes, actors, directors and other crewmembers
- this class can be used to find the projects a person has worked on as well as general biographical information on them
- it can also check if an individual has worked in a specific movie.

### 5. company.py

- This class finds production companies and whether they worked on specific movies, and can look for a certain movie in the company's repertoire.


## TODO

In future iterations, natural language processing will be implemented, as well as a GUI, and custom API implementations.
This may require a full refactor of the project, so it is very much a WIP.
