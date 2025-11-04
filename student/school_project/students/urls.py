from django.urls import path
from . import views
from .views import StudentListView
from .views import StudentCreateView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='student_add'),
]
