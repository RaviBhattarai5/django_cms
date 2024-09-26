from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PermissionType
from .forms import PermissionTypeForm
from django.contrib import messages
from utils.common import arrange_pagination

class PermissionTypeListView(ListView):
    model = PermissionType
    template_name = 'permission_type/index.html'
    context_object_name = 'permission_types'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = PermissionType.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Permission Type'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'PermissionType', 'url':'permission_type_list'}]
        context['new_url'] = 'permission_type_create'
        
        context = arrange_pagination(context)
        return context

class PermissionTypeDetailView(DetailView):
    model = PermissionType
    template_name = 'permission_type/detail.html'
    
class PermissionTypeCreateView(CreateView):
    model = PermissionType
    form_class = PermissionTypeForm
    template_name = 'permission_type/form.html'
    success_url = reverse_lazy('permission_type_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create PermissionType'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'PermissionType', 'url':'permission_type_list'},{'name':'Create Permission Type', 'url':'permission_type_create'}]
        return context

class PermissionTypeUpdateView(UpdateView):
    model = PermissionType
    form_class = PermissionTypeForm
    template_name = 'permission_type/form.html'
    success_url = reverse_lazy('permission_type_list')
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update PermissionType'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'PermissionType', 'url':'permission_type_list'},{'name':'Update Permission Type'}]
        return context
    
class PermissionTypeDeleteView(DeleteView):
    model = PermissionType
    success_url = reverse_lazy('permission_type_list')
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)