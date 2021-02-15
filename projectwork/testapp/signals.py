from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import Customer


def create_customer(sender,instance,created, **kwargs):
    if created:
       group = Group.objects.get(name='customer')
       instance.groups.add(group)
       Customer.objects.create(user=instance,name=instance.username)
post_save.connect(create_customer,sender=User)
