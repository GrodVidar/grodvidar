import requests


def get_title_offers(node_id, country):
    url = "https://apis.justwatch.com/graphql"
    query = {
        "operationName": "GetTitleOffers",
        "variables": {
            "platform": "WEB",
            "nodeId": node_id,
            "country": country,
            "language": "en",
            "filterBuy": {"monetizationTypes": ["BUY"], "bestOnly": True},
            "filterFlatrate": {
                "monetizationTypes": ["FLATRATE"],
                "bestOnly": True
            },
            "filterRent": {
                "monetizationTypes": ["RENT"],
                "bestOnly": True
            },
            "filterFree": {
                "monetizationTypes": ["ADS", "FREE"],
                "bestOnly": True
            }
        },
        "query": """query GetTitleOffers($nodeId: ID!, $country: Country!, $language: Language!, $filterFlatrate: OfferFilter!, $filterBuy: OfferFilter!, $filterRent: OfferFilter!, $filterFree: OfferFilter!, $platform: Platform! = WEB) {
            node(id: $nodeId) {
                ... on MovieOrShowOrSeasonOrEpisode {
                    offerCount(country: $country, platform: $platform)
                    flatrate: offers(
                    country: $country
                    platform: $platform
                    filter: $filterFlatrate
                    ) {
                        ...TitleOffer
                    }
                    buy: offers(country: $country, platform: $platform, filter: $filterBuy) {
                    ...TitleOffer
                    }
                    rent: offers(country: $country, platform: $platform, filter: $filterRent) {
                    ...TitleOffer
                    }
                    free: offers(country: $country, platform: $platform, filter: $filterFree) {
                        ...TitleOffer
                    }
                }
            }
        }

        fragment TitleOffer on Offer {
        monetizationType
        retailPrice(language: $language)
        retailPriceValue
        currency
        lastChangeRetailPriceValue
        type
        package {
            clearName
            technicalName
        }
        standardWebURL
        availableTo
        }
    """,
    }
    response = requests.post(url, json=query)
    return response.json()


def get_search_titles(title, country):
    url = "https://apis.justwatch.com/graphql"
    query = {
        "operationName": "GetSearchTitles",
        "variables": {
            "country": country,
            "first": 5,
            "language": "en",
            "sortRandomSeed": 0,
            "searchTitlesFilter": {
                "monetizationTypes": ["FLATRATE", "FLATRATE_AND_BUY", "BUY", "FREE", "RENT"],
                "searchQuery": title,
            },
        },
        "query": """
        query GetSearchTitles($allowSponsoredRecommendations: SponsoredRecommendationsInput, $country: Country!, $first: Int! = 5, $language: Language!, $searchTitlesFilter: TitleFilter) {
            popularTitles(
            allowSponsoredRecommendations: $allowSponsoredRecommendations
            country: $country
            filter: $searchTitlesFilter
            first: $first
            ) {
                edges {
                    ...SearchTitleGraphql
                }
            }
        }

        fragment SearchTitleGraphql on PopularTitlesEdge {
        node {
            id
            content(country: $country, language: $language) {
                title
            }
          }
        }
    """,
    }
    response = requests.post(url, json=query)
    return response.json()


def query_title(title, providers, country):
    search_titles = get_search_titles(title, country)
    if 'errors' in search_titles:
        raise Exception(search_titles['errors'][0]['message'])
    results = search_titles['data']['popularTitles']['edges']
    movies = []
    for result in results:
        movie = {
            'external_id': result['node']['id'],
            'title': result['node']['content']['title'],
            'flatrate': [],
            'buy': [],
            'rent': [],
            'free': [],
        }
        offers = get_title_offers(movie['external_id'], country)['data']['node']
        if offers['offerCount'] > 0:
            for offer in offers['flatrate']:
                if offer['package']['technicalName'] in providers:
                    flatrate = {
                        'name': offer['package']['clearName'],
                        'tech_name': offer['package']['technicalName'],
                        'url': offer['standardWebURL'],
                        'available_to': offer['availableTo'],
                    }
                    movie['flatrate'].append(flatrate)
            for offer in offers['rent']:
                if offer['package']['technicalName'] in providers:
                    rent = {
                        'price': offer['retailPriceValue'],
                        'currency': offer['currency'],
                        'last_price_change': offer['lastChangeRetailPriceValue'],
                        'name': offer['package']['clearName'],
                        'tech_name': offer['package']['technicalName'],
                        'url': offer['standardWebURL'],
                        'available_to': offer['availableTo'],
                    }
                    movie['rent'].append(rent)
            for offer in offers['buy']:
                if offer['package']['technicalName'] in providers:
                    buy = {
                        'price': offer['retailPriceValue'],
                        'currency': offer['currency'],
                        'last_price_change': offer['lastChangeRetailPriceValue'],
                        'name': offer['package']['clearName'],
                        'tech_name': offer['package']['technicalName'],
                        'url': offer['standardWebURL'],
                        'available_to': offer['availableTo'],
                    }
                    movie['buy'].append(buy)
            for offer in offers['free']:
                if offer['package']['technicalName'] in providers:
                    free = {
                        'name': offer['package']['clearName'],
                        'tech_name': offer['package']['technicalName'],
                        'url': offer['standardWebURL'],
                        'available_to': offer['availableTo'],
                    }
                    movie['free'].append(free)
            movies.append(movie)
    return movies
