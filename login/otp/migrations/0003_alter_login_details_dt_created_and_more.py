# Generated by Django 4.2 on 2023-05-01 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("otp", "0002_remove_login_details_is_verified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="login_details",
            name="dt_created",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 23, 45, 41, 169797)
            ),
        ),
        migrations.AlterField(
            model_name="login_details",
            name="dt_updated",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 1, 23, 45, 41, 169797)
            ),
        ),
    ]
