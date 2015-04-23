# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0028_revent_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revent',
            name='archive',
            field=models.BooleanField(default=False, verbose_name=b'Archive Event'),
            preserve_default=True,
        ),
    ]
