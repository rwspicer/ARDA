# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0015_auto_20150401_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='rlibrary',
            name='borrower_name',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='checkout_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='email',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='return_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'available'), (b'1', b'reservered'), (b'2', b'checked out')]),
            preserve_default=True,
        ),
    ]
