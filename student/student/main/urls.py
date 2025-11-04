from django.urls import path
from . import views  # import your views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('home/', views.home, name='home'),
     path('', views.student_list, name='student_list'),
    path('student/<str:roll_no>/', views.student_detail, name='student_detail'),
    # Password change URLs
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),

    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]

