# Generated by Django 3.1.3 on 2021-02-14 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0014_auto_20210209_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]