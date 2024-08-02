from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from grodvidar import settings
from grodvidar.views import index

urlpatterns = [
    path("", index),
    path("accounts/", include("allauth.urls")),
    path("counters/", include("apps.day_counter.urls")),
    path("movies/", include("apps.movies.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
] + static(settings.MEDIA_URL)
