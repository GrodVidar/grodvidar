from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, DateField, TimeField, BooleanField, CharField, ImageField, UUIDField
from django.db.models import ForeignKey, CASCADE
from datetime import datetime, timedelta, date
import uuid


class Counter(Model):
    name = CharField('Name', max_length=255, null=True, blank=True)
    image = ImageField(upload_to='images', null=True, blank=True)
    create_date = DateTimeField(auto_now_add=True)
    modify_date = DateTimeField(auto_now=True)
    end_date = DateField('End date', null=False)
    end_time = TimeField('End time', null=True, blank=True)
    is_date_only = BooleanField()
    days_left = DateField(null=True, blank=True)
    guid = UUIDField('Unique Id', default=uuid.uuid4)
    is_guest = BooleanField()
    user = ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
