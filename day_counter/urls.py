from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from day_counter.views import logout, index
from day_counter.views import CounterView, CountersView, CounterCreateView, CounterDeleteView, UserUpdateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index),
    path("accounts/", include("allauth.urls")),
    path('logout/', logout),
    path('create/', CounterCreateView.as_view(), name='create_view'),
    path('counter/<str:guid>', CounterView.as_view(), name='counter_view'),
    path('counters/', CountersView.as_view(), name='counters_view'),
    path('delete/<int:pk>', CounterDeleteView.as_view(), name='delete_view'),
    path('profile/edit/<int:pk>', UserUpdateView.as_view(), name='update_user_view')
]

urlpatterns += staticfiles_urlpatterns()
