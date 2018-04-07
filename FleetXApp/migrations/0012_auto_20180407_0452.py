# Generated by Django 2.0.3 on 2018-04-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FleetXApp', '0011_auto_20180407_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_color',
        ),
        migrations.AlterField(
            model_name='files',
            name='linked_object_type',
            field=models.CharField(choices=[('VEHICLE', 'VEHICLE'), ('REMINDER', 'REMINDER'), ('ISSUE', 'ISSUE'), ('FUELENTRY', 'FUELENTRY'), ('SERVICEENTRY', 'SERVICEENTRY'), ('CONTACT', 'CONTACT')], max_length=20),
        ),
    ]