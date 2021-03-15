from re import split
import film as f
import person as p
import company as c
import user as u

print('IMDBot: Hello There! My name is IMDBot. ', end='')
userName = u.askForName() #set username for the first time
print(f'IMDBOT: I just want to make sure I have your name right.')
userName = u.checkName(userName) #check username if correct. method can also be used if user wants to change their username
print(f'I am a bot who knows all about movies. How can I help you today?') #concatenates to "IMDBot: That's a cool name, userName! "

while True:
    try:
        user_input = input(f'{userName}: ') #collect user input for this iteration. Do not convert to lower here.
        if (user_input.lower().__contains__('bye')): #end conversation if user says bye
            break
        elif (user_input.lower().__contains__('a movie') or user_input.lower().__contains__('another movie')): # pick the movie to talk about
            movie = f.findMovie(userName)
        elif (user_input.lower().__contains__('director') or user_input.lower().__contains__('directed')): #find the director of the movie we're talking about and store as object for follow up questions about them
            if 'movie' in locals(): # check if a movie is being spoken about
                person = f.findDirector(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to find the director. Try to ask me to find a movie :)') # if a movie is not being currently discussed, tell user it doesn't understand 
        elif (user_input.lower().__contains__('summary') or user_input.lower().__contains__('plot')):
            if 'movie' in locals():
                movie = f.giveSummary(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about. Try to ask me to find a movie :)')
        elif (user_input.lower().__contains__('characters')):
            if 'movie' in locals():
                movie = f.showCharacters(movie)
            else:
                print('IMDBot: Sorry, I don\'t know which movie you\'re asking about to list the characters. Try to ask me to find a movie first!')
        elif (user_input.lower().__contains__('who played')):
            if 'movie' in locals():
                character = user_input.split('played ')[1] #if user writes 'who played neo in matrix' cuts to 'neo in matrix'
                character = character.split(' ')[0] #continues to cut the string. now it is 'neo'. this might be problematic because it is only looking at the first name
                person = f.whoPlayed(movie, character)
            else:
                print('IMDBot: Sorry, I need to know which movie you\'re talking about first. Please ask me to look up a movie first.')
        elif (user_input.lower().__contains__('how long') or user_input.lower().__contains__('runtime')):
            if 'movie' in locals():
                movie = f.runtime(movie)
            else:
                print('IMDBot: Sorry, I need to know which movie you want me to check the runtime for. Please ask me to find a movie first.')
        elif (user_input.lower().__contains__('change' and 'name')):
            userName = u.checkName(userName)
            print('How can I help you?') #concatenates to "IMDBot: That's a cool name, userName! "
        elif (user_input.lower().__contains__('nevermind')):
            print(f'IMDBot: Ok. How can I help?')
        elif(user_input.lower().__contains__('worked on') or user_input.lower().__contains__('role in')):
            #takes in user input and calls isMember() from person.py
            if 'movie' in locals():
                print("IMDBOT: Hmm... let me check...")
                p.isMember(movie, person)
            else:
                print("IMDBOT: Sorry, I could not find anything about that")
        elif(user_input.lower().__contains__('what other')):
            #takes in user input and calls otherRoles() from person.py
            if 'movie' in locals():
                print("IMDBOT: Hmm... let me think...")
                p.otherRoles(person)
            else:
                print("IMDBOT: Sorry i am not sure how to help with that")
        elif(user_input.lower().__contains__('birthday') or user_input.lower().__contains__('birth date')):
            #Call giveBio() from person.py
            #Search for birthday/birthdate
            #"What is the birthday of {any actor name} or birthday/birth date of {any actor name}"
            #Problem with code you have to type birthday/birth date of {any actor name}(as a whole sentence) in order of it to work! Working on the fix ASAP
            person = user_input.split("of ")[1] #if user writes 'birthday/birth date of {any actor name}' cuts to '{any actor name}'
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 1)
            print("IMDBOT: What else would you like to know?")
        elif(user_input.lower().__contains__('birth place')):
            #Search for birth place of an actor
            #Example, what is the birth place of {any actor name}
            person = user_input.split("of ")[1] #What is the birth place of {any actor name} cuts to {any actor name}
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 2)
            print("IMDBOT: What else would you like to know?")
        elif(user_input.lower().__contains__('latest movie')):
            #Search for a latest movie by an actor
            #Example, what is the latest movie {any actor name} has worked in
            person = user_input.split("movie ")[1]
            person = person.split("has")[0]
            print("IMDBOT: Hmm... let me think...")
            p.giveBio(person, 3)
            print("IMDBOT: What else would you like to know?")
        elif(user_input.lower().__contains__('check')):
            #Check if a {any actor name} is in {any movie name}
            # Example, check if {any actor name} is in {any movie name}
            person = user_input.split("if")[1]
            person = person.split('is')[0]
            movie = user_input.split("in")[1]
            p.checker(person, movie)
            print("IMDBOT: What else would you like to know?")
        elif(user_input.lower().__contains__('bio')):
            #Gets bio of an actor
            # bio {any actor name}
            person = user_input.split("bio ")[1]
            p.giveBio(person, 4)
            print("IMDBOT: What else would you like to know?")
        elif (user_input.lower().__contains__('production company') or user_input.lower().__contains__('production companies')):
            print("IMDBot: Okay, let me search the production companies for you!") # buffer for searching companies
            company = c.findCompany(movie) # list the production companies of the movie asked
            print('IMDBot: What else would you like to know about the company? :)')
        elif (user_input.lower().__contains__('produced other movie')):
            otherMovie = c.findMovieForCompany(userName)
            if c.isProduction(company,otherMovie):
                print('IMDBot: Yes, this company has worked on ' + otherMovie['title'])
            else:
                print('IMDBot: No, this company did not work on ' + otherMovie['title'])
            print("IMDBOT: What else would you like to know?")
        else:
            print('IMDBOT: Sorry, what you are saying is a bit out of my scope right now') 

    except(KeyboardInterrupt, EOFError, SystemExit): #end conversation in case of fatal error or user inputs ctrl+c
        break
print('\nIMDBot: Goodbye! It was nice talking to you ' + userName)