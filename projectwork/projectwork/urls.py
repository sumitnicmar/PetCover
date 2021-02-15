"""projectwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeview,name='home'),
    path('register/',views.registration,name='register'),
    path('login/',views.loginpage,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('logout/',views.logoutuser,name='logout'),
    path('updateform/',views.update_customerform,name='updateform'),
    path('deleteuser/<int:id>/',views.delete_user,name='deleteuser'),
    path('displayinfo/',views.displayinfo,name='displayinfo'),
    path('appointment/',views.appointmentview,name='appointment'),
    path('history/',views.display_history,name='history'),
    path('allhistory/<int:id>/',views.display_appointment,name='allhistory'),
    path('upcoming',views.upcoming_appointment,name='upcoming'),
    path('updateappointment/<int:id>/',views.update_appointment,name='updateappointment'),
    path('status/<int:id>/',views.change_status,name='statuschange'),
    path('clstatus/<int:id>/',views.close_status,name='closestatus'),

]
