from django.shortcuts import render
import requests
from apps.movies.forms import MoviesForm
from apps.movies.models import Movie, Provider, Price
from apps.utils import get_country_code_from_request
from simplejustwatchapi import search


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
                # movie_data = query_title(title, providers, country_iso)
                media_entries = search(title, providers, country_iso, 'en', 10, True)
                movies = []
                for media_entry in media_entries:
                    matched = False
                    flatrate = []
                    rent = []
                    buy = []
                    free = []
                    for offer in media_entry.offers:
                        if convert_tech_name_to_short(offer.package.technical_name) in providers:
                            matched = True
                            provider = Provider(
                                offer.package.name,
                                offer.package.technical_name,
                                offer.url,
                                offer.available_to
                            )
                            match offer.monetization_type:
                                case 'FLATRATE':
                                    flatrate.append(provider)
                                case 'FREE':
                                    free.append(provider)
                                case 'RENT':
                                    rent.append(
                                        Price(
                                            offer.price_value,
                                            offer.price_currency,
                                            offer.last_change_retail_price_value,
                                            provider
                                        )
                                    )
                                case 'BUY':
                                    buy.append(
                                        Price(
                                            offer.price_value,
                                            offer.price_currency,
                                            offer.last_change_retail_price_value,
                                            provider
                                        )
                                    )
                        else:
                            print(media_entry.title)
                            print(media_entry.offers)
                    if matched:
                        movies.append(
                            Movie(
                                media_entry.entry_id,
                                media_entry.title,
                                media_entry.poster,
                                flatrate,
                                buy,
                                rent,
                                free
                            )
                        )
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


def convert_tech_name_to_short(technical_name):
    match technical_name:
        case 'amazonprimevideo':
            return 'prv'
        case 'netflix':
            return 'nfx'
        case 'disneyplus':
            return 'dnp'
        case 'viaplay':
            return 'vip'
        case 'max':
            return 'max'
        case 'skyshowtime':
            return 'sst'
        case 'sfanytime':
            return 'sfa'
        case 'appletvplus':
            return 'atp'
        case 'microsoft':
            return 'msf'
        case 'svtplay':
            return 'svt'
        case 'discoveryplus':
            return 'dpe'
        case 'tv4play':
            return 'tv4'
