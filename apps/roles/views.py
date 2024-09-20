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
from django.core.paginator import Paginator
class RolesView(View):
    template_name = 'roles/roles.html'

    def get(self, request):
        roles = Roles.objects.all()  
        form = RolesForm() 
       

        paginator = Paginator(roles, 2)
        page_number = request.GET.get('page')
        servicedatafinal = paginator.get_page(page_number)
        totalpage = servicedatafinal.paginator.num_pages
        
        return render(request, self.template_name, {
            'roles': servicedatafinal, 
            'form': form, 
            'lastpage': totalpage,
            'totalPagelist': [n+1 for n in range(totalpage)],
        })


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
