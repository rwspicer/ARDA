# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0012_auto_20150331_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(default=b'title', max_length=90),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rlibrary',
            name='item_type',
            field=models.CharField(max_length=1, choices=[(b'0', b'Book'), (b'1', b'DVD'), (b'2', b'CD'), (b'3', b'VHS'), (b'4', b'Binder'), (b'5', b'Manual'), (b'6', b'Spiral Notebook'), (b'7', b'Package(Book, DVD, et. al.)'), (b'8', b'Cards'), (b'9', b'Book w/ CD'), (b'a', b'Activity Book'), (b'b', b'Kit'), (b'c', b'Various'), (b'd', b'Catalogue'), (b'e', b'Computer Game'), (b'f', b'Watch/Timer')]),
            preserve_default=True,
        ),
    ]
