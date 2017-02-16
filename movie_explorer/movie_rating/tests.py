from django.test import TestCase

# Create your tests here.

from .models import MovieRatings, UserME

class Story4Cases(TestCase):

	def number_of_movies_displayed(self):
		"""
		Test to see if only 10 movies are displayed
		"""
		
