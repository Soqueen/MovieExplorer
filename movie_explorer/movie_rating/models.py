from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MovieRatings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField(null=False, default=-1)
    rating = models.IntegerField(null=False, default=0)


class UserME(models.Model):
    member_since = models.DateField()
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    username = models.CharField(unique=True, max_length=20, default='')
    password = models.CharField(max_length=15, default='secret')
