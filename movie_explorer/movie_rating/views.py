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


# Create your views here.
def home(request):
    return render(request, 'home.html')


class MovieView(TemplateView):
    tmdb.API_KEY = settings.TMDB_API_KEY
    template_name = 'movie.html'  # SET TEMPLATE NAME

    def get_context_data(self, **kwargs):
        movies = tmdb.Movies()
        config = tmdb.Configuration().info()
        POSTER_SIZE = 2

        context = {}
        context['results'] = movies.upcoming()['results']
        context['image_path'] = config['images']['base_url'] + config['images']['poster_sizes'][POSTER_SIZE]
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
        confirm_pwd = request.POST['confirm_pwd']

        #   Check if the fields are not empty
        if not first_name.strip() \
                or not last_name.strip() \
                or not email.strip() \
                or not username.strip() \
                or not password.strip():
            response['error'] = 'Please fill all the fields'
            return render(request, 'register.html', response)

        # Check if both passwords are matched
        if password != confirm_pwd:
            response['error'] = 'Passwords do not match'
            return render(request, 'register.html', response)

        # Check if  username is unique
        try:
            user = User.objects.get(username=username)
            response['error'] = 'Username is already in used'
            return render(request, 'register.html', response)
        except User.DoesNotExist:
            pass

        # Check if Email is unique
        try:
            user = User.objects.get(email=email)
            response['error'] = 'Email is already in used'
            return render(request, 'register.html', response)
        except User.DoesNotExist:
            pass

        #   Check if the Email is valid format
        try:
            validate_email(email)
        except ValidationError:
            response['error'] = 'Email is not in correct format'
            return render(request, 'register.html', response)

        # Store the new user into the database
        User.objects.create_user(username,
                                 email=email,
                                 password=password,
                                 last_name=last_name,
                                 first_name=first_name)
        response['success'] = 'You are successfully register to Movie Explorer!'
        return render(request, 'register.html', response)

    else:
        return render(request, 'register.html')
