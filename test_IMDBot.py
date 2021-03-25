from os import name
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
    def setUp(self): #This will setup few of object like movie, person or more and run it before every test case"
        self.ia = IMDb()
        self.movie = self.ia.get_movie('0133093')

    def tearDown(self): #we won't required this 
        pass     

    @patch('builtins.input', return_value=name) # "The patch decorator (function) temporarily replaces the target object with a different object during the test."
    def test_askForName(self, mock_input):
        self.assertEqual(u.askForName(), 'Sam')
    
    #@patch('builtins.input', return_value=movieName)
    #def test_findMovie(self, mock_input): #The Matrix (1999)
        #self.assertEqual(f.findMovie(name), 'The Matrix (1999)')

    #@patch('f.findMovie.print')
    #@patch('f.findMovie.input', create=True)
    #def test_findMovie(self, mock_input, mock_print):
       # mock_input.side_effect = ['foo']
       # mock_print.side_effect = [None, Exception("Break the loop")]
       # with self.assertRaises(Exception):
         #   f.findMovie()
       # mock_print.assert_called_with('You need to enter a number!')
    
    def test_findDirector(self):
        result = f.findDirector(self.movie)
        result = result['name']
        self.assertEqual(result, 'Lana Wachowski') 
    
    def test_showCharacters(self):
        result = f.showCharacters(self.movie)
        result = result['name']
        self.assertEqual(result, 'Keanu Reeves')
    
    #def test_whoPlayed  - mock print
    # whole person.py - mock print because they return only string

    def test_findCompany(self):
        result = c.findCompany(self.movie)
        result = result['name']
        self.assertEqual(result, 'Warner Bros.')








if __name__ == '__main__':
    unittest.main()


