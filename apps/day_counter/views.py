from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CounterForm
from .models import Counter


def index(request):
    if request.user.is_authenticated:
        return redirect('counters:counters_view')

    return render(request, 'index.html')
    # else:
    #     return TemplateResponse(request, 'index.html')


def logout(request):
    django_logout(request)
    return render(request, 'index.html')


class CounterView(generic.DetailView):
    model = Counter
    template_name = 'counter/detail.html'

    def get_object(self, queryset=None):
        return Counter.objects.get(guid=self.kwargs['guid'])

    def get_context_data(self, **kwargs):
        context = super(CounterView, self).get_context_data(**kwargs)
        context['is_following'] = self.object.followers.filter(pk=self.request.user.pk).exists()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'follow' in request.POST:
            self.object.followers.add(request.user)
            messages.add_message(request, messages.SUCCESS, 'Counter followed')
        elif 'unfollow' in request.POST:
            self.object.followers.remove(request.user)
            messages.add_message(request, messages.SUCCESS, 'Counter unfollowed')
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=context)


class CountersView(LoginRequiredMixin, generic.ListView):
    template_name = 'counter/counters.html'
    permission_denied_message = 'not logged in'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super(CountersView, self).get_context_data(**kwargs)
        context['followed_counters'] = Counter.objects.filter(followers=self.request.user)
        return context

    def get_queryset(self):
        return Counter.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if 'unfollow' in request.POST:
            Counter.objects.get(pk=request.POST['unfollow']).followers.remove(self.request.user)
            messages.add_message(request, messages.SUCCESS, 'Counter unfollowed')
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=context)


class CounterCreateView(CreateView):
    model = Counter
    form_class = CounterForm
    template_name = 'counter/create.html'

    def get_success_url(self):
        return reverse('counters:counter_view', kwargs={'guid': self.object.guid})

    def form_valid(self, form):
        counter = form.save(commit=False)
        if self.request.user.is_authenticated:
            counter.user = self.request.user
            counter.is_guest = False
        else:
            counter.is_guest = True
        return super(CounterCreateView, self).form_valid(form)


class CounterUpdateView(UserPassesTestMixin, UpdateView):
    model = Counter
    form_class = CounterForm
    template_name = 'counter/update.html'

    def get_success_url(self):
        return reverse('counters:counter_view', kwargs={'guid': self.object.guid})

    def test_func(self):
        return self.get_object().user.pk == self.request.user.pk


class CounterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Counter
    success_url = reverse_lazy('counters:counters_view')

    def test_func(self):
        return self.get_object().user.pk == self.request.user.pk



