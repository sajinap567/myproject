from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm



def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})



# List all students
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    ordering = ['roll_no']  # fallback ordering if Meta fails

# Add new student
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/add_student.html'
    success_url = reverse_lazy('student_list')  # redirect after success


