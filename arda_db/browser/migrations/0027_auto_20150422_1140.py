# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0026_auto_20150422_1032'),
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
            field=models.DateTimeField(null=True, verbose_name=b'Check Out Appointment', blank=True),
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
            field=models.DateTimeField(null=True, verbose_name=b'Return Appointment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Available'), (b'1', b'Reservered'), (b'2', b'Checked out')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sbehaviour',
            name='safety_home',
            field=models.BooleanField(default=False, verbose_name=b'Safety Home'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sbehaviour',
            name='safety_public',
            field=models.BooleanField(default=False, verbose_name=b'Safety Public'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sbehaviour',
            name='safety_travel',
            field=models.BooleanField(default=False, verbose_name=b'Safety Travel'),
            preserve_default=True,
        ),
    ]
