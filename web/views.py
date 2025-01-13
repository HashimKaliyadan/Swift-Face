from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.models import Student  
from django.contrib.auth.models import User
from django.contrib import messages

# Index view
def index(request):
    return render(request, 'web/index.html') 
# Student login view
def student_login(request):
    if request.method == 'POST':
        school_id = request.POST.get('school_id')
        password = request.POST.get('password')  

        try:
            student = Student.objects.get(school_id=school_id)  # Now querying by school_id
            user = authenticate(request, username=student.user.username, password=password)
        except Student.DoesNotExist:
            user = None 
        
        if user is not None:
            auth_login(request, user)  
            return HttpResponseRedirect(reverse('web:dashboard')) 
        else:
            return render(request, 'web/student_login.html', {'error': 'Invalid credentials'}) 
    else:
        return render(request, 'web/student_login.html')

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        full_name = request.POST.get('full_name')
        school_id = request.POST.get('school_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate form inputs
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'web/register.html')

        if User.objects.filter(username=school_id).exists():
            messages.error(request, "School ID already registered.")
            return render(request, 'web/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'web/register.html')

        # Split full name into first and last name
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

        # Create the user
        user = User.objects.create_user(
            username=school_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()

        # Create a student profile
        author = Student.objects.create(user=user, school_id=school_id)  # Now including school_id
        author.save()

        messages.success(request, "Registration successful! Please log in.")
        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')
    
def school_dashboard(request):
    return render(request, 'web/student_dashboard.html')
    
        

