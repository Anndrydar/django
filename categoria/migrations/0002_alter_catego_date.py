# Generated by Django 4.1.5 on 2023-02-09 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catego',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 11, 32, 16, 787265)),
        ),
    ]