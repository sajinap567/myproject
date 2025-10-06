from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
# Create your views here.
def print_hello(request):
    return HttpResponse("hello django get started")
def about(request):

    person = {
        'name': 'sajina',
        'age' : 30,
        'place' : 'calicut'
    }
    numbers = {
        'num1': [1,2,3,4,5,6,7],
    }
    return render(request, 'about.html', numbers)
def index(request):
    return render(request, 'index.html')
def review(request):
    return render(request, 'review.html')
def doctors(request):
    dict_docs ={
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html')

def department(request):
    dict_dept = {
        'dept' : Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)