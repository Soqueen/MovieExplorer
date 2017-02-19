from django.test import TestCase
# from .models import MovieRatings, UserME
from .views import MovieView
from django.conf import settings
# Create your tests here.



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

    """
    def test_is_API_missing_error(self):

# Test to see if the appropriate error is return if the API is missing.

        new_content = MovieView.get_context_data(self)
        print(new_content)
        print(settings.TMDB_API_KEY)
    """