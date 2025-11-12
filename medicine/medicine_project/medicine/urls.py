# medical/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('add/', views.add_medicine, name='add_medicine'),
    
]
