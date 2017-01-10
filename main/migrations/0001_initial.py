# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 15:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('desc', models.CharField(max_length=2000, null=True)),
                ('imageUrl', models.CharField(default='images/default.jpg', max_length=256)),
                ('participation', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
