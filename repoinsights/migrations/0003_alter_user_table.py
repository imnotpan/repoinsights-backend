# Generated by Django 4.2.1 on 2023-06-01 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repoinsights', '0002_alter_project_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
