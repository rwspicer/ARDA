# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0011_auto_20150329_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(default=b'title', max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='author',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
