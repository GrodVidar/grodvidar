from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from grodvidar.views import index

from grodvidar import settings

urlpatterns = [
    path('', index),
    path('accounts/', include('allauth.urls')),
    path('counters/', include('apps.day_counter.urls')),
    path('movies/', include('apps.movies.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
