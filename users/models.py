from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerField, BooleanField


class User(AbstractUser):
    enable_reminders = BooleanField(default=False)
    reminder_days = IntegerField('Days to remind before a counter ends', default=0)

    class Meta:
        db_table = 'auth_user'
