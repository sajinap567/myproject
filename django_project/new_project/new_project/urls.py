"""
URL configuration for new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from new_app import views
from django.conf.urls.static import static
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('next/',views.print_hello),
    path('about/', views.about),
    path('index/', views.index),
    path('review/', views.review),
    path('department/', views.department),
    path('doctors/', views.doctors),
    path('contact/', views.contact_view, name='contact'),
    path('book', views.list_books, name='book-list'),
    path('books/add/', views.create_book, name='book-create'),
    path('books/<int:pk>/edit/', views.update_book, name='book-update'),
    path('books/<int:pk>/delete/', views.delete_book, name='book-delete'),
    path('', views.home_view, name='home'),  
    path('accounts/', include('accounts.urls')),  # Our custom app
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path('change-password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
