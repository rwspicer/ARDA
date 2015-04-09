# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0019_resource_show_in_browser'),
    ]

    operations = [
        migrations.CreateModel(
            name='REvent',
            fields=[
                ('resource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='browser.Resource')),
                ('date_time', models.DateTimeField()),
                ('location', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Event',
            },
            bases=('browser.resource',),
        ),
        migrations.AlterModelOptions(
            name='rlibrary',
            options={'verbose_name': 'Library Item'},
        ),
        migrations.AlterModelOptions(
            name='ronline',
            options={'verbose_name': 'Online item'},
        ),
        migrations.AlterModelOptions(
            name='rservice',
            options={'verbose_name': 'Service'},
        ),
        migrations.AlterField(
            model_name='borower',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Available'), (b'1', b'Reserved'), (b'2', b'Checked Out')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='aspergers',
            field=models.BooleanField(default=False, verbose_name=b'Asperger Syndrome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sdisorder',
            name='cdd',
            field=models.BooleanField(default=False, verbose_name=b'Cognitive Development Disorder'),
            preserve_default=True,
        ),
    ]
