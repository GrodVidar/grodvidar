from django.shortcuts import render
import requests
from apps.movies.forms import MoviesForm
from apps.movies.queries import query_title
from apps.movies.models import Movie
from apps.utils import get_country_code_from_request


def index(request):
    context = {}
    country_iso = ''
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        context['form'] = form
        if form.is_valid():
            providers = form.cleaned_data['providers']
            title = form.cleaned_data['title']
            country_iso = form.cleaned_data['country']
            try:
                movie_data = query_title(title, providers, country_iso)
                # print(movie_data)
                movies = [Movie(**data) for data in movie_data]
                context['movies'] = movies
            except Exception as e:
                context['error'] = e
    else:
        country_iso = request.COOKIES.get('country_iso', get_country_code_from_request(request))
        form = MoviesForm(initial={'country': country_iso})
        context['form'] = form
    response = render(request, 'movies/index.html', context)
    response.set_cookie('country_iso', country_iso)
    return response
