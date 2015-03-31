# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0013_auto_20150331_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='catagory',
            field=models.CharField(max_length=1, choices=[(b'0', b'Sensory Integration'), (b'1', b'DVD/Software materials'), (b'2', b'Resources for Professionals & Parents'), (b'3', b'Couple Relationships'), (b'4', b'Resources for Teaching Children/School'), (b'5', b'Support for Siblings'), (b'6', b'Resources for Older Children, Teens & Adults'), (b'a', b'Behavior'), (b'7', b"Nonfiction/Novels/Children's Books"), (b'8', b'Binder/Folder Resources'), (b'9', b'FASD')]),
            preserve_default=True,
        ),
    ]
