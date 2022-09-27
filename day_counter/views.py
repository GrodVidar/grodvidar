from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView

from .forms import CounterForm
from django.contrib import messages
from .models import Counter


def logout(request):
    django_logout(request)
    return render(request, 'base.html')


class CounterView(generic.DetailView):
    model = Counter
    template_name = 'counter/detail.html'

    def get_object(self, queryset=None):
        return Counter.objects.get(guid=self.kwargs['guid'])


class CountersView(generic.ListView):
    template_name = 'counter/counters.html'
    pk_url_kwarg = 'guid'

    def get_queryset(self):
        return Counter.objects.filter(user=self.request.user)


class CounterCreateView(CreateView):
    model = Counter
    form_class = CounterForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('counter_view', kwargs={'guid': self.object.guid})

    def form_valid(self, form):
        counter = form.save(commit=False)
        if self.request.user.is_authenticated:
            counter.user = self.request.user
            counter.is_guest = False
        else:
            counter.is_guest = True
        return super(CounterCreateView, self).form_valid(form)
