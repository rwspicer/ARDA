# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0021_auto_20150417_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='author',
            field=models.CharField(max_length=160),
            preserve_default=True,
        ),
    ]
