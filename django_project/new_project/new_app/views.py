from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors,Book
from .forms import ContactForm
from django.shortcuts import get_object_or_404

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




