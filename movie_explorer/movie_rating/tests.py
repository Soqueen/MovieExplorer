from django.test import TestCase
# from .models import MovieRatings, UserME
from .views import MovieView
from django.conf import settings
# Create your tests here.
import tmdbsimple as tmdb


class Story4Cases(TestCase):
    def test_ST4_1_is_movie_List_Empty(self):
        """
        Test to see if there are any movies that are displayed.
        Check to see if there are 10 movies which are returned to display as per specs
        If the dictionary returned was empty, then know that API failed
        """

        new_context = MovieView.get_context_data(self) # Return query of movies
        len_context = len(new_context['results']) # Check how many movies have been returned; found in results part of dictionary
        moviesFound = False
        # print(len_context)
        if(len_context == 10): # Check if there are 10 movies returned
            moviesFound = True
        self.assertIs(moviesFound,True)


    def test_ST4_2_API_incorrect_errors(self):
        """
        Test to see if the appropriate error is return if the API is missing.
        """
        tmdb.API_KEY = '789c9ad70b777c9c124863f3ab386089' # setting an incorrect API key with the correct length
        # tmdb.API_KEY = '' # Need to implement error checking for this
        new_content = MovieView.get_context_data(self)
        if(new_content['status'] == 'failure'):
            incorrectAPI_lengthGood = True
        else:
            incorrectAPI_lengthGood = False
        tmdb.API_KEY = 'b777c9c124863f3ab386089' # setting an incorrect API key with an incorrect length
        new_content = MovieView.get_context_data(self)
        if (new_content['status'] == 'failure'):
            incorrectAPI_lengthBad = True
        else:
            incorrectAPI_lengthBad = False
        tmdb.API_KEY = ''  # setting an incorrect API key as an empty key
        new_content = MovieView.get_context_data(self)
        if (new_content['status'] == 'failure'):
            incorrectAPI_empty = True
        else:
            incorrectAPI_empty = False
        if(incorrectAPI_lengthGood and incorrectAPI_lengthBad and incorrectAPI_empty):
            errorFound = True
        else:
            errorFound = False
        self.assertIs(errorFound,True)