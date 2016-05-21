# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_sex', models.CharField(blank=True, max_length=30, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('profile_picture_url', models.ImageField(blank=True, upload_to='profile_images')),
                ('follows', models.ManyToManyField(related_name='followed_by', to='login.UserProfile')),
            ],
        ),
    ]
