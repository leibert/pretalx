# Generated by Django 3.0.5 on 2020-06-24 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0021_auto_20200621_1700_squashed_0026_auto_20200621_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mastadon',
            new_name='mastodon',
        ),
    ]
