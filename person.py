from logging import info
import imdb
import film as f
import synonyms as sy

ia = imdb.IMDb()

#find out if a person worked on a  movie, if so, display their role.
def isMember(movie, person):
    movie = movie['title']
    person = person['name']
    #finds the correct movie in imdb's database
    movies = ia.search_movie(movie.title())
    movies_ID = ia.get_movie(movies[0].movieID)

    #finds the correct person in imdb's database
    pers = ia.search_person(person.title())
    pers_ID = ia.get_person(pers[0].personID)

    #arrays for actors, crew members, and directors of the movie
    actors = movies_ID['cast']
    art = movies_ID['art department']
    director = movies_ID['directed by']

    #Checks to see if the person is a member of the movie
    if (pers_ID in movies_ID):
        #Checks to see if the person in an actor/actress on the movie
        if (str(actors).find(person.title()) != -1):
            index = 0
            target = 0
            #iterates through everyone in the actors list in order to find the index of the correct person
            for i in actors:
                if(str(i).find(person.title()) != -1):
                    target = index
                    movieAndPerson = 'test '+ movie.title() +' and '+ person.title()
                    print("IMDBot:",person.title(), 'was an actor in', movie.title(), 'and played the role of', actors[target].currentRole)
                    print("IMDBot: What else do you want to know about "+ person.title()+ "?")
                    return movieAndPerson
                else:
                    index = index + 1
        #Checks to see if the person in a crew member (in the art department)
        elif (str(art).find(person.title()) != -1):
            index = 0
            target = 0
            #iterates though everyone in the list in order to find the correct person
            for i in art:
                if(str(i).find(person.title()) != -1):
                    target = index
                    print("IMDBot:", person.title(), 'was a crew member for', movie.title(), 'and this was his role:', art[target].notes)
                    print("IMDBot: What else do you want to know about "+ person.title()+ "?")
                    return 'Is a crew member'
                else:
                    index = index + 1
        #Checks to see if the person is a director for the movie
        elif (str(director).find(person.title()) != -1):
            index = 0
            target = 0
            #Iterates through everyone in the list in order to find the correct person
            for i in director:
                if(str(i).find(person.title()) != -1):
                    target = index
                    print("IMDBot:", person.title(), 'was a director for', movie.title())
                    print("IMDBot: What else do you want to know about "+ person.title()+ "?")
                    return 'Is a director'
                else:
                    index = index + 1
    #Prints that the person is not a member of the movie's cast or crew
    else:
        print("IMDBot:", person.title(),"did not work on", movie.title())
        print("IMDBot: What else do you want to know about "+ person.title()+ "?")
        return 'Not in movie'


#display other movies this person has worked in
def otherRoles(person):
    person = person['name']
    pers = ia.search_person(person.title())
    #Gets the imdb code for person
    pers_ID = pers[0].personID

    #Accesses the filmography dictionary of the person
    p = ia.get_person(pers_ID, info=['filmography'])

    #prints 5 of the person's newest movies
    print("IMDBot:", person.title(), "is in the following 5 movies: ")
    for i in range(5):
        print("\t", p.get('filmography')['actor'][i])
    return p.get('filmography')['actor'][0] + ' >> Actor\'s top role'

#Try to use/call otherRoles in this method because it is calling for filmogrpahy to avoid redundancy 
#Get Bio of the person such as birthdate and other info
#left to add... Get the latest movie worked by an actor
def giveBio(person, x):
    try:
        pers = ia.search_person(person.title())

        #Gets the imdb code for person/movie and put into a varaible
        p = ia.get_person(pers[0].personID)

        #x==1 then it get birthday/birth date
        if(x==1):
            birthdate = p['birth date']
            print("IMDBot: The birth date of", person.title(),"is", birthdate)
            return birthdate
        # x==2 gets the birthplace of the actor
        elif(x==2):
            birthplace = p['birth info']['birth place']
            print("IMDBot: The birth place of ", person.title(),"is", birthplace)
            return birthplace
        # x==3 gets latest movie the actor is working 
        elif(x==3):
            personName = person.title()
            latestFilm = p.get('filmography')['actor'][1]
            print(f"IMDBot: The latest movie {personName} has worked in is {latestFilm}")
        elif(x==4):
            # Bio needs to made shorter
            print(p['biography']) 
        else:
            print("Try Again")
        return p
    except:
        print("IMDBot: Sorry, I can\'t find that person. What else can I help you with?")

# Using in operator in Imdb api to check if {any actor name} was in {any movie name}
def checker(userName, person_name, oldMovie, newMovie_name):
    try:
        # Finds the person in IMDB, gets the id code for person
        pers = ia.search_person(person_name.title())
        p = ia.get_person(pers[0].personID)
        pName = p['name']

        checkMovie = '' # Variable to hold the movie id of the movie that will be checked

        if(oldMovie == ''): # If no movie was being talked about previously
            print(f'IMDBot: Before I can check if {pName} was in {newMovie_name}, I need to confirm the movie.')
            checkMovie = f.searchForMovie(userName, newMovie_name) # Search for the new movie being talked about
            if (checkMovie == ''): # checkMovie will only return blank if the user said to stop searching
                return 'User cancelled'
        else:
            oldMovie_name = oldMovie['title']
            if oldMovie_name != newMovie_name: # If the old movie and new movie names don't match
                print(f'IMDBot: Before I can check if {pName} was in {newMovie_name}, I need to confirm the movie.')
                while True:
                    print(f'IMDBot: We were talking about {oldMovie_name}. Want me to search for {newMovie_name}?')
                    searchCheck = input(userName+': ')
                    sCheckFirst = searchCheck[:1].lower() # Save first letter (might only need y or n)
                    sCheckArr = sy.getArray(searchCheck, []) # Turn user input into array for synonym checking
                    if (sCheckFirst == 'y' or sy.findSyns(sCheckArr, 'yes') == 0): # If the user does want to search for the new movie name
                        checkMovie = f.searchForMovie(userName, newMovie_name)
                        if (checkMovie == ''): # checkMovie will only return blank if the user said to stop searching
                            return 'User Cancelled'
                        break
                    elif (sCheckFirst == 'n' or sy.findSyns(sCheckArr, 'no') == 0): # If the user does not want to search for the new movie name
                        print('IMDBot: Ok. I\'ll check if {pName} was in {oldMovie_name}.')
                        checkMovie = oldMovie
                        break
                    else:
                        print(f'IMDBot: I\'m sorry, I don\'t understand. ')
            else: # if the old movie name and new movie name match
                checkMovie = oldMovie # check using the old movie because we already have the movie ID

        checkMovie_name = checkMovie['title']
        if(p in checkMovie):
            print(f'IMDBot: Yes, {pName} was in {checkMovie_name}!')
            return True
        else:
            print(f'IMDBot: No, {pName} was not in {checkMovie_name}.')
            return False
    except:
        print("IMDBot: Woops! Something went wrong. What else can I help you with?")
        return 'Error Found'
