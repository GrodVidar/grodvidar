# Generated by Django 4.1.1 on 2022-10-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_counter', '0017_counter_unique_title_for_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='is_date_only',
            field=models.BooleanField(default=False, verbose_name='is time only'),
        ),
    ]