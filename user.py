# Used to ask for user's name and to check input

import ner
import synonyms as sy
import time

def askForName(imdbotgui): #allows the user to set their username for the first time
    while True:
        imdbotgui.addToOutputBox('IMDBot:What\'s your name?')

        # take the user input from the gui -- problem is here
        # name = imdbotgui.userInput
        name = input(f'You: ')

        if name.__contains__(' '):
            return ner.getPersonName(name)
        elif name == '' or not name.isalpha(): #name can't be blank or have no letters
            print('IMDBot: I didn\'t catch that. ', end='')
            continue
        else:
            return name

    
# def checkName(name,imdbotgui): #can be used if the user wants to change their username
#     nameCorrect = False
#     while nameCorrect == False: #using nameCorrect as a flag
#         imdbotgui.addToOutputBox(f'IMDBot: Is your name {name}?')
#         nameCheck = input(f'You: ')[:1] #check the first letter of their answer. Only need a y or n
#         if (nameCheck.lower() == 'y' or sy.findSyns(nameCheck, 'yes') == 0):
#             imdbotgui.addToOutputBox(f'IMDBot: That\'s a cool name, {name}! ', end="")
#             nameCorrect = True
#         elif (nameCheck.lower() == 'n' or sy.findSyns(nameCheck, 'no') == 0):
#             imdbotgui.addToOutputBox('IMDBot: Sorry I got it wrong. ', end="")
#             name = askForName(imdbotgui)
#         else:
#             imdbotgui.addToOutputBox(f'IMDBot: I\'m sorry, I don\'t understand. ')
#     return name