from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm, ContactForm, PatientRegistrationForm
import random


def home(request):
    """Home page view"""
    return render(request, 'home.html')


def about(request):
    """About page view"""
    return render(request, 'about.html')


def services(request):
    """Services page view"""
    return render(request, 'services.html')


def departments(request):
    """Departments page view"""
    return render(request, 'departments.html')


def doctors_view(request):
    """Doctors page view with list of doctors from database"""
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the contact form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Here you could send an email or save to database
            # For now, just show a success message
            messages.success(request, f'Thank you {name}! Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)


def appointment(request):
    """Appointment booking page with form handling"""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Get or create patient
            first_name = form.cleaned_data['patient_first_name']
            last_name = form.cleaned_data['patient_last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            
            # Generate a unique medical record number
            mrn = f"MRN{random.randint(100000, 999999)}"
            
            # Check if patient exists or create new one
            patient, created = Patient.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                defaults={'medical_record_number': mrn}
            )
            
            # Create appointment
            appointment_obj = Appointment.objects.create(
                patient=patient,
                appointment_date=form.cleaned_data['appointment_date'],
                reason_for_visit=form.cleaned_data['reason_for_visit']
            )
            
            messages.success(
                request, 
                f'Appointment booked successfully for {patient.first_name} {patient.last_name} '
                f'on {appointment_obj.appointment_date.strftime("%B %d, %Y at %I:%M %p")}!'
            )
            return redirect('appointment')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = AppointmentForm()
    
    context = {'form': form}
    return render(request, 'appointment.html', context)


def index(request):
    """Legacy index view - redirects to home"""
    return redirect('home')


def starter(request):
    """Legacy starter page view"""
    return render(request, 'starter-page.html')
