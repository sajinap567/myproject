from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'phone_number',
            'date_of_birth',
            'address',
            'profile_picture',
        ]
