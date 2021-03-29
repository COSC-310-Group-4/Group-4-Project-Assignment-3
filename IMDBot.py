from re import split
import film as f
import person as p
import company as c
import user as u
import ner
import spellinghandler as sp
import synonyms as sy
import postagging as pt
from chatterbot import ChatBot

bot = ChatBot('MovieBot')
print('IMDBot: Hello There! My name is IMDBot. ', end='')
userName = u.askForName() #set username for the first time
print(f'IMDBOT: I just want to make sure I have your name right.')
userName = u.checkName(userName) #check username if correct. method can also be used if user wants to change their username
print(f'I am a bot who knows all about movies. How can I help you today?') #concatenates to "IMDBot: That's a cool name, userName! "

while True:
    try:
        raw_user_input = input(f'{userName}: ') #collect user input for this iteration.
        entities = ner.listEntities(raw_user_input)
        movie_name = ner.getMovieName(raw_user_input)
        person_name = ner.getPersonName(raw_user_input)
        company_name = ner.getOrgName(raw_user_input)
        user_input = sp.fixSentence(raw_user_input, entities)
        tagged = pt.getPosSentenceEntity(user_input,entities) # get the Part of speech of the spell checked sentence in the form of arrays containing tuples
        user_input = sy.getArray(user_input, entities) # User input is now an array. To look for keywords: if 'keyword' in user_input

        for i in range (len(user_input)):
            user_input[i] = user_input[i].lower()
        
        if ('bye' in user_input or sy.findSyns(user_input, 'goodbye') == 0): #end conversation if user says bye
            break

        elif ('nevermind' in user_input):
            print(f'IMDBot: Ok. How can I help?')

        elif ((sy.findSyns(user_input, 'find') == 0 or sy.findSyns(user_input, 'search') == 0) and ('another' in user_input or sy.findSyns(user_input, 'movie') == 0)): # pick the movie to talk about
            movie = f.findMovie(userName)

        elif (sy.findSyns(user_input, 'director') == 0 or sy.findSyns(user_input, 'directed') == 0): #find the director of the movie we're talking about and store as object for follow up questions about them
            if 'movie' in locals(): # check if a movie object is already saved (a movie is being spoken about)
                person = f.findDirector(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to find the director. Try to ask me to find a movie :)') # if a movie is not being currently discussed, tell user it doesn't understand 
        
        elif (sy.findSyns(user_input, 'character') == 0):
            if 'movie' in locals():
                movie = f.showCharacters(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to list the characters. Try to ask me to find a movie first!')
        
        elif (('who' in user_input) and ('played' in user_input) or ('voiced' in user_input)):
            if 'movie' in locals():
                person = f.whoPlayed(userName, movie, person_name, movie_name)
            else:
                person = f.whoPlayed(userName, '', person_name, movie_name)
        
        elif (sy.findSyns(user_input, 'change') == 0 and ('name' in user_input or 'username' in user_input)):
            userName = u.checkName(userName)
            print('How can I help you?') #concatenates to "IMDBot: That's a cool name, userName! "
        
        elif('what' in user_input and ('other' in user_input or 'another' in user_input)) :
            #takes in user input and calls otherRoles() from person.py
            if 'person' in locals():
                print("IMDBot: Hmm... let me think...")
                p.otherRoles(person) # Takes person object
            else:
                print("IMDBot: Sorry I am not sure how to help with that.")
        
        elif(sy.findSyns(user_input, 'birthday') == 0 or ('when' in user_input and sy.findSyns(user_input, 'born') == 0)):
            #Call giveBio() from person.py
            #Search for birthday/birthdate
            print("IMDBot: Hmm... let me think...")
            if 'person' in locals():
                p.giveBio(person['name'], 1)
            elif person_name != '':
                p.giveBio(person_name, 1)
            else:
                print("IMDBot: I\'m not sure who you\'re asking about.")
            print("IMDBot: What else would you like to know?")
        
        elif(('where' in user_input or 'place' in user_input) and ('born' in user_input or 'birth' in user_input)):
            #Search for birth place of an actor
            print("IMDBot: Hmm... let me think...")
            if 'person' in locals():
                p.giveBio(person['name'], 2)
            elif person_name != '':
                p.giveBio(person_name, 2)
            else:
                print("IMDBot: I\'m not sure who you\'re asking about.")
            print("IMDBot: What else would you like to know?")
        
        elif(sy.findSyns(user_input, 'latest') == 0 and sy.findSyns(user_input, 'movie') == 0):
            #Search for a latest movie by an actor
            print("IMDBot: Hmm... let me think...")
            if 'person' in locals():
                p.giveBio(person['name'], 3)
            elif person_name != '':
                p.giveBio(person_name, 3)
            else:
                print("IMDBot: I\'m not sure who you\'re asking about.")
            print("IMDBot: What else would you like to know?")
        
        elif('bio' in user_input or sy.findSyns(user_input, "biography") == 0):
            # Gets bio of an actor
            # bio {any actor name}
            if 'person' in locals():
                p.giveBio(person['name'], 4)
            elif person_name != '':
                p.giveBio(person_name, 4)
            else:
                print("IMDBot: I\'m not sure who you\'re asking about.")
            print("IMDBot: What else would you like to know?")
        
        elif((('check' and 'if' and 'in') in user_input) and (person_name != '') and (movie_name != '')):
            #Check if a {actor} is in {movie}
            if 'movie' in locals():
                p.checker(userName, person_name, movie, movie_name)
            else:
                p.checker(userName, person_name, '', movie_name)
            print('IMDBot: What else can I help you with?')
        
        elif (('production' and 'company') in user_input or sy.findSyns(user_input, 'companies') == 0):
            print("IMDBot: Okay, let me search the production companies for you!") # buffer for searching companies
            company = c.findCompany(movie) # list the production companies of the movie asked
            print('IMDBot: What else would you like to know about the company? :)')

        elif ('other' in user_input and sy.findSyns(user_input, 'produce')):
            otherMovie = c.findMovieForCompany(userName)
            c.isProduction(company_name, otherMovie)
            print("IMDBot: What else would you like to know?")
            
        elif ((('how' and 'long') in user_input) or ('runtime' in user_input or sy.findSyns(user_input, 'length') == 0)): # Moved to the bottom because it can get called by accident if near top
            if 'movie' in locals():
                movie = f.runtime(movie)
            else:
                print('IMDBot: Sorry, I need to know which movie you want me to check the runtime for. Please ask me to find a movie first.')
        
        elif(('worked' in user_input and 'on' in user_input) or ('role' in user_input and 'in' in user_input) or ('acted' in user_input and 'in' in user_input)): # Moved to bottom because it can get called by accident if at the top
            #takes in user input and calls isMember() from person.py
            if 'movie' in locals():
                print("IMDBot: Hmm... let me check...")
                p.isMember(movie, person) # Takes movie and person objects so they must already be defined
            else:
                print("IMDBot: Sorry, I could not find anything about that.")
                
        elif (('summary' in user_input) or ('plot' in user_input)):
            if 'movie' in locals():
                movie = f.giveSummary(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about. Try to ask me to find a movie :)')

        else:
            #print("ELSE")
            bot.get_response(raw_user_input)
            #print("IMDBot: I'm sorry. Something went wrong. Can you try to ask that again in another way?")

    except(KeyboardInterrupt, EOFError, SystemExit) as e: #end conversation in case of fatal error or user inputs ctrl+c
        break
print('\nIMDBot: Goodbye! It was nice talking to you ' + userName)