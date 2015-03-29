# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0010_auto_20150328_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAdditional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parents', models.BooleanField(default=False, verbose_name=b'For Parents & Professionals')),
                ('relationships', models.BooleanField(default=False, verbose_name=b'Relationships')),
                ('teachers', models.BooleanField(default=False, verbose_name=b'For Teachers')),
                ('sibilings', models.BooleanField(default=False, verbose_name=b'For Siblings')),
                ('teens', models.BooleanField(default=False, verbose_name=b'For Teens/Young Adults')),
                ('resource', models.ForeignKey(to='browser.Resource')),
            ],
            options={
                'verbose_name': 'Additional Search optiions',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='ronline',
            name='otype',
            field=models.CharField(max_length=1, verbose_name=b'type', choices=[(b'0', b'video'), (b'1', b'article'), (b'2', b'web site')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='cdd',
            field=models.BooleanField(default=False, verbose_name=b'Cognative Develpoment Disorder'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='fas',
            field=models.BooleanField(default=False, verbose_name=b'Fetal Alcohol Syndrome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='pdd',
            field=models.BooleanField(default=False, verbose_name=b'Pervasive Developmental Disorder'),
            preserve_default=True,
        ),
    ]
