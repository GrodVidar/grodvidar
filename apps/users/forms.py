from django import forms
from django.contrib.auth.forms import UserChangeForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible

from apps.users.models import User


class UserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        del self.fields["password"]

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "enable_reminders",
            "reminder_days",
        )


class AllAuthSignupForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    def save(self, request, user):
        user = super(AllAuthSignupForm, self).save(request)
        return user

    def signup(self, request, user):
        pass
