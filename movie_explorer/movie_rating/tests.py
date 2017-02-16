from django.test import TestCase
# from .models import MovieRatings, UserME
from .views import MovieView
# Create your tests here.



class Story4Cases(TestCase):
    def test_is_movie_List_Empty(self):
        """
        Test to see if there are any movies that are displayed.
        If the dictionary returned was empty, then know that API failed
        """

        new_context = MovieView.get_context_data(self) # Return query of movies
        len_context = len(new_context) # Check how many movies have been returned
        moviesFound = False
        if(len_context>0): # Check if there is any movie returned
            moviesFound = True
        self.assertIs(moviesFound,True)