import imdb
import synonyms as sy

ia = imdb.IMDb() # Initializes the IMDb integration through an IMDbPy method

def findMovie(userName): # Finds the movie requested by the user
    print('IMDBot: Which movie would you like to know about?')
    search = input(f'{userName}: ')
    movie = searchForMovie(userName, search)
    if movie == '':
        print(f'IMDBot: Ok. What else can I help you with?')
        return ''
    else: 
        title = movie['title']
        print(f'IMDBot: Ok! What do you want to know about {title}?') # confirms the movie
        return movie # returns movie object

def searchForMovie(userName, search):
    searchID = 0 #an index to go through the list to confirm the movie the user is talking about
    print('IMDBot: Ok! Let me see if I can find it...') # Serves to provide a buffer while the query is sent
    while True:
        try:
            if (searchID > 0 and searchID % 3 == 0 and askToContinue(userName) == False):
                return ''
            else:
                movie = ia.get_movie(ia.search_movie(search.lower())[searchID].movieID) # gets the movieID through a search, then creates an object for the movie from the IMDbPy classes
                title = movie['title']
                year = movie['year']
                print(f'IMDBot: I found {title} ({year}). Is this the movie you\'re asking about?')
                movieCheck = input(f'{userName}: ') 
                movieCheckFirst = movieCheck[:1].lower()
                movieCheckArr = sy.getArray(movieCheck, [])
                if (movieCheckFirst == 'y' or sy.findSyns(movieCheckArr, 'yes') == 0):
                    return movie
                elif (movieCheck == 'n' or sy.findSyns(movieCheckArr, 'no') == 0):
                    print(f'IMDBot: Hmm. Ok, let me try again...')
                    searchID += 1 #to continue through the list of movies found
                else: #if the user didn't enter an answer starting with y or n
                    print(f'IMDBot: I\'m sorry. I don\'t understand.')
        except:
            print(f'IMDBot: Uh oh. I can\'t find any movies that match {search}. Let\'s try again.')
            return findMovie(userName)

def askToContinue(userName):
    while True:
        print('IMDBot: Wait. Would you like me to keep looking?')
        check = input(f'{userName}: ')
        checkFirst = check[:1].lower()
        checkArr = sy.getArray(check, [])
        if (checkFirst == 'y' or sy.findSyns(checkArr, 'yes') == 0):
            print(f'IMDBot: Ok. Let me see...')
            return True
        elif (check == 'n' or sy.findSyns(checkArr, 'no') == 0):
            print(f'IMDBot: Ok. What else can I help you with?')
            return False
        else: #if the user didn't enter an answer starting with y or n
            print(f'IMDBot: I\'m sorry. I don\'t understand.')
    

def findDirector(movie):
    dirList = ''
    try:
        if (len(movie['directors']) == 1):
            print('IMDBot: The director of ' + movie['title'] + ' is ' + movie['directors'][0]['name']) # outputs this if the movie has only one director
            print('What would you like to know about the director?')
            return movie['directors'][0]
        else:
            c = 1
            for director in movie['directors']: #loops in order to ensure multiple directors are listed properly (Try asking for "The Matrix" directors)
                if (c < len(movie['directors'])):
                    dirList += director['name'] + ', '
                else: 
                    dirList += 'and ' + director['name']
                c += 1
            print('IMDBot: The directors of ' + movie['title'] + ' are ' + dirList)
            print('IMDBot: What would you like to know about the main director of ' + movie['title'] + '?')
            return movie['directors'][0] # returns a person object in case of follow up questions (can only return one director properly or other functions might not work)
    except:
        print(f'IMDBot: Uh oh. I can\'t find any directors.')
        print('IMDBot: What else would you like to know about ' + movie['title'] + '?')
        return 'Exception' 

def giveSummary(movie):
    try:
        title = movie['title']
        summary = movie['plot'][0]
        summary = summary.split('::')[0] # some plots have an author at the end. The format imdb provides is the summary and then ::author so this is just not including the author's name
        print(f'IMDBot: Ok, here\'s a quick summary of {title}:')
        print(f'IMDBot: {summary}')
        print(f'IMDBot: What else would you like to know about {title}?')
    except:
        print('IMDBot: Uh oh. I can\'t find a summary. What else would you like to know about' + movie['title'] + '?')
    return summary

