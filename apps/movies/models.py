class Provider:
    def __init__(self, name, tech_name, url, available_to):
        self.name = name
        self.tech_name = tech_name
        self.url = url
        self.available_to = available_to


class Price:
    def __init__(self, price, currency, last_price_change, name, tech_name, url, available_to):
        self.price = price
        self.currency = currency
        self.last_price_change = last_price_change
        self.provider = Provider(name, tech_name, url, available_to)


class Movie:
    def __init__(self, external_id, title, flatrate, buy, rent, free):
        self.external_id = external_id
        self.title = title
        self.flatrate = [Provider(**provider) for provider in flatrate]
        self.buy = [Price(**price) for price in buy]
        self.rent = [Price(**price) for price in rent]
        self.free = [Provider(**provider) for provider in free]
