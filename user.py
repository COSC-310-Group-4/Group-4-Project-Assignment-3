# Used to ask for user's name and to check input

def askForName(): #allows the user to set their username for the first time
    while True:
        print('What\'s your name?')
        name = input(f'You: ')
        if name == '' or not name.isalpha(): #name can't be blank or have no letters
            print('IMDBot: I didn\'t catch that. ', end='')
            continue
        else:
            break
    return name

def checkName(name): #can be used if the user wants to change their username
    nameCorrect = False
    while nameCorrect == False: #using nameCorrect as a flag
        print(f'IMDBot: Is your name {name}?')
        nameCheck = input(f'You: ')[:1] #check the first letter of their answer. Only need a y or n
        if nameCheck == 'y' or nameCheck == 'Y':
            print(f'IMDBot: That\'s a cool name, {name}! ', end="")
            nameCorrect = True
        elif nameCheck == 'n' or nameCheck == 'N':
            print('IMDBot: Sorry I got it wrong. ', end="")
            name = askForName()
        else:
            print(f'IMDBot: I\'m sorry, I don\'t understand. ')
    return name
