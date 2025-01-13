from django.urls import path
from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),  # Home page
    path('login/', views.student_login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.school_dashboard, name='dashboard'),
    
]