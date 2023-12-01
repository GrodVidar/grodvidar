from django import forms


class MoviesForm(forms.Form):
    NETFLIX = 'netflix'
    PRIME = 'amazonprimevideo'
    DISNEY_PLUS = 'disneyplus'
    VIAPLAY = 'viaplay'
    HBO_MAX = 'hbomax'
    SKY_SHOWTIME = 'skyshowtime'
    SF_ANYTIME = 'sfanytime'
    PROVIDER_CHOICES = (
        (NETFLIX, 'Netflix'),
        (PRIME, 'Amazon Prime Video'),
        (DISNEY_PLUS, 'Disney+'),
        (VIAPLAY, 'Viaplay'),
        (HBO_MAX, 'HBO Max'),
        (SKY_SHOWTIME, 'Sky Showtime'),
        (SF_ANYTIME, 'SF Anytime'),
    )

    provider = forms.ChoiceField(
        label='Providers',
        choices=PROVIDER_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )