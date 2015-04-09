# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0018_auto_20150404_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='show_in_browser',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
