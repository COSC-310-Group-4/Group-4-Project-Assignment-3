import imdb

ia = imdb.IMDb() # Initializes the IMDb integration through an IMDbPy method

def findMovie(userName): # Finds the movie requested by the user
    movie = ""
    movieFound = False
    while movieFound == False:
        print('IMDBot: Which movie would you like to know about?')
        search = input(f'{userName}: ')
        searchID = 0 #an index to go through the list to confirm the movie the user is talking about
        print('IMDBot: Ok! Let me see if I can find it...') # Serves to provide a buffer while the query is sent
        movieNameCorrect = False
        while movieNameCorrect == False:
            try:
                movie = ia.get_movie(ia.search_movie(search.lower())[searchID].movieID) # gets the movieID through a search, then creates an object for the movie from the IMDbPy classes
                title = movie['title']
                year = movie['year']
                print(f'IMDBot: I found {title} ({year}). Is this the movie you\'re asking about?')
                movieCheck = input(f'{userName}: ')[:1].lower() #only need to know if the first letter is y or n
                if movieCheck == 'y':
                    movieNameCorrect = True
                    movieFound = True
                    break
                elif movieCheck == 'n':
                    print(f'IMDBot: Hmm. Ok, let me try again...')
                    searchID += 1 #to continue through the list of movies found
                    continue
                else: #if the user didn't enter an answer starting with y or n
                    print(f'IMDBot: I\'m sorry. I don\'t understand.')
                    continue
            except:
                print(f'IMDBot: Uh oh. I can\'t find any movies that match {search}. Let\'s try again.')
                break #starts from the beginning so the user can search for a new title
    print(f'IMDBot: Ok! What do you want to know about {title}?') # confirms the movie    
    return movie # returns movie object
    
def findDirector(movie):
    dirList = ''
    if (len(movie['directors']) == 1): 
        print('The director of ' + movie['title'] + ' is ' + movie['directors']['name']) # outputs this if the movie has only one director
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

def giveSummary(movie):
    title = movie['title']
    summary = movie['plot'][0]
    summary = summary.split('::')[0] # some plots have an author at the end. The format imdb provides is the summary and then ::author so this is just not including the author's name
    print(f'IMDBot: Ok, here\'s a quick summary of {title}:')
    print(f'IMDBot: {summary}')
    print(f'IMDBot: What else would you like to know about {title}?')
    return movie

def showCharacters(movie):
    title = movie['title']
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
    print(f'IMDBot: What else would you like to know about {title}?')
    return movie

def runtime(movie):
    title = movie['title']
    try:
        runtime = str(movie.data['runtimes']) #need to convert to string. Given format is ['00']
        runtime = runtime[2:-2] #Format changed to only be the digits. This is only in minutes. Would need to convert to hours:minutes
        print(f'IMDBot: The runtime for {title} is {runtime} minutes.')
    except: #Some short films don't have a runtime listed in IMDB
        print(f'IMDBot: Sorry. I can\'t find the runtime for {title} :(')
    print(f'IMDBot: What else would you like to know about {title}?')
    return movie

def whoPlayed(movie, charName):
    title = movie['title']
    print(f'IMDBot: Ok, let me see if I can find {charName} in {title}...') #buffer while the bot searches
    castID = 0
    while (castID < len(movie['cast'])):
        character = movie['cast'][castID].currentRole #need to look through each cast member's role
        actor = movie['cast'][castID]
        if (str(character).lower().find(charName.lower()) != -1): #compares the role and the string in lowercase to compare
            print(f'IMDBot: {character} is played by {actor}')
            break
        else:
            castID += 1
    print(f'IMDBot: What would you like to know about {actor}?')
    return actor