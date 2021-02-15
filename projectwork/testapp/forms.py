from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Appointment
from datetime import date
'''from datetimewidget.widgets import DateTimeWidget'''

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields = ['first_name','last_name','email']
    
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ['number','address','location']
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
    

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor','date','timeslot']
        widgets = {'date':DateInput()}
    
    def clean_date(self):
        day = self.cleaned_data['date']
        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)')
        return day

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','timeslot','doctor']
        widgets = {'date':DateInput()}

    def clean_date(self):
        day = self.cleaned_data['date']
        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)')
        return day

    def __init__(self, *args, **kwargs):
        super(UpdateAppointmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}


    

    
    



        