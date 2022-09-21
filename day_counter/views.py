from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate


def logout(request):
    django_logout(request)
    return render(request, 'index.html')
