# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('ordering', models.PositiveSmallIntegerField(db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='external_ref',
            field=models.URLField(blank=True, null=True),
        ),
    ]
