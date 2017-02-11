from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import tmdbsimple as tmdb
from django.conf import settings



# Create your views here.
def index(request):
    return HttpResponse("Hello, Movie Explorer teams")

class MovieView(TemplateView):
    tmdb.API_KEY = settings.TMDB_API_KEY
    template_name =  'movie.html' # SET TEMPLATE NAME

    def get_context_data(self, **kwargs):
        movies = tmdb.Movies()
        context = {}
        context['results'] = movies.upcoming()['results']
        return context
