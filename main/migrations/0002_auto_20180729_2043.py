# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 20:43
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]