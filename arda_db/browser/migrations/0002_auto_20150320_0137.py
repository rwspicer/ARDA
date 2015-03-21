# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RLibrary',
            fields=[
                ('resource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='browser.Resource')),
                ('phys_id', models.IntegerField(null=True, blank=True)),
                ('author', models.CharField(max_length=30)),
                ('item_type', models.CharField(max_length=1, choices=[(b'0', b'book'), (b'1', b'dvd'), (b'2', b'cd')])),
                ('catagory', models.CharField(max_length=1, choices=[(b'0', b'a'), (b'1', b'b'), (b'2', b'c')])),
                ('availablity', models.CharField(max_length=1, choices=[(b'0', b'available'), (b'1', b'reserved'), (b'2', b'out')])),
            ],
            options={
            },
            bases=('browser.resource',),
        ),
        migrations.CreateModel(
            name='SDemo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age1to3', models.IntegerField(null=True, blank=True)),
                ('age3to18', models.IntegerField(null=True, blank=True)),
                ('age18plus', models.IntegerField(null=True, blank=True)),
                ('gender_m', models.IntegerField(null=True, blank=True)),
                ('gender_f', models.IntegerField(null=True, blank=True)),
                ('resource', models.ForeignKey(to='browser.Resource')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(default=b'title', max_length=30),
            preserve_default=True,
        ),
    ]
