# Generated by Django 5.0.7 on 2024-08-03 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0011_usergroup_privilege_level'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prempro', models.BooleanField(default=False)),
                ('aftereffects', models.BooleanField(default=False)),
                ('illustrator', models.BooleanField(default=False)),
                ('photoshop', models.BooleanField(default=False)),
                ('audition', models.BooleanField(default=False)),
                ('vegaspro', models.BooleanField(default=False)),
                ('cut', models.BooleanField(default=False)),
                ('subtitles', models.BooleanField(default=False)),
                ('transitions', models.BooleanField(default=False)),
                ('memes', models.BooleanField(default=False)),
                ('infograf', models.BooleanField(default=False)),
                ('effects', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]