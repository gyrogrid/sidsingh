# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150901_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]
