# Generated by Django 3.0.1 on 2020-01-05 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200105_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 5, 19, 30, 27, 121843)),
        ),
    ]
