from django.core.management.base import BaseCommand
from apps.day_counter.models import Counter
from apps.users.models import User
from datetime import timedelta, datetime
from django.template import loader
from grodvidar.settings import DOMAIN
from django.core.mail import get_connection, EmailMultiAlternatives
import html2text


def send_mass_html_mail(datatuple, fail_silently=False, user=None, password=None,
                        connection=None):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently)
    messages = []
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient)
        message.attach_alternative(html, 'text/html')
        messages.append(message)
    return connection.send_messages(messages)


class Command(BaseCommand):
    help = 'Sends an email to all followers for every counter'

    def handle(self, *args, **kwargs):
        messages = ()
        for user in User.objects.filter(enable_reminders=True):
            date = (datetime.today() + timedelta(user.reminder_days)).date()
            followed_counters = Counter.objects.filter(followers=user, end_date=date)
            owned_counters = Counter.objects.filter(user=user, end_date=date)
            if followed_counters.exists() or owned_counters.exists():
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
                text_message = html2text.html2text(html_message)
                messages += (('Counter reminders', text_message, html_message, None, [user.email]),)
        send_mass_html_mail(messages)


