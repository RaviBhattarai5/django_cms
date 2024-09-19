from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'layouts/base.html',{'page_title':'Dashboard'})