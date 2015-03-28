# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0009_auto_20150321_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rlibrary',
            name='catagory',
            field=models.CharField(max_length=1, choices=[(b'0', b'Sensory Integration'), (b'1', b'DVD/Software materials'), (b'2', b'Resources for Professionals & Parents'), (b'3', b'Couple Relationships'), (b'4', b'Resources for Teaching Children/School'), (b'5', b'Support for Siblings'), (b'6', b'Resources for Older Children, Teens & Adults'), (b'7', b"Nonfiction/Novels/Children's Books"), (b'8', b'Binder/Folder Resources'), (b'9', b'FASD')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='item_type',
            field=models.CharField(max_length=1, choices=[(b'0', b'Book'), (b'1', b'DVD'), (b'2', b'CD'), (b'3', b'VHS'), (b'4', b'Binder'), (b'5', b'Manual'), (b'6', b'Spiral Notebook'), (b'7', b'Package(Book, DVD, et. al.)'), (b'8', b'Cards'), (b'9', b'Book w/ CD'), (b'10', b'Activity Book'), (b'11', b'Kit'), (b'12', b'Various'), (b'13', b'Catalogue'), (b'14', b'Computer Game'), (b'15', b'Watch/Timer')]),
            preserve_default=True,
        ),
    ]
