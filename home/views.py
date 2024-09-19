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


