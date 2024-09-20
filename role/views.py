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

def role_update(request, id):
    role_user=Role.objects.get(id=id)
    if request.method=="POST":
        role_user.role_name=request.POST['role_name']
        role_user.descriptions=request.POST['role_name']
        role_user.isRole=request.POST['isRole']
        role_user.save()
        return redirect('role')
    return render(request, 'role.html')


def role_delete(request, id):
    role_user=Role.objects.get(id=id)
    role_user.delete()
    return redirect('login')



        

        