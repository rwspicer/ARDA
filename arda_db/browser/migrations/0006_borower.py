# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0005_auto_20150320_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrower_name', models.CharField(max_length=50, blank=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('checkout_date', models.DateField(null=True, blank=True)),
                ('return_date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=1, choices=[(b'0', b'available'), (b'1', b'reservered'), (b'2', b'checked out')])),
                ('resource', models.ForeignKey(to='browser.RLibrary')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
