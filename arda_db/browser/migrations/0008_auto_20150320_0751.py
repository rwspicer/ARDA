# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0007_auto_20150320_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sbehaviour',
            options={'verbose_name': 'Behaviors'},
        ),
        migrations.AlterModelOptions(
            name='sdemo',
            options={'verbose_name': 'Demographics'},
        ),
        migrations.AlterModelOptions(
            name='sdisorder',
            options={'verbose_name': 'Disorders'},
        ),
        migrations.AlterModelOptions(
            name='sservices',
            options={'verbose_name': 'Service Features'},
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age18plus',
            field=models.BooleanField(default=False, verbose_name=b'Age 18+'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age1to3',
            field=models.BooleanField(default=False, verbose_name=b'Age 1-3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='age3to18',
            field=models.BooleanField(default=False, verbose_name=b'Age 3-18'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='gender_f',
            field=models.BooleanField(default=False, verbose_name=b'Female'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdemo',
            name='gender_m',
            field=models.BooleanField(default=False, verbose_name=b'Male'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='asd',
            field=models.BooleanField(default=False, verbose_name=b'Autism Spectrum Disorder'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='aspergers',
            field=models.BooleanField(default=False, verbose_name=b'Aspergers Syndrome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='cdd',
            field=models.BooleanField(default=False, verbose_name=b'Cognative Devlpoment Disorder'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='fas',
            field=models.BooleanField(default=False, verbose_name=b'Fetal Alchol Syndrome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='pdd',
            field=models.BooleanField(default=False, verbose_name=b'Pervasive Devlopmental Disorder'),
            preserve_default=True,
        ),
    ]
