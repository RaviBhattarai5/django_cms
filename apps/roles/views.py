from django.shortcuts import render, redirect
# 
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from django.views.generic.edit import UpdateView
from .models import Roles

from django.views import View
from django.shortcuts import render, redirect
from .models import Roles
from .forms import RolesForm

class RolesView(View):
    template_name = 'roles/roles.html'

    def get(self, request):
        roles = Roles.objects.all()  
        form = RolesForm() 
        return render(request, self.template_name, {'data': roles, 'form': form})

    def post(self, request):
        form = RolesForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('roles') 
        roles = Roles.objects.all() 
        return render(request, self.template_name, {'data': roles, 'form': form})

    
   
class RolesDeleteView(DeleteView):
    model = Roles
    template_name = 'roles/role_delete.html'
    success_url = reverse_lazy('roles')

class RolesUpdateView(UpdateView):
    model = Roles
    fields = ['role_name', 'descriptions', 'isRole']
    template_name = 'roles/role_edit.html'
    success_url = reverse_lazy('roles')
