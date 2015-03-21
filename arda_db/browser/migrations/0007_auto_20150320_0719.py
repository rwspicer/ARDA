# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0006_borower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borower',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'available'), (b'1', b'reservered'), (b'2', b'checked out')]),
            preserve_default=True,
        ),
    ]
