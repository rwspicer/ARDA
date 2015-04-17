# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0020_auto_20150409_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(default=b'', max_length=160),
            preserve_default=True,
        ),
    ]
