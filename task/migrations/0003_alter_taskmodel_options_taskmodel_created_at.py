# Generated by Django 4.2.2 on 2023-06-14 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_tasks_taskmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 6, 14, 1, 20, 0, 189832, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]