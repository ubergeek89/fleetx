# Generated by Django 2.0.3 on 2018-04-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FleetXApp', '0012_auto_20180407_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='uuid',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
