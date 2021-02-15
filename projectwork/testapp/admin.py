from django.contrib import admin
from testapp.models import Customer,Doctor,Appointment

# Register your models here.

admin.site.register(Customer)
admin.site.register(Doctor)
admin.site.register(Appointment)
