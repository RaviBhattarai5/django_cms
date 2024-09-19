from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'layouts/base.html',{'page_title':'Dashboard'})

# def register(request):
#     return render(request, 'registration/register.html')


def register(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        try:
            validate_password(password)
            if password==confirm_password:
                if User.objects.filter(username=email).exists():
                    messages.info(request, 'Email is already exists !!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=email, password=password)
                    messages.success(request, "Register Successfully !")
                    return redirect('login')
            else:
                messages.error(request, "Password does not match")
                return redirect('register')
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return redirect('register')
        
    return render(request, 'registration/register.html')


def log_in(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        if not username or not password:
            messages.error(request, 'All fields are required.')
            return redirect('login')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'User is not register yet !!')
            return redirect('login')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid keyword !!')
            return redirect('login')
    return render(request, 'registration/login.html')

def log_out(request):
    logout(request)
    return redirect('login')


