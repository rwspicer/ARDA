# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0029_auto_20150423_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Available'), (b'1', b'Reservered'), (b'2', b'Checked Out')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sservices',
            name='city',
            field=models.CharField(max_length=1, choices=[(b'0', b'State Wide'), (b'1', b'Anchorage'), (b'2', b'Fairbanks'), (b'3', b'Juneau')]),
            preserve_default=True,
        ),
    ]
