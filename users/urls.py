from django.urls import path
from .views import UserUpdateView

app_name = 'users'

urlpatterns = [
    path('profile/edit/<int:pk>', UserUpdateView.as_view(), name='update_user_view'),
]