from django.shortcuts import render
import requests
from apps.movies.forms import MoviesForm
from apps.movies.queries import query_title
from apps.movies.models import Movie


def index(request):
    # return render(request, 'movies/index.html')
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            providers = form.cleaned_data['providers']
            title = form.cleaned_data['title']
            country = form.cleaned_data['country']
            try:
                movie_data = query_title(title, providers, country)
                movies = [Movie(**data) for data in movie_data]
                return render(request, 'movies/index.html', {'form': form, 'movies': movies})
            except Exception as e:
                return render(request, 'movies/index.html', {'form': form, 'error': e})
    else:
        form = MoviesForm(initial={'country': 'SE'})

    return render(request, 'movies/index.html', {'form': form})
