# Generated by Django 3.2.6 on 2021-09-14 13:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210914_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 13, 5, 26, 210612, tzinfo=utc)),
        ),
    ]
