# Generated by Django 4.2.1 on 2023-05-15 04:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_userprivaterepos_userprofile_usertokens_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPrivateRepos',
            new_name='PrivateRepository',
        ),
    ]
