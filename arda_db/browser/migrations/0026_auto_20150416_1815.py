# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0025_auto_20150416_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='borrower_name',
            field=models.CharField(max_length=60, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='email',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
