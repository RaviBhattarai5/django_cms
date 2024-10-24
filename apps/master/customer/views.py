from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomerMaster
from .forms import CustomerMasterForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_menu_slug='customer'

#! ListView..
class CustomerListView(ListView):
    model = CustomerMaster
    template_name = 'master/customer/index.html'
    context_object_name = 'customers'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = CustomerMaster.objects.all().order_by('id')
        title = self.request.GET.get('customer_name')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Customer'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Customer', 'url':'customer_list'}]
        context['new_url'] = 'customer_create'
        context['can_add'] = has_permission(self.request.user, 'customer', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'customer', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'customer', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
#! DetailView   
class CustomerDetailView(DetailView):
    model = CustomerMaster
    template_name = 'master/customer/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

#! CreateView
class CustomerCreateView(CreateView):
    model = CustomerMaster
    form_class = CustomerMasterForm
    template_name = 'master/customer/form.html'
    success_url = reverse_lazy('customer_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(CustomerCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Customer'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Customers', 'url':'customer_list'},{'name':'Create Customers', 'url':'customer_create'}]
        return context

#! UpdateView  
class CustomerUpdateView(UpdateView):
    model = CustomerMaster
    form_class = CustomerMasterForm
    template_name = 'master/customer/form.html'
    success_url = reverse_lazy('customer_list')
    

    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Customers', 'url':'customer_list'},{'name':'Update customer', 'url':'customer_update'}]
        return context
    

class CustomerUpdateView(UpdateView):
    model = CustomerMaster
    form_class = CustomerMasterForm
    template_name = 'master/customer/form.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Customer'
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': 'dashboard'},
            {'name': 'Customers', 'url': 'customer_list'},
            {'name': 'Update Customer'}
        ]
        return context
#! DeleteView
class CustomerDeleteView(DeleteView):
    model = CustomerMaster
    template_name = 'customer/confirm_delete.html'
    success_url = reverse_lazy('customer_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)