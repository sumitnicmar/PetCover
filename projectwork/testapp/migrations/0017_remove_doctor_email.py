# Generated by Django 3.1.3 on 2021-02-15 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0016_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
    ]