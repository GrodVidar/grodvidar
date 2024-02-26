from apps.users.models import User
from django.contrib.auth.forms import UserChangeForm


class UserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'enable_reminders', 'reminder_days')
