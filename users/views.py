from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import UserForm
from django.contrib import messages


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'account/edit_profile.html'

    def test_func(self):
        return self.get_object().pk == self.request.user.pk

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Profile updated')
        return reverse_lazy('counters_view')

    def post(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            print(form.cleaned_data['enable_reminders'])
        return super(UserUpdateView, self).post(request, args, kwargs)
