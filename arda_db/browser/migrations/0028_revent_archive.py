# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0027_auto_20150422_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='revent',
            name='archive',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
