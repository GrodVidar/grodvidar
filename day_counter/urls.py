from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from day_counter.views import logout


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path("accounts/", include("allauth.urls")),
    path('logout/', logout),
]
