# Generated by Django 2.1.7 on 2019-08-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_textjob_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textjob',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
