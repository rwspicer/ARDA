# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0017_auto_20150404_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='homepage',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sbehaviour',
            name='nutrition',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
