from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'full_name', 'email', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'roll_no', 'email')
