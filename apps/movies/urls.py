from apps.movies.views import index
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'movies'

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
