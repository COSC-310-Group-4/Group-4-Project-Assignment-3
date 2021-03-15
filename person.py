from logging import info
import imdb

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
                    print("IMDBOT:",person.title(), 'was an actor in', movie.title(), 'and played the role of', actors[target].currentRole)
                    print("IMDBOT: What else do you want to know about "+ person.title()+ "?")
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
                    print("IMDBOT:", person.title(), 'was a crew member for', movie.title(), 'and this was his role:', art[target].notes)
                    print("IMDBOT: What else do you want to know about "+ person.title()+ "?")
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
                    print("IMDBOT:", person.title(), 'was a director for', movie.title())
                    print("IMDBOT: What else do you want to know about "+ person.title()+ "?")
                else:
                    index = index + 1
    #Prints that the person is not a member of the movie's cast or crew
    else:
        print("IMDBOT:", person.title(),"did not work on", movie.title())
        print("IMDBOT: What else do you want to know about "+ person.title()+ "?")


#display other movies this person has worked in
def otherRoles(person):
    person = person['name']
    pers = ia.search_person(person.title())
    #Gets the imdb code for person
    pers_ID = pers[0].personID

    #Accesses the filmography dictionary of the person
    p = ia.get_person(pers_ID, info=['filmography'])

    #prints 5 of the person's newest movies
    print("IMDBOT:", person.title(), "is in the following 5 movies: ")
    for i in range(5):
        print("\t", p.get('filmography')['actor'][i])

#Try to use/call otherRoles in this method because it is calling for filmogrpahy to avoid redundancy 
#Get Bio of the person such as birthdate and other info
#left to add... Get the latest movie worked by an actor
def giveBio(person, x):
    pers = ia.search_person(person.title())

    #Gets the imdb code for person/movie and put into a varaible
    p = ia.get_person(pers[0].personID)

    #x==1 then it get birthday/birth date
    if(x==1):
        print("IMDBOT: The birth date of ", person.title(),"is", p['birth date'])
    # x==2 gets the birthplace of the actor
    elif(x==2):
        print("IMDBOT: The birth place of ", person.title(),"is", p['birth info']['birth place'])
    # x==3 gets latest movie the actor is working 
    elif(x==3):
        print("IMDBOT: The latest movie", person.title(), "has worked in is", p.get('filmography')['actor'][1])
    elif(x==4):
        # Bio needs to made shorter
        print(p['biography']) 
    else:
        print("Try Again")

# Using in operator in Imdb api to check if {any actor name} was in a {any movie name}
def checker(person, movie):
    pers = ia.search_person(person.title())
    mov = ia.search_movie(movie.title())

    #Gets the imdb code for person/movie and put into a varaible
    p = ia.get_person(pers[0].personID)
    m = ia.get_movie(mov[0].movieID)

    if(p in m):
        print("YES!") #Update this, Full sentences
    else:
        print("NO!") #Update this, Full sentences


