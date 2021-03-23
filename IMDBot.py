from re import split
import film as f
import person as p
import company as c
import user as u
import ner
import spellinghandler as sp
import synonyms as sy
#from chatterbot import ChatBot

#bot = ChatBot('MovieBot')
print('IMDBot: Hello There! My name is IMDBot. ', end='')
userName = u.askForName() #set username for the first time
print(f'IMDBOT: I just want to make sure I have your name right.')
userName = u.checkName(userName) #check username if correct. method can also be used if user wants to change their username
print(f'I am a bot who knows all about movies. How can I help you today?') #concatenates to "IMDBot: That's a cool name, userName! "

while True:
    try:
        user_input = input(f'{userName}: ') #collect user input for this iteration.
        entities = ner.listEntities(user_input)
        movie_name = ner.getMovieName(user_input)
        person_name = ner.getPersonName(user_input)
        company_name = ner.getOrgName(user_input)
        user_input = sp.fixSentence(user_input, entities)
        user_input = sy.getArray(user_input, entities) # User input is now an array. To look for keywords: if 'keyword' in user_input
        
        for word in user_input: # Turn all words into lowercase for easier search for keywords.
            word.lower()
        
        if ('bye' in user_input or sy.findSyns(user_input, 'goodbye') == 0): #end conversation if user says bye
            break
        #TODO: figure this one out
        elif ((sy.findSyns(user_input, 'find') == 0 or sy.findSyns(user_input, 'search') == 0) and ('another' in user_input or sy.findSyns(user_input, 'movie') == 0)): # pick the movie to talk about
            movie = f.findMovie(userName)
        elif (sy.findSyns(user_input, 'director') == 0 or sy.findSyns(user_input, 'directed') == 0): #find the director of the movie we're talking about and store as object for follow up questions about them
            if 'movie' in locals(): # check if a movie object is already saved (a movie is being spoken about)
                person = f.findDirector(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to find the director. Try to ask me to find a movie :)') # if a movie is not being currently discussed, tell user it doesn't understand 
        elif (sy.findSyns(user_input, 'summary') == 0 or sy.findSyns(user_input, 'plot') == 0):
            if 'movie' in locals():
                movie = f.giveSummary(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about. Try to ask me to find a movie :)')
        elif (sy.findSyns(user_input, 'characters') == 0):
            if 'movie' in locals():
                movie = f.showCharacters(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to list the characters. Try to ask me to find a movie first!')
        elif (sy.findSyns(user_input, 'played') == 0 or sy.findSyns(user_input, 'voiced') == 0):
            if 'movie' in locals():
                person = f.whoPlayed(movie, person_name)
            else:
                print('IMDBot: Sorry, I need to know which movie you\'re talking about first. Please ask me to look up a movie first.')
        elif (('how' and 'long') or 'runtime' in user_input or sy.findSyns(user_input, 'length') == 0):
            if 'movie' in locals():
                movie = f.runtime(movie)
            else:
                print('IMDBot: Sorry, I need to know which movie you want me to check the runtime for. Please ask me to find a movie first.')
        elif ('change' and ('name' or 'username') in user_input):
            userName = u.checkName(userName)
            print('How can I help you?') #concatenates to "IMDBot: That's a cool name, userName! "
        elif ('nevermind' in user_input):
            print(f'IMDBot: Ok. How can I help?')
        elif(('worked' and 'on') or ('role' and 'in') or ('acted' and 'in') in user_input):
            #takes in user input and calls isMember() from person.py
            if 'movie' in locals():
                print("IMDBOT: Hmm... let me check...")
                p.isMember(movie, person)
            else:
                print("IMDBOT: Sorry, I could not find anything about that.")
        #TODO: find other key words for this
        elif(('what' and 'other') in user_input):
            #takes in user input and calls otherRoles() from person.py
            if 'movie' in locals():
                print("IMDBOT: Hmm... let me think...")
                p.otherRoles(person)
            else:
                print("IMDBOT: Sorry I am not sure how to help with that.")
        elif(sy.findSyns(user_input, 'birthday') == 0):
            #Call giveBio() from person.py
            #Search for birthday/birthdate
            #"What is the birthday of {any actor name} or birthday/birth date of {any actor name}"
            #Problem with code you have to type birthday/birth date of {any actor name}(as a whole sentence) in order of it to work! Working on the fix ASAP
            person = user_input.split("of ")[1] #if user writes 'birthday/birth date of {any actor name}' cuts to '{any actor name}'
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 1)
            print("IMDBOT: What else would you like to know?")
        elif(('birth' and 'place') in user_input):
            #Search for birth place of an actor
            #Example, what is the birth place of {any actor name}
            person = user_input.split("of ")[1] #What is the birth place of {any actor name} cuts to {any actor name}
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 2)
            print("IMDBOT: What else would you like to know?")
        elif(('latest' and 'movie') in user_input):
            #Search for a latest movie by an actor
            #Example, what is the latest movie {any actor name} has worked in
            person = user_input.split("movie ")[1]
            person = person.split("has")[0]
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 3)
            print("IMDBOT: What else would you like to know?")
        # TODO: figure out how to integrate this one
        elif('check' and 'if' and 'in' in user_input):
            #Check if a {any actor name} is in {any movie name}
            # Example, check if {any actor name} is in {any movie name}
            p.checker(person_name, movie_name)
            print("IMDBOT: What else would you like to know?")
        elif('bio' in user_input):
            #Gets bio of an actor
            # bio {any actor name}
            p.giveBio(person_name, 4)
            print("IMDBOT: What else would you like to know?")
        elif ('production' in user_input and (sy.findSyns('company') == 0 or sy.findSyns('companies') == 0)):
            print("IMDBot: Okay, let me search the production companies for you!") # buffer for searching companies
            company = c.findCompany(movie) # list the production companies of the movie asked
            print('IMDBot: What else would you like to know about the company? :)')
        elif (('produced' and 'other') in user_input):
            otherMovie = c.findMovieForCompany(userName)
            if c.isProduction(company_name, otherMovie):
                print('IMDBot: Yes, this company has worked on ' + otherMovie['title'])
            else:
                print('IMDBot: No, this company did not work on ' + otherMovie['title'])
            print("IMDBOT: What else would you like to know?")
        else:
            #bot.get_response(user_input)
            print("IMDBot: I'm sorry. Something went wrong. Can you try to ask that again in another way?")

    except(KeyboardInterrupt, EOFError, SystemExit) as e: #end conversation in case of fatal error or user inputs ctrl+c
        break
print('\nIMDBot: Goodbye! It was nice talking to you ' + userName)