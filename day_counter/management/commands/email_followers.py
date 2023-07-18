from django.core.management.base import BaseCommand, CommandError
from ...models import Counter
from datetime import timedelta, datetime


class Command(BaseCommand):
    help = 'Sends an email to all followers for every counter'

    def handle(self, *args, **kwargs):
        for counter in Counter.objects.exclude(followers=None):
            day_left = datetime.today() - counter.end_date
            for follower in counter.followers.all():
                # check user settings, send email.
                pass


