# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0024_auto_20150416_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='checkout_date',
            field=models.DateTimeField(null=True, verbose_name=b'reserved until/check out appointment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='return_date',
            field=models.DateTimeField(null=True, verbose_name=b'return appointment', blank=True),
            preserve_default=True,
        ),
    ]
