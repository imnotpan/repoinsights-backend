# Generated by Django 4.2.1 on 2023-06-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabase', '0003_metabaseuserdata_metabase_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='metabaseuserdata',
            name='metabase_db_id',
            field=models.IntegerField(default=-1),
        ),
    ]
