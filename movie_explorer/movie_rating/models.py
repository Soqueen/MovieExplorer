from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieRatings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField(null = False, default = -1)
    rating = models.IntegerField(null = False, default  = 0)

class UserME(User):
    member_since = models.DateField()
