from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from apps.movies.views import index

app_name = "movies"

urlpatterns = [
    path("", index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()
