from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Student

def index(request):
    return HttpResponse("Hello, world! This is the main app.")


# 🏠 List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# ➕ Add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})

# ✏️ Edit a student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student'})

# ❌ Delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def home(request):
    return render(request, 'home.html')


# View to display all students
def student_list(request):
    students = Student.objects.all()  # Ordered automatically by 'name' (Meta)
    return render(request, 'student_list.html', {'students': students})

# View to display a single student's details
def student_detail(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)
    return render(request, 'student_detail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        course = request.POST.get('course')
        marks = request.POST.get('marks', 0)  # ✅ default 0 if not provided

        Student.objects.create(
            name=name,
            roll_no=roll_no,
            course=course,
            marks=marks
        )
        return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'main/add_student.html', {'form': form})
   

