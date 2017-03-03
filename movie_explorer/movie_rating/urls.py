from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.sort, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^movies/', views.MovieView.as_view(), name='movies'),
    url(r'^search/', views.search, name='search'),
    url(r'^home/', views.sort, name='home'),
]
