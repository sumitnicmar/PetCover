# Generated by Django 3.1.3 on 2021-02-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20210214_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
