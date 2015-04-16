# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0023_auto_20150416_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='borrower_name',
            field=models.CharField(default=b'', max_length=60, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='checkout_date',
            field=models.DateTimeField(default=b'', null=True, verbose_name=b'reserved until/check out appointment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='email',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='phone',
            field=models.CharField(default=b'', max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='return_date',
            field=models.DateTimeField(default=b'', null=True, verbose_name=b'return appointment', blank=True),
            preserve_default=True,
        ),
    ]
