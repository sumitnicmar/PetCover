# Generated by Django 3.1.3 on 2021-01-30 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=256)),
                ('location', models.CharField(choices=[('kothrud', 'Kothrud'), ('swargate', 'Swargate'), ('wakad', 'Wakad'), ('aundh', 'Aundh'), ('katraj', 'Katraj')], default='kothrud', max_length=20)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 – 10:00'), (1, '10:00 – 11:00'), (2, '11:00 – 12:00'), (3, '12:00 – 13:00'), (4, '13:00 – 14:00'), (5, '14:00 – 15:00'), (6, '15:00 – 16:00'), (7, '16:00 – 17:00'), (8, '17:00 – 18:00')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.customer')),
            ],
            options={
                'unique_together': {('doctor', 'date', 'timeslot')},
            },
        ),
    ]
