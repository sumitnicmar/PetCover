from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User,related_name='doctor', null=True, on_delete=models.CASCADE)
    location_choice = (('kothrud','Kothrud'),('swargate','Swargate'),('wakad','Wakad'),('aundh','Aundh'),('katraj','Katraj'))
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    location = models.CharField(max_length=20,choices=location_choice,default='kothrud')
    number = models.BigIntegerField(null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str('{} {}'.format(self.user.first_name,self.user.last_name))

class Customer(models.Model):
    location_choice = (('kothrud','Kothrud'),('swargate','Swargate'),('wakad','Wakad'),('aundh','Aundh'),('katraj','Katraj'))
    user = models.OneToOneField(User,related_name='profile', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=256,null=True)
    location = models.CharField(max_length=20,choices=location_choice,default='kothrud')
    number = models.BigIntegerField(null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.name)

class Appointment(models.Model):
    TIMESLOT_LIST = (
        ('09:00 – 10:00','09:00 – 10:00'),
        ('10:00 – 11:00','10:00 – 11:00'),
        ('11:00 – 12:00','11:00 – 12:00'),
        ('12:00 – 13:00','12:00 – 13:00'),
        ('13:00 – 14:00','13:00 – 14:00'),
        ('14:00 – 15:00','14:00 – 15:00'),
        ('15:00 – 16:00','15:00 – 16:00'),
        ('16:00 – 17:00','16:00 – 17:00'),
        ('17:00 – 18:00','17:00 – 18:00')
    )
    STATUS_CHOICE = ((1,'Pending'),(2,'Closed'),(3,'Cancle'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    timeslot = models.CharField(max_length=20, choices=TIMESLOT_LIST)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICE,default=1)
    today = models.BooleanField(default=False)

    class Meta:
        unique_together = ['doctor','date','timeslot']

    def __str__(self):
        return str('Appointment ID-{} on date {}'.format(self.id,self.date))


    

