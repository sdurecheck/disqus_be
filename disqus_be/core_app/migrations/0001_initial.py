# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
