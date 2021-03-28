from os import name
from re import search
import unittest
from unittest.mock import patch  # "unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used"
import film as f
import person as p
import company as c
import user as u
from imdb import IMDb

class TestIMDBot(unittest.TestCase):
    name = 'Sam'
    name1 = ''
    movieName = 'The Matrix'
    actorName = 'Keanu Reeves'
    def setUp(self): #This will setup few of object like movie, person or more and run it before every test case"
        self.ia = IMDb()
        self.movie = self.ia.get_movie('0133093')
        self.person = self.ia.get_person('0000206')

    def tearDown(self): #we won't required this 
        pass     

    @patch('builtins.input', return_value=name) # FROM User.py # "The patch decorator (function) temporarily replaces the target object with a different object during the test."
    def test_askForName(self, mock_input):
        self.assertEqual(u.askForName(), 'Sam')

    def test_searchForMovie(self):  # FROM FILM.py
        with patch('builtins.input', return_value = 'y') as mock_input:
            r = f.searchForMovie(name,self.movieName)
            mock_input.assert_called_once()
            self.assertEqual(r, self.movie)
    """ If this return the correct movie back (in the case The matrix) then it works.
        If not, the test will fail and it will return a expection or string but not the object"""

    
    def test_findDirector(self):  #FROM FILM.py
        result = f.findDirector(self.movie)
        result = result['name']
        self.assertEqual(result, 'Lana Wachowski') 
    
    def test_showCharacters(self):   #FROM FILM.py
        result1 = f.showCharacters(self.movie)
        result1 = result1['name']
        self.assertEqual(result1, 'Keanu Reeves')

    def test_findCompany(self):   #FROM COMPANY.py
        result2 = c.findCompany(self.movie)
        self.assertEqual(result2, 'Warner Bros.')

    def test_isMember(self):  # FROM PERSON.py
        r = p.isMember(self.movie, self.person)
        self.assertEqual(r, 'test The Matrix and Keanu Reeves')
    
    def test_giveBio(self): # From person.py
        self.assertEqual(p.giveBio(self.actorName, 1), '1964-09-02')   # test for birth date
        self.assertEqual(p.giveBio(self.actorName, 2), 'Beirut, Lebanon') # test for birth place
        with patch('builtins.print') as mock_print:
            p.giveBio(self.actorName, 3)

            mock_print.assert_called_once_with("IMDBot: The latest movie Keanu Reeves has worked in is Rain ()")   # test for the latest movie
        
        

    

if __name__ == '__main__':
    unittest.main()