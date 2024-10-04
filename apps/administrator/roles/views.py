from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Roles
from .forms import RolesForm
from utils.permissions import has_permission  # Assuming a utility for permission checking
from utils.paginator import get_paginated_queryset # Custom pagination utility
from decorators.decorators import permission_required

class RolesView(View):
    template_name = 'administrator/roles/roles.html'

    # Handle GET request
    def get(self, request, *args, **kwargs):
        form = RolesForm()  # Empty form for role creation
        roles = self.get_filtered_queryset(request)  # Fetch and filter roles
        context = self.get_context_data(request, form, roles)  # Prepare context data
        return render(request, self.template_name, context)

    # Handle POST request (form submission)
    def post(self, request, *args, **kwargs):
        form = RolesForm(request.POST)  # Bind form to POST data
        if form.is_valid():
            form.save()  # Save the new role
            messages.success(request, "Role created successfully!")
            return redirect('roles')  # Redirect back to the roles list
        
        # If the form is invalid, re-render the page with errors
        roles = self.get_filtered_queryset(request)  # Re-fetch roles for display
        context = self.get_context_data(request, form, roles)
        return render(request, self.template_name, context)

    # Function to get filtered queryset (if filtering is needed, e.g., by name)
    def get_filtered_queryset(self, request):
        queryset = Roles.objects.all().order_by('id')
        role_name = request.GET.get('role_name')  # Optional filter by role name
        if role_name:
            queryset = queryset.filter(name__icontains=role_name)  # Filter by role name
        return queryset

    # Function to prepare the context data for rendering the template
    def get_context_data(self, request, form, roles):
        page_obj, page_range = get_paginated_queryset(roles, request, per_page=10)  # Paginate roles
        return {
            'form': form,  # The form for creating new roles
            'page_obj': page_obj,  # Paginated roles list
            'page_range': page_range,  # Range of pages for frontend pagination
            'page_title': 'Roles',
            'breadcrumbs': [
                {'name': 'Dashboard', 'url': 'dashboard'},
                {'name': 'Roles', 'url': 'roles'}
            ],
            'new_url': reverse_lazy('roles'),
            'can_add': has_permission(request.user, 'role', 'Create'),  # Permission to create roles
            'can_edit': has_permission(request.user, 'role', 'Edit'),  # Permission to edit roles
            'can_delete': has_permission(request.user, 'role', 'Delete'),  # Permission to delete roles
        }

   
class RolesDeleteView(DeleteView):
    model = Roles
    template_name = 'administrator/roles/role_delete.html'
    success_url = reverse_lazy('roles')

    @permission_required('role', 'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Delete successfully!")
        return super().form_valid(form)

class RolesUpdateView(UpdateView):
    model = Roles
    form_class = RolesForm
    template_name = 'administrator/roles/role_edit.html'
    success_url = reverse_lazy('roles')

    @permission_required('role','Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Update successfully!")
        return super().form_valid(form)


