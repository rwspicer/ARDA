# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0008_auto_20150320_0751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rlibrary',
            options={'verbose_name': 'library item'},
        ),
        migrations.AlterModelOptions(
            name='ronline',
            options={'verbose_name': 'online item'},
        ),
        migrations.AlterModelOptions(
            name='rservice',
            options={'verbose_name': 'service'},
        ),
        migrations.RemoveField(
            model_name='rlibrary',
            name='availablity',
        ),
        migrations.RemoveField(
            model_name='rlibrary',
            name='r_type',
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='phys_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
