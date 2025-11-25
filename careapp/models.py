from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    medical_record_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason_for_visit = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date}"
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    prescribed_date = models.DateField()

    def __str__(self):
        return f"Prescription for {self.patient}: {self.medication_name}"
     
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Medical Record for {self.patient} on {self.record_date}"
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"
    
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"Visit of {self.patient} with {self.doctor} on {self.visit_date}"
    
class BillingRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Billing Record for {self.patient} on {self.billing_date} - Amount: {self.amount}"

class InsuranceInfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    coverage_details = models.TextField()

    def __str__(self):
        return f"Insurance Info for {self.patient} - Provider: {self.provider_name}"
    
class EmergencyContact(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Emergency Contact for {self.patient}: {self.name} ({self.relationship})"
    
class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergen = models.CharField(max_length=100)
    reaction = models.TextField()

    def __str__(self):
        return f"Allergy for {self.patient}: {self.allergen}"

class Immunization(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    immunization_date = models.DateField()

    def __str__(self):
        return f"Immunization for {self.patient}: {self.vaccine_name} on {self.immunization_date}"
    
class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.TextField()
    test_date = models.DateField()

    def __str__(self):
        return f"Lab Result for {self.patient}: {self.test_name} on {self.test_date}"
    
class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_to = models.CharField(max_length=100)
    referral_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Referral for {self.patient} to {self.referred_to} on {self.referral_date}"
    
class Surgery(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    surgery_type = models.CharField(max_length=100)
    surgery_date = models.DateField()
    surgeon = models.CharField(max_length=100)

    def __str__(self):
        return f"Surgery for {self.patient}: {self.surgery_type} on {self.surgery_date}"
    
class FollowUp(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    follow_up_date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"Follow-Up for {self.patient} on {self.follow_up_date}"
    
class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    recorded_date = models.DateField()

    def __str__(self):
        return f"Health Metric for {self.patient}: {self.metric_name} = {self.value} on {self.recorded_date}"