# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0002_auto_20150320_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='SBehaviour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sleep', models.BooleanField(default=False)),
                ('safety_home', models.BooleanField(default=False)),
                ('safety_public', models.BooleanField(default=False)),
                ('safety_travel', models.BooleanField(default=False)),
                ('repetition', models.BooleanField(default=False)),
                ('aggression', models.BooleanField(default=False)),
                ('communication', models.BooleanField(default=False)),
                ('nonverbal', models.BooleanField(default=False)),
                ('sensory', models.BooleanField(default=False)),
                ('meltdown', models.BooleanField(default=False)),
                ('anxiety', models.BooleanField(default=False)),
                ('change', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(to='browser.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SDisorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asd', models.BooleanField(default=False)),
                ('fas', models.BooleanField(default=False)),
                ('pdd', models.BooleanField(default=False)),
                ('aspergers', models.BooleanField(default=False)),
                ('cdd', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(to='browser.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diagnostic', models.BooleanField(default=False)),
                ('resource', models.BooleanField(default=False)),
                ('therapy', models.BooleanField(default=False)),
                ('educational', models.BooleanField(default=False)),
                ('referral', models.BooleanField(default=False)),
                ('legal', models.BooleanField(default=False)),
                ('city', models.CharField(default=b'fairbanks', max_length=30, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='resource',
            name='r_type',
        ),
        migrations.AddField(
            model_name='rlibrary',
            name='r_type',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'library')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age18plus',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age1to3',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age3to18',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='gender_f',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='gender_m',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
