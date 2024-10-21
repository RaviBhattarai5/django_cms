from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

def home(request):
    return render(request, 'layouts/base.html',{'page_title':'Dashboard'})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        try:
            validate_password(password)
            if password==confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email is already exists !!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, "Register Successfully !")
                    return redirect('login')
            else:
                messages.error(request, "Password does not match")
                return redirect('register')
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return redirect('register')
        
    return render(request, 'administrator/registration/register.html')


def log_in(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        try:
            # Check if the input is an email or username
            if '@' in username_or_email:
                user = User.objects.get(email=username_or_email)
            else:
                user = User.objects.get(username=username_or_email)

            # Authenticate user
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to your desired page
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
    return render(request, 'administrator/registration/login.html')

def log_out(request):
    logout(request)
    return redirect('login')


def password_change(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_form=PasswordChangeForm(user=request.user)
    if request.method=="POST":
        user_form=PasswordChangeForm(user=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    context={
        'user_form':user_form
    }
    return render(request, 'registration/password_change.html', context)

def error_403(request):
    return render(request, '403.html')
    