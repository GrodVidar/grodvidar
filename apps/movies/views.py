from django.shortcuts import render
import requests
from apps.movies.forms import MoviesForm
from apps.movies.queries import query_title


def index(request):
    # return render(request, 'movies/index.html')
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            providers = form.cleaned_data['providers']
            title = form.cleaned_data['title']
            movies = query_title(title, providers)
            print(movies)
    else:
        form = MoviesForm()

    return render(request, 'movies/index.html', {'form': form})
