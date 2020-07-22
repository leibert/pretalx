# Generated by Django 3.0.5 on 2020-07-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_auto_20190429_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='export',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='lastExport',
            field=models.DateField(blank=True, null=True),
        ),
    ]