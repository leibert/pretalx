# Generated by Django 3.0.5 on 2020-07-22 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0048_auto_20200722_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='currentCount',
            new_name='attendeeRSVP',
        ),
    ]