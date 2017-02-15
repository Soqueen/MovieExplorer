import datetime
import tmdbsimple as tmdb

from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import MovieRatings, UserME


# Create your views here.
def home(request):
    return render(request, 'home.html')


class MovieView(TemplateView):
    tmdb.API_KEY = settings.TMDB_API_KEY
    template_name = 'movie.html'  # SET TEMPLATE NAME

    def get_context_data(self, **kwargs):
        movies = tmdb.Movies()
        config = tmdb.Configuration().info()

        context = {}
        context['results'] = movies.upcoming()['results']
        context['image_path'] = config['images']['base_url']+config['images']['poster_sizes'][2]

        return context


def register(request):
    """ Handle registration form """
    if request.method == 'POST':
        response = dict()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print('username:{0}', username)

        try:
            username = UserME.objects.get(username=username)
            response["status"] = 'failure'
            response["error_message"] = 'Username is already exist'
            return JsonResponse(response, safe=False)
        except UserME.DoesNotExist:
            user = UserME.objects.create(member_since=datetime.datetime.now(), first_name=first_name,
                                         last_name=last_name, email=email,
                                         username=username, password=password)
            response["status"] = 'success'
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'register.html')
