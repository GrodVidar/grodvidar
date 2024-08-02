from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.users.models import User

from .forms import UserForm


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "account/edit_profile.html"

    def test_func(self):
        return self.get_object().pk == self.request.user.pk

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Profile updated")
        return reverse_lazy("counters:counters_view")
