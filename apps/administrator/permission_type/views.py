from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PermissionType
from .forms import PermissionTypeForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

class PermissionTypeListView(ListView):
    model = PermissionType
    template_name = 'administrator/permission_type/index.html'
    context_object_name = 'permission_types'
    paginate_by = 50
    
    @permission_required('permission-type', 'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = PermissionType.objects.all().order_by('id')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Permission Types'
        context['breadcrumbs'] = [{'name': 'Dashboard', 'url': 'dashboard'}, {'name': 'Permission Types', 'url': 'permission_type_list'}]
        context['new_url'] = 'permission_type_create'
        context['can_add'] = has_permission(self.request.user, 'permission-type', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'permission-type', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'permission-type', 'Delete')
        context = arrange_pagination(context)
        return context

class PermissionTypeDetailView(DetailView):
    model = PermissionType
    template_name = 'administrator/permission_type/detail.html'
    
    @permission_required('permission-type', 'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PermissionTypeCreateView(CreateView):
    model = PermissionType
    form_class = PermissionTypeForm
    template_name = 'administrator/permission_type/form.html'
    success_url = reverse_lazy('permission_type_list')
    
    @permission_required('permission-type', 'Create')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Permission Type'
        context['breadcrumbs'] = [{'name': 'Dashboard', 'url': 'dashboard'}, {'name': 'Permission Types', 'url': 'permission_type_list'}, {'name': 'Create Permission Type', 'url': 'permission_type_create'}]
        return context

class PermissionTypeUpdateView(UpdateView):
    model = PermissionType
    form_class = PermissionTypeForm
    template_name = 'administrator/permission_type/form.html'
    success_url = reverse_lazy('permission_type_list')
    
    @permission_required('permission-type', 'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Permission Type'
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': 'dashboard'}, 
            {'name': 'Permission Types', 'url': 'permission_type_list'}, 
            {'name': 'Update Permission Type'}]
        return context

class PermissionTypeDeleteView(DeleteView):
    model = PermissionType
    template_name = 'administrator/permission_type/confirm_delete.html'
    success_url = reverse_lazy('permission_type_list')
    
    @permission_required('permission-type','Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)
