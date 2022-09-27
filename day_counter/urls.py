from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from day_counter.views import logout
from day_counter.views import CounterView, CountersView, CounterCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path("accounts/", include("allauth.urls")),
    path('logout/', logout),
    path('create/', CounterCreateView.as_view()),
    path('counter/<str:guid>', CounterView.as_view(), name='counter_view'),
    path('counters/', CountersView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
