"""Welfinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.urls import path,re_path


urlpatterns = [

    path('',views.home,name='home'),

    path('log',views.log,name='log'),

    path('logoff',views.logoff,name='logoff'),

    path('emr/', views.emr,name='emr'),

    path('adm/',views.adm,name='adm'),

    path('doc',views.doc,name='doc'),

    path('adm/<int:registrationID>/',views.editDoctor,name='editDoctor'),

    path('dash/<int:pid>/editPatient/',views.editPatient,name='editPatient'),

    
    path('dash/<int:pid>/addMedicalProblem/',views.addMedicalProblem,name='addMedicalProblem'),

    path('dash/<int:pid>/addPrescription/',views.addPrescription,name='addPrescription'),
   
    path('dash/<int:pid>/',views.dash,name='dash'),
    
    path('dash/<int:pid>/encounter/', views.encounter,name='encounter'),
    
    path('dash/<int:pid>/getEnc/',views.getEnc,name='getEnc'),
    
    path('dash/<int:pid>/encounter/<int:encid>/',views.encSummary,name='encSummary'),

    path('dash/<int:pid>/encounter/<int:encid>/delPrescription/<int:prescid>',views.delPrescription,name='delPrescription'),
    
    path('dash/<int:pid>/encounter/<int:encid>/savevitals/',views.savevitals,name='savevitals'),
    
    path('dash/<int:pid>/encounter/<int:encid>/savenotes/',views.savenotes,name='savenotes'),
    
    path('dash/<int:pid>/encounter/<int:encid>/savesoap/',views.savesoap,name='savesoap'),
    
    path('dash/<int:pid>/encounter/<int:encid>/saveros/',views.saveros,name='saveros'),

    path('addDoctor',views.addDoctor,name='addDoctor'),

]
