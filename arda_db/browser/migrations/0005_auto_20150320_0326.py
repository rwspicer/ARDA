# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0004_auto_20150320_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='RService',
            fields=[
                ('resource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='browser.Resource')),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('url', models.TextField(blank=True)),
            ],
            options={
            },
            bases=('browser.resource',),
        ),
        migrations.AlterField(
            model_name='ronline',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
