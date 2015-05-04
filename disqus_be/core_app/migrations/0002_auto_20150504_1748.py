# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default=datetime.datetime(2015, 5, 4, 17, 48, 48, 958094, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
