# Generated by Django 3.1.3 on 2021-02-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='today',
            field=models.BooleanField(default=False),
        ),
    ]
