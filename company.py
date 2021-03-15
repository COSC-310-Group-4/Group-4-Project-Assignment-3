import imdb

ia = imdb.IMDb()

def findCompany(movie): # Find the companies that produce the given movie
    # getting the movie name
    movieName = movie['title']

    # get the list of companies of the movie 
    companies = movie.data['production companies']

    if len(companies) == 0:
        print("IMDBot: There is no production company for this movie")
        return
    else:
        print("IMDBot: The production company is: " + companies[0]['name'])

    return companies[0] # return the main company of the movie production


def isProduction(company, movie): # Check if this company produced a certain movie
    
    mainMovieCompany = movie.data['production companies']

    # look for the company passed against the movie companies
    for c in mainMovieCompany:
        if c == company:
            return True
        else:
            return False

def findMovieForCompany(userName):
    movie = ""
    movieFound = False
    while movieFound == False:
        print('IMDBot: Which movie do you have in mind?')
        search = input(f'{userName}: ')
        searchID = 0 #an index to go through the list to confirm the movie the user is talking about
        print('IMDBot: Ok! I\'m searching for the movie ...') # Serves to provide a buffer while the query is sent
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
    return movie # returns movie object
    

    

    


