# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'date_posted', 'ordering': ['date_posted']},
        ),
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(default='New Post Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='New Post Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='New Post Title', max_length=20),
        ),
    ]
