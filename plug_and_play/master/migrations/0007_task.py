# Generated by Django 2.1.7 on 2019-08-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_auto_20190827_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField(default=0)),
                ('jobid', models.IntegerField(default=0)),
                ('workerid', models.IntegerField(default=0)),
            ],
        ),
    ]
