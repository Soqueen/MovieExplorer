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
from django.shortcuts import get_object_or_404
from django.http import Http404
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
    
    # Set the page to search
    context = {'page_type' : 'search_page'}
   
    """ Handle registration form """
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        search_query = request.POST['search']

        # Select the page to be requested from the API
        if request.POST.__contains__('prev_page'):
            page = request.POST.get('prev_page', '2')
            pageNumber = int(page)
            page = str(pageNumber - 1)
        elif request.POST.__contains__('next_page'):
            page = request.POST.get('next_page', '0')
            pageNumber = int(page)
            page = str(pageNumber + 1)
        else:
            page = '1'

        # Check if query is empty
        if len(search_query) == 0:
            context['status'] = 'empty'
            return render(request, 'home.html', context)

        else:
            tmdb.API_KEY = settings.TMDB_API_KEY
            
            # Query the API
            try:
                search = tmdb.Search()
                config = tmdb.Configuration().info()
                POSTER_SIZE = 2

                context['search'] = search_query

                context['status'] = 'success'
                movie_query = search.movie(page=page, query=search_query)
                context['results'] = movie_query['results']

                context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
                context['page_num'] = page

                context['last_page'] = 'false'
                if int(page) == movie_query['total_pages']:
                    context['last_page'] = 'true'

                if len(context['results']) == 0:
                    context['status'] = 'noresult'

                return render(request, 'home.html', context)

            except (requests.exceptions.HTTPError, tmdb.APIKeyError )as e:
                print ("THE API IS WRONG")
                context["status"] = 'failure'
                return render(request, 'home.html', context)
                
    else:
        return render(request, 'home.html')

# ----This is goes to the home page----
# This is function does both sort and filter together
def sort(request):
    sort_option = 'popularity.desc'
    genre_option = ''
    page = '1'
    context = {'page_type' : 'sort_and_filter'}
    tmdb.API_KEY = settings.TMDB_API_KEY

    try:
        discover = tmdb.Discover()
        config = tmdb.Configuration().info()
        POSTER_SIZE = 2

        if request.method == 'POST':
            context['status'] = 'success'
            sort_option = request.POST['sort_by']
            genre_option = request.POST['genre']

            if request.POST.__contains__('prev_page'):
                page = request.POST.get('prev_page', '2')
                pageNumber = int(page)
                page = str(pageNumber - 1)
            elif request.POST.__contains__('next_page'):
                page = request.POST.get('next_page', '0')
                pageNumber = int(page)
                page = str(pageNumber + 1)
            else:
                page = '1'

        movie_query = discover.movie(page=page, sort_by=sort_option, with_genres=genre_option, with_release_type='2|3|4|5|6')
        # For testing purposes, you can use commented query below to get result which will only return 2 pages
        # movie_query = discover.movie(page=page, sort_by=sort_option, with_genres=genre_option, vote_count_gte='6234')

        context['results'] = movie_query['results']

        context['last_page'] = 'false'
        if int(page) == movie_query['total_pages']:
            context['last_page'] = 'true'

        if len(context['results']) == 0:
            context['status'] = 'noresult'

        context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
        context['sort_selected'] = sort_option
        context['genre_selected'] = genre_option
        context['page_num'] = page
        return render(request, 'home.html', context)

    except (requests.exceptions.HTTPError, tmdb.APIKeyError)as e:
        print("THE API IS WRONG")
        context["status"] = 'failure'
        return render(request, 'home.html', context)


def description(request):
    context = {}
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        movieID = request.POST['id_movie']

        tmdb.API_KEY = settings.TMDB_API_KEY

        try:
            movies = tmdb.Movies(int(movieID))
            config = tmdb.Configuration().info()
            POSTER_SIZE = 3

            context['status'] = 'success'
            context['results'] =  movies.info()
            context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]

            context['genre'] = []
            for x in context['results']['genres']:
                context['genre'].append(x['name'])
            # context['title'] = context['results']['original_title']

            if request.user.is_authenticated:

                # ----show stars----
                try:
                    m = MovieRatings.objects.get(user=request.user, movie_id=movies.id)
                    rating = m.rating
                except:
                    rating = 0
                context['current_rating'] = str(rating)

            return render(request, 'description.html', context)

        except (requests.exceptions.HTTPError, tmdb.APIKeyError)as e:
            context = {}
            print ("THE API IS WRONG")
            context["status"] = 'failure'
            return render(request, 'description.html', context)
                
    else:
        raise Http404("No Movie Selected")


def rate(request):
    context = {}
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )
        tmdb.API_KEY = settings.TMDB_API_KEY
        movieID = request.POST['id_movie']

        try:
            movies = tmdb.Movies(int(movieID))
            config = tmdb.Configuration().info()
            POSTER_SIZE = 3

            context['status'] = 'success'
            context['results'] = movies.info()
            context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]

            rating = request.POST.get('star', 0)
            if request.user.is_authenticated:
                try:
                    m = MovieRatings.objects.get(user=request.user, movie_id=movies.id)
                    # ----Update star rating----
                    m.rating = int(rating)
                    m.save()
                except MovieRatings.DoesNotExist:
                    # ----Create star rating----
                    MovieRatings.objects.create(user=request.user, movie_id=movies.id, rating=rating)
                except:
                    context['status'] = 'databaseError'
                context['current_rating'] = str(rating)

            return render(request, 'description.html', context)

        except (requests.exceptions.HTTPError, tmdb.APIKeyError)as e:
            print("THE API IS WRONG")
            context["status"] = 'failure'
            return render(request, 'description.html', context)

    else:
        raise Http404("No Movie Selected")

def viewRatings(request):
    context = {}
    if request.method == 'POST':
        response = dict(
            errors=list(),
        )

        if request.user.is_authenticated:
            # context['status'] = 'failure'
            myratings = MovieRatings.objects.values('movie_id','rating')
            try:
                context['status'] = 'success'
                context['results'] = myratings
            except MovieRatings.DoesNotExist:
                context['status'] = 'failure'
        return render(request, 'myratings.html', context)

    else:
        raise Http404("No Movie Selected")