# Generated by Django 4.1.1 on 2022-09-26 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day_counter', '0012_alter_counter_guid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='is_date_only',
        ),
    ]