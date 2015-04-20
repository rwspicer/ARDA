# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0023_auto_20150419_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borower',
            name='resource',
        ),
        migrations.DeleteModel(
            name='Borower',
        ),
        migrations.AlterField(
            model_name='ronline',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rservice',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sservices',
            name='city',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'State Wide'), (b'1', b'Anchorage'), (b'2', b'Fairbanks'), (b'3', b'Juno')]),
            preserve_default=True,
        ),
    ]
