# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0022_auto_20150417_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sservices',
            name='city',
            field=models.CharField(max_length=1, choices=[(b'0', b'State Wide'), (b'1', b'Anchorage'), (b'2', b'Fairbanks'), (b'3', b'Juno')]),
            preserve_default=True,
        ),
    ]
