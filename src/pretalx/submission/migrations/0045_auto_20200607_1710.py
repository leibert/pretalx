# Generated by Django 3.0.5 on 2020-06-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0044_submission_editedvideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='editedVideo',
            new_name='edited_video',
        ),
    ]
