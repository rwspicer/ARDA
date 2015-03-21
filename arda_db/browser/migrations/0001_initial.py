# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('r_id', models.AutoField(serialize=False, primary_key=True)),
                ('r_type', models.CharField(max_length=1, choices=[(b'0', b'libaray'), (b'1', b'service'), (b'2', b'online')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
