# Generated by Django 2.1.7 on 2019-08-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20190723_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='textjob',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
