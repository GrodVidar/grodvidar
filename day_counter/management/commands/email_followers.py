from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail, send_mass_mail
from day_counter.models import Counter
from users.models import User
from datetime import timedelta, datetime
from django.template import loader
from grodvidar.settings import DOMAIN


class Command(BaseCommand):
    help = 'Sends an email to all followers for every counter'

    def handle(self, *args, **kwargs):
        messages = ()
        for user in User.objects.filter(enable_reminders=True):
            date = (datetime.today() + timedelta(user.reminder_days)).date()
            followed_counters = Counter.objects.filter(followers=user, end_date=date)
            owned_counters = Counter.objects.filter(user=user, end_date=date)
            html_message = loader.render_to_string(
                'counter/messages/counter_reminder.html',
                {
                    'user_name': user.first_name or user.username,
                    'days_left': user.reminder_days,
                    'owned_counters': owned_counters,
                    'followed_counters': followed_counters,
                    'domain': DOMAIN,
                }
            )
            messages += (('Counter reminders', html_message, None, [user.email]),)
        send_mass_mail(messages)



