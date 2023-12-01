from apps.movies.views import index
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', index, name='index'),
]
