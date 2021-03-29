import imdb
import synonyms as sy

ia = imdb.IMDb()

def findCompany(movie): # Find the companies that produce the given movie
    # getting the movie name
    movieName = movie['title']
    try:
        # get the list of companies of the movie 
        companies = movie.data['production companies']

        if len(companies) == 0:
            print("IMDBot: There is no production company for this movie")
            return 'No Production'
        else:
            print("IMDBot: The production company is: " + companies[0]['name'])
            return companies[0]['name']

        return companies[0]['name'] # return the main company of the movie production
    except:
        print(f'IMDBot: Uh oh. Something went wrong. What else would you like to know about {movieName}?')
        return 'Exception'


def isProduction(company, movie): # Check if this company produced a certain movie
    try:
        mainMovieCompany = movie.data['production companies']
        # look for the company passed against the movie companies
        for c in mainMovieCompany:
            if c == company:
                print('IMDBot: Yes, this company worked on ' + movie['title'])
                return True
            else:
                print('IMDBot: No, this company did not work on ' + movie['title'])
                return False
    except:
        print(f'IMDBot: Uh oh. Something went wrong.')
        return 'Exception'
                
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
                movieCheck = input(f'{userName}: ')
                movieCheckFirst = movieCheck[:1].lower()
                movieCheckArr = sy.getArray(movieCheck, [])
                if (movieCheckFirst == 'y' or sy.findSyns(movieCheckArr, "yes") == 0): # If first letter is y or word is synonym of yes
                    movieNameCorrect = True
                    movieFound = True
                elif (movieCheckFirst == 'n' or sy.findSyns(movieCheckArr, "no") == 0): # If first letter is n or word is synonym of no
                    print(f'IMDBot: Hmm. Ok, let me try again...')
                    searchID += 1 #to continue through the list of movies found
                else: #if the user didn't enter an answer starting with y or n
                    print(f'IMDBot: I\'m sorry. I don\'t understand.')
            except:
                print(f'IMDBot: Uh oh. I can\'t find any movies that match {search}. Let\'s try again.')
                break #starts from the beginning so the user can search for a new title
    return movie # returns movie object
    

    

    


