# Generated by Django 2.1.7 on 2019-08-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_auto_20190827_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='aggregate',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='process',
        ),
        migrations.AddField(
            model_name='jobs',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
