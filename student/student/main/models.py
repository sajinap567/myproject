from django.db import models
from datetime import date
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()  # <- newly added field
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='student_pics/', blank=True, null=True)
    
    course = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




# One-to-Many: Author -> Book
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Many-to-Many: Student <-> Course

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name