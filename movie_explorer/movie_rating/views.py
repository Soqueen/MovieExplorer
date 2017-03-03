import datetime
import tmdbsimple as tmdb

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import MovieRatings
import requests

# For UserModelEmailBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Create your views here.
class MovieView(TemplateView):
    tmdb.API_KEY = settings.TMDB_API_KEY
    template_name = 'movie.html'  # SET TEMPLATE NAME

    def get_context_data(self, **kwargs):
        try:
            movies = tmdb.Movies()
            config = tmdb.Configuration().info()
            POSTER_SIZE = 2

            context = {}
            context['status'] = 'success'
            context['results'] = movies.top_rated(page = 1)['results'][:10]
            context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
            return context
        except (requests.exceptions.HTTPError, tmdb.APIKeyError )as e:
            context = {}
            print ("THE API IS WRONG")
            context["status"] = 'failure'
            return context

def register(request):
    """ Handle registration form """
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )
        # This field firstname and lastname are disable
        #  for first sprint and should be enable back in the second sprint.

        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pwd = request.POST['confirm_pwd']

        #   Check if the fields are not empty

        # if not first_name.strip():
        #     response['errors'].append(' Please fill in your first name.')
        # if not last_name.strip():
        #     response['errors'].append(' Please fill in your last name.')

        if not email.strip():
            response['errors'].append(' Please fill in your email address.')
        if not username.strip():
            response['errors'].append(' Please fill in your username.')
        if not password:
            response['errors'].append(' Please fill in your password.')
        if not confirm_pwd:
            response['errors'].append(' Please confirm your password.')

        # Check if both passwords are matched
        if password != confirm_pwd:
            response['errors'].append(' Passwords do not match.')

        # Check if  username is unique
        try:
            user = User.objects.get(username=username)
            response['errors'].append(' Username is already in use.')
        except User.DoesNotExist:
            pass

        # Check if Email is unique
        try:
            user = User.objects.get(email=email)
            response['errors'].append(' Email is already in use.')
        except User.DoesNotExist:
            pass

        # Check if the Email is valid format
        try:
            validate_email(email)
        except ValidationError:
            response['errors'].append(' Email is not in correct format')

        if response['errors']:
            return render(request, 'register.html', response)
        else:
            # Store the new user into the database

            # User.objects.create_user(username,
            #                          email=email,
            #                          password=password,
            #                          last_name=last_name,
            #                          first_name=first_name)

            # Once you enable firstname and lastname fields, please remove bellowed object.
            User.objects.create_user(username,
                                     email=email,
                                     password=password)
            response['success'] = 'You are successfully registered to Movie Explorer!'
            return render(request, 'register.html', response)

    else:
        return render(request, 'register.html')

class UserModelEmailBackend(ModelBackend):

    def authenticate(self, username="", password="", **kwargs):
        try:
            user = get_user_model().objects.get(email__iexact=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except get_user_model().DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None


def search(request):
    """ Handle registration form """
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        search_query = request.POST['search']

        tmdb.API_KEY = settings.TMDB_API_KEY
        try:
            search = tmdb.Search()
            config = tmdb.Configuration().info()
            POSTER_SIZE = 2

            context = {}
            context['status'] = 'success'
            context['results'] = search.movie(query=search_query)['results']
            #context['results'] = movies.top_rated(page = 1)['results'][:10]
            context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
            return render(request, 'search.html', context)

        except (requests.exceptions.HTTPError, tmdb.APIKeyError )as e:
            context = {}
            print ("THE API IS WRONG")
            context["status"] = 'failure'
            return render(request, 'search.html', context)
            
    else:
        return render(request, 'search.html')

# ----This is goes to the home page----
def sort(request):
    sort_option = 'popularity.desc'
    context = {}
    tmdb.API_KEY = settings.TMDB_API_KEY

    try:
        discover = tmdb.Discover()
        config = tmdb.Configuration().info()
        POSTER_SIZE = 2

        if request.method == 'POST':
            context['status'] = 'success'
            sort_option = request.POST['sort_by']

        context['results'] = discover.movie(page=1, sort_by=sort_option)['results']
        context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
        context['default_selected'] = sort_option
        return render(request, 'home.html', context)

    except (requests.exceptions.HTTPError, tmdb.APIKeyError)as e:
        print("THE API IS WRONG")
        context["status"] = 'failure'
        return render(request, 'home.html', context)


