def showCharacters(movie):
    title = movie['title']
    try:
        print(f'IMDBot: Here\'s a list of the characters in {title}:')
        castID = 0
        while (castID < len(movie['cast'])): #need to iterate through the cast's roles
            character = movie['cast'][castID].currentRole
            actor = movie['cast'][castID]
            if (str(character).find('Various') != -1) or (str(character).find('Additional') != -1): #not including any various or additional background characters in this list
                break
            else:
                print(f'\t{character} played by {actor}')
            castID += 1
    except:
        print('IMDBot: Uh oh. I can\'t find any characters.')
    print(f'IMDBot: What else would you like to know about {title}?')
    return movie['cast'][0]

def runtime(movie):
    title = movie['title']
    try:
        runtime = str(movie.data['runtimes']) #need to convert to string. Given format is ['00']
        runtime = runtime[2:-2] #Format changed to only be the digits. This is only in minutes. Would need to convert to hours:minutes
        print(f'IMDBot: The runtime for {title} is {runtime} minutes.')
    except: #Some short films don't have a runtime listed in IMDB
        print(f'IMDBot: Sorry. I can\'t find the runtime for {title} :(')
    print(f'IMDBot: What else would you like to know about {title}?')
    return runtime

# This is for checking which actor played a CHARACTER in a MOVIE
def whoPlayed(userName, oldMovie, charName, newMovie_name):
    try:
        movie = '' # Variable to hold movie id of the one to look for the character in
        if(oldMovie == ''):
            print(f'IMDBot: Before I can see who played {charName} in {newMovie_name}, I need to confirm the movie.')
            movie = searchForMovie(userName, newMovie_name)
            if (movie == ''): # will only be '' if user said to stop searching
                return 'User cancel'
        else:
            oldMovie_name = oldMovie['title']
            if (newMovie_name == '' or (newMovie_name == oldMovie_name)):
                movie = oldMovie # check using the old movie because we already have the movie ID
            else:
                print(f'IMDBot: Before I can see who played {charName} in {newMovie_name}, I need to confirm the movie')
                while True:
                    print(f'IMDBot: We were talking about {oldMovie_name}. Want me to search for {newMovie_name}?')
                    searchCheck = input(f'{userName}: ')
                    sCheckFirst = searchCheck[:1].lower() # Save first letter (might only need y or n)
                    sCheckArr = sy.getArray(searchCheck, []) # Turn user input into array for synonym checking
                    if (sCheckFirst == 'y' or sy.findSyns(sCheckArr, 'yes') == 0): # If the user does want to search for the new movie name
                        movie = searchForMovie(userName, newMovie_name)
                        if (movie == ''): # movie will only return blank if the user said to stop searching
                            return 'User cancel'
                        break
                    elif (sCheckFirst == 'n' or sy.findSyns(sCheckArr, 'no') == 0): # If the user does not want to search for the new movie name
                        print('IMDBot: Ok. I\'ll see who played {charName} in {oldMovie_name}.')
                        movie = oldMovie
                        break
                    else:
                        print(f'IMDBot: I\'m sorry, I don\'t understand. ')
                
        title = movie['title']
        print(f'IMDBot: Ok. Let me see...') #buffer while the bot searches
        castID = 0
        while (castID < len(movie['cast'])):
            character = movie['cast'][castID].currentRole #need to look through each cast member's role
            actor = movie['cast'][castID]
            if (str(character).lower().find(charName.lower()) != -1): #compares the role and the string in lowercase to compare
                print(f'IMDBot: {character} is played by {actor}')
                print(f'IMDBot: What would you like to know about {actor}?')
                return actor
            else:
                castID += 1
        print(f'IMDBot: It looks like I can\'t find {charName} in {title}.')
        print(f'IMDBot: What else would you like to know about {title}?')
        return 'Couldn\'t find the character'
    except:
        print(f'IMDBot: Uh oh. Something went wrong.')
        print(f'IMDBot: What else would you like to know about {title}?')
        return 'Error handled'