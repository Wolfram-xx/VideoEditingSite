# Generated by Django 5.0.7 on 2024-08-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0015_telegram_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram_code',
            name='maybe_tg_id',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
