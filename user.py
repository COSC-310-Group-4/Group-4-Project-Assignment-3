# Used to ask for user's name and to check input

import ner
import synonyms as sy

def askForName(): #allows the user to set their username for the first time
    while True:
        print('What\'s your name?')
        name = input(f'You: ')
        if name.__contains__(' '):
            return ner.getPersonName(name)
        elif name == '' or not name.isalpha(): #name can't be blank or have no letters
            print('IMDBot: I didn\'t catch that. ', end='')
            continue
        else:
            return name

def checkName(name): #can be used if the user wants to change their username
    nameCorrect = False
    while nameCorrect == False: #using nameCorrect as a flag
        print(f'IMDBot: Is your name {name}?')
        nameCheck = input(f'You: ') # Receive input from user
        nameCheckFirst = nameCheck[:1].lower() # Save first letter (might only need y or n)
        nameCheckArr = sy.getArray(nameCheck, []) # Turn user input into array for synonym checking
        if (nameCheckFirst == 'y' or sy.findSyns(nameCheckArr, 'yes') == 0):
            print(f'IMDBot: That\'s a cool name, {name}! ', end="")
            nameCorrect = True
        elif (nameCheckFirst == 'n' or sy.findSyns(nameCheckArr, 'no') == 0):
            print('IMDBot: Sorry I got it wrong. ', end="")
            name = askForName()
        else:
            print(f'IMDBot: I\'m sorry, I don\'t understand. ')
    return name
