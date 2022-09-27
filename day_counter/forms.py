from crispy_forms.helper import FormHelper
from .models import Counter
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ['%d/%m/%Y']


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ('title', 'image', 'end_date', 'end_time')
        widgets = {
            'end_date': DateInput(format='%d/%m/%Y'),
            'end_time': TimeInput()
        }

    def __init__(self, *args, **kwargs):
        super(CounterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
