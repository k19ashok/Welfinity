from django.contrib import admin

# Register your models here.
from .models import PatientData,Encounter
admin.site.register(PatientData)
admin.site.register(Encounter)


