from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from apps.day_counter.views import (CounterCreateView, CounterDeleteView,
                                    CountersView, CounterUpdateView,
                                    CounterView, index, logout)

app_name = "counters"

urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout),
    path("create/", CounterCreateView.as_view(), name="create_view"),
    path("counter/<str:guid>", CounterView.as_view(), name="counter_view"),
    path("update/<int:pk>", CounterUpdateView.as_view(), name="update_view"),
    path("counters/", CountersView.as_view(), name="counters_view"),
    path("delete/<int:pk>", CounterDeleteView.as_view(), name="delete_view"),
]

urlpatterns += staticfiles_urlpatterns()
