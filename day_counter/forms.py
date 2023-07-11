from crispy_forms.helper import FormHelper
from .models import Counter
from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ('title', 'image', 'end_date', 'end_time')
        widgets = {
            'end_date': DateInput(),
            'end_time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CounterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
