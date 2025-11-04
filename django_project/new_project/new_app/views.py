from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departments,Doctors,Book
from .forms import ContactForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from .models import Profile

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



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save or send email, etc.
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Replace with your URL name
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})
def list_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Replace with your URL name
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'delete_book.html', {'book': book})
# myapp/views.py



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Profile.objects.get_or_create(user=user)
            return redirect('dashboard.html')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})





