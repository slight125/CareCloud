from django.contrib import admin
from .models import (
    Patient, Appointment, Prescription, MedicalRecord, Doctor, Visit, 
    BillingRecord, InsuranceInfo, EmergencyContact, Allergy, Immunization, 
    LabResult, Referral, Surgery, FollowUp, HealthMetric
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(MedicalRecord)
admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(BillingRecord)
admin.site.register(InsuranceInfo)
admin.site.register(EmergencyContact)
admin.site.register(Allergy)
admin.site.register(Immunization)
admin.site.register(LabResult)
admin.site.register(Referral)
admin.site.register(Surgery)
admin.site.register(FollowUp)
admin.site.register(HealthMetric)
