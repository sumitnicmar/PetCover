from django.shortcuts import render,redirect
from testapp.forms import CreateUserForm,CustomerForm,AppointmentForm,UpdateAppointmentForm,UpdateUserForm
from django.shortcuts import get_object_or_404
from testapp.models import Appointment

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import authenticaton,allowed_users


from django.dispatch import receiver

from testapp.models import Customer
from django.contrib.auth.models import Group

from datetime import date

# Create your views here.
# Customer views
@authenticaton
def homeview(request):
    return render(request,'testapp/home.html')

@authenticaton
def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect ('login')
        
    return render(request,'testapp/registration.html',{'form':form})

@authenticaton
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(redirect,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'Username or password is incorrect')
    return render(request,'testapp/login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def userhome(request):
    return render(request,'testapp/userhome.html')


@login_required(login_url='login')
def appointmentview(request):
    if request.method == 'POST':
        form =  AppointmentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('userhome')
    if request.method == 'GET':
        form = AppointmentForm()
    return render (request,'testapp/appointment.html',{'form':form})


@login_required(login_url='login')
def displayinfo(request):
    current_id = request.user.id
    info = Customer.objects.get(user_id=current_id)
    return render (request,'testapp/displayinfo.html',{'info':info})

@login_required(login_url='login')
def display_history(request):
    form = Appointment.objects.filter(user_id = request.user.id).order_by('-date')
    formdoc = Appointment.objects.filter(doctor__user_id = request.user.id).order_by('-date')
    return render(request,'testapp/display_history.html',{'form':form,'formdoc':formdoc})

@login_required(login_url='login')
def display_appointment(request,id):
    form = Appointment.objects.filter(id=id)
    return render(request,'testapp/display_allhistory.html',{'form':form})

@login_required(login_url='login')
def upcoming_appointment(request):
    form = Appointment.objects.filter(user_id = request.user.id, date__gte=date.today(),status=1).order_by('date','timeslot')
    docform = Appointment.objects.filter(doctor__user_id = request.user.id, date__gte=date.today(),status=1).order_by('date','timeslot')
    return render(request,'testapp/upcoming_appointment.html',{'form':form,'docform':docform})

@login_required(login_url='login')
def update_appointment(request,id):
    update = get_object_or_404(Appointment,id=id,user_id=request.user.id)

    if request.method=='POST':
        form = UpdateAppointmentForm(request.POST,instance=update)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('upcoming')
        
    else:
         form = UpdateAppointmentForm(instance=update)
    
    return render(request,'testapp/updateappointment.html',{'form':form})

@login_required(login_url='login')
def change_status(request,id):
    status = get_object_or_404(Appointment,id=id)
    if status.status == 1:
        status.status = 3
        status.save()
    return redirect('userhome')

@login_required(login_url='login')
def close_status(request,id):
    status = get_object_or_404(Appointment,id=id)
    if status.status == 1:
        status.status = 2
        status.save()
    return redirect('userhome')

@login_required(login_url='login')
def update_customerform(request):

    update_profile_customer = get_object_or_404(Customer,user_id=request.user.id)
    update_profile_user = get_object_or_404(User,id=request.user.id)

    if request.method == 'POST':
        form1 = CustomerForm(request.POST,instance=update_profile_customer)
        form2 = UpdateUserForm(request.POST,instance=update_profile_user)
        if form1.is_valid() and form2.is_valid():
            profile1 = form1.save(commit=False)
            profile1.save()
            profile2 = form2.save(commit=False)
            profile2.save()
            return redirect ('userhome')
    else:
        form1 = CustomerForm(instance=update_profile_customer)
        form2 = UpdateUserForm(instance=update_profile_user)
    return render (request,'testapp/updatecuform.html',{'form1':form1,'form2':form2})

@login_required(login_url='login')
def delete_user(request,id):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('home')

# Doctor views




