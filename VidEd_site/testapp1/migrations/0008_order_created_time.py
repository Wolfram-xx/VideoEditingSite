# Generated by Django 5.0.7 on 2024-08-02 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0007_urlsorders_url_iscloud'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 2, 9, 47, 48, 198660, tzinfo=datetime.timezone.utc)),
        ),
    ]