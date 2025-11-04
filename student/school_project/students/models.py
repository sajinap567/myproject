from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    # Custom method
    def full_name(self):
        """Return the full name of the student."""
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        """Check if the student is at least 18 years old."""
        from datetime import date
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age >= 18

    # Meta options
    class Meta:
        ordering = ['roll_no']          # Default ordering
        verbose_name = 'Student Record'
        verbose_name_plural = 'Students Records'
        db_table = 'student_info'       # Custom database table name

    def __str__(self):
        return f"{self.full_name()} ({self.roll_no})"

