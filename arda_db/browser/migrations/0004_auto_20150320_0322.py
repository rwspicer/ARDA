# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_auto_20150320_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROnline',
            fields=[
                ('resource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='browser.Resource')),
                ('otype', models.CharField(max_length=1, choices=[(b'0', b'video'), (b'1', b'article'), (b'2', b'web site')])),
                ('date', models.DateTimeField()),
                ('url', models.TextField(blank=True)),
            ],
            options={
            },
            bases=('browser.resource',),
        ),
        migrations.CreateModel(
            name='SServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diagnostic', models.BooleanField(default=False)),
                ('resource', models.BooleanField(default=False)),
                ('therapy', models.BooleanField(default=False)),
                ('educational', models.BooleanField(default=False)),
                ('referral', models.BooleanField(default=False)),
                ('legal', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=30)),
                ('resourceLink', models.ForeignKey(to='browser.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='SService',
        ),
    ]
