from django import forms
from .models import Patient, Appointment, Doctor
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


class AppointmentForm(forms.Form):
    """Form for creating appointments with patient registration"""
    
    # Patient Information
    patient_first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'required': 'required'
        })
    )
    
    patient_last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'required': 'required'
        })
    )
    
    patient_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'required': 'required'
        })
    )
    
    patient_phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Phone',
            'required': 'required'
        })
    )
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'required': 'required'
        })
    )
    
    # Appointment Information
    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
            'required': 'required'
        })
    )
    
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select Doctor",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': 'required'
        })
    )
    
    reason_for_visit = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Reason for Visit',
            'required': 'required'
        })
    )
    
    medical_history = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Medical History (Optional)'
        })
    )
    
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date:
            # Make sure we're comparing timezone-aware datetimes
            now = timezone.now()
            if timezone.is_naive(appointment_date):
                appointment_date = timezone.make_aware(appointment_date)
            if appointment_date < now:
                raise ValidationError("Appointment date cannot be in the past.")
        return appointment_date
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > datetime.date.today():
            raise ValidationError("Date of birth cannot be in the future.")
        return dob


class ContactForm(forms.Form):
    """Form for contact page"""
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'required': 'required'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'required': 'required'
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
            'required': 'required'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Message',
            'required': 'required'
        })
    )


class PatientRegistrationForm(forms.ModelForm):
    """Form for patient registration using ModelForm"""
    
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'medical_record_number']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'medical_record_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Medical Record Number'
            }),
        }
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > datetime.date.today():
            raise ValidationError("Date of birth cannot be in the future.")
        return dob
