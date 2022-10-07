from django.contrib import admin

# Register your models here.
from .models import ClinicalNotes, Doctors, PatientData,Encounter, Vitals, ROS, SOAP, MedicalProblems, Prescription
admin.site.register(PatientData)
admin.site.register(Encounter)
admin.site.register(Vitals)
admin.site.register(ClinicalNotes)
admin.site.register(ROS)
admin.site.register(SOAP)
admin.site.register(Doctors)
admin.site.register(Prescription)
admin.site.register(MedicalProblems)


