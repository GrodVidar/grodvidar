import requests
from requests.structures import CaseInsensitiveDict
from django.conf import settings
from ipware import get_client_ip


def get_country_code_from_request(request):
    client_ip, is_routable = get_client_ip(request)
    if client_ip == '127.0.0.1':
        return "SE"
    url = f"https://api.geoapify.com/v1/ipinfo?&apiKey={settings.GEOAPIFY_API_KEY}&ip={client_ip}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    data = requests.get(url, headers=headers).json()
    country_iso = data.get('country', {}).get('iso_code', {})
    if country_iso:
        return country_iso
    else:
        return "SE"
