from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('starter/', views.starter, name='starter'),
    path('index/', views.index, name='index'),  # Legacy redirect
]
