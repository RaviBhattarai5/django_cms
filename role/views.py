from django.shortcuts import render, redirect
from .models import Role
from django.contrib import messages
def role(request):
    role_lists=Role.objects.all()
    if request.method=="POST":
        role_name=request.POST['role_name']
        descriptions=request.POST['role_name']
        Role.objects.create(role_name=role_name, descriptions=descriptions, isRole=True)
        messages.success(request, 'Successfull register')
        return redirect('role')
    context={
        'role_lists':role_lists
    }
    return render(request, 'role.html', context)

        