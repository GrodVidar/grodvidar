class Provider:
    def __init__(self, name, tech_name, url, available_to):
        self.name = name
        self.tech_name = tech_name
        self.url = url
        self.available_to = available_to


class Price:
    def __init__(self, price, currency, last_price_change, provider):
        self.price = price
        self.currency = currency
        self.last_price_change = last_price_change
        self.provider = provider


class Movie:
    def __init__(self, external_id, title, poster, flatrate, buy, rent, free):
        self.external_id = external_id
        self.title = title
        self.poster = poster
        self.flatrate = flatrate
        self.buy = buy
        self.rent = rent
        self.free = free
