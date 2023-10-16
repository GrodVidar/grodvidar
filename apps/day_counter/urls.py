from django.urls import path, include
from apps.day_counter.views import logout, index
from apps.day_counter.views import CounterView, CountersView, CounterCreateView, CounterDeleteView
from apps.day_counter.views import CounterUpdateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index),
    path("accounts/", include("allauth.urls")),
    path('logout/', logout),
    path('create/', CounterCreateView.as_view(), name='create_view'),
    path('counter/<str:guid>', CounterView.as_view(), name='counter_view'),
    path('update/<int:pk>', CounterUpdateView.as_view(), name='update_view'),
    path('counters/', CountersView.as_view(), name='counters_view'),
    path('delete/<int:pk>', CounterDeleteView.as_view(), name='delete_view'),
]

urlpatterns += staticfiles_urlpatterns()
