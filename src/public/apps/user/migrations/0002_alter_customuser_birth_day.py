# Generated by Django 4.2.3 on 2023-10-17 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_day',
            field=models.DateField(auto_created=True, default=datetime.datetime(2023, 10, 17, 14, 30, 1, 581977, tzinfo=datetime.timezone.utc)),
        ),
    ]