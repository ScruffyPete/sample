# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Doradca',
                'verbose_name_plural': 'Doradcy',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='advisers',
            field=models.ManyToManyField(to='clients.Adviser'),
        ),
    ]
