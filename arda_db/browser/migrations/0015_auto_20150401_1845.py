# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0014_auto_20150331_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sadditional',
            options={'verbose_name': 'Additional Search options', 'verbose_name_plural': 'Additional Search options'},
        ),
        migrations.AlterModelOptions(
            name='sbehaviour',
            options={'verbose_name': 'Behaviors', 'verbose_name_plural': 'Behaviors'},
        ),
        migrations.AlterModelOptions(
            name='sdemo',
            options={'verbose_name': 'Demographics', 'verbose_name_plural': 'Demographics'},
        ),
        migrations.AlterModelOptions(
            name='sdisorder',
            options={'verbose_name': 'Disorders', 'verbose_name_plural': 'Disorders'},
        ),
        migrations.AlterModelOptions(
            name='sservices',
            options={'verbose_name': 'Service Features', 'verbose_name_plural': 'Service Features'},
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(default=b'', max_length=90),
            preserve_default=True,
        ),
    ]
