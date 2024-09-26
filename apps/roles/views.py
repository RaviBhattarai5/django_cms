from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from .models import Roles
from .forms import RolesForm
from django.core.paginator import Paginator
from django.contrib import messages
from utils.paginator import get_paginated_queryset
class RolesView(View):
    template_name = 'roles/roles.html'

    def get(self, request):
        roles = Roles.objects.all() 
        form = RolesForm() 
       
        page_obj, page_range = get_paginated_queryset(roles, request, per_page=2)

        return render(request, self.template_name, {
            'page_obj': page_obj, 
            'form': form, 
            'page_range': page_range,
        })


    def post(self, request):
        form = RolesForm(request.POST)  
        if form.is_valid():
            form.save()  
            messages.success(request, "Role Create successfully! ")
            return redirect('roles') 
        
        roles = Roles.objects.all() 
        return render(request, self.template_name, {'data': roles, 'form': form})
    

    
   
class RolesDeleteView(DeleteView):
    model = Roles
    template_name = 'roles/role_delete.html'
    success_url = reverse_lazy('roles')

    def form_valid(self, form):
        messages.success(self.request, "Delete successfully!")
        return super().form_valid(form)

class RolesUpdateView(UpdateView):
    model = Roles
    form_class = RolesForm
    template_name = 'roles/role_edit.html'
    success_url = reverse_lazy('roles')

    def form_valid(self, form):
        if self.request.method == 'POST':
            print("Data is being posted.")
        return super().form_valid(form)


