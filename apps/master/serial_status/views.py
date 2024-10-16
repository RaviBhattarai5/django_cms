from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SerialStatus
from .forms import SerialStatusForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_menu_slug='serial_status'
class SerialStatusListView(ListView):
    model = SerialStatus
    template_name = 'master/serial_status/index.html'
    context_object_name = 'serial_status'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = SerialStatus.objects.all().order_by('id')
        title = self.request.GET.get('serialStatus')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Group'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Serial Status', 'url':'serial_status_list'}]
        context['new_url'] = 'serial_status_create'
        context['can_add'] = has_permission(self.request.user, 'serial_status', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'erial_status', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'erial_status', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class SerialStatusDetailView(DetailView):
    model = SerialStatus
    template_name = 'master/serial_status/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class SerialStatusCreateView(CreateView):
    model = SerialStatus
    form_class = SerialStatusForm
    template_name = 'master/serial_status/forms.html'
    success_url = reverse_lazy('serial_status_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(SerialStatusCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Groupte Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Serial Status', 'url':'serial_status_list'},{'name':'Create SerialStatus', 'url':'serial_status_create'}]
        return context
    
class SerialStatusUpdateView(UpdateView):
    model = SerialStatus
    form_class = SerialStatusForm
    template_name = 'master/serial_status/forms.html'
    success_url = reverse_lazy('serial_status_list')
    
    @permission_required(_menu_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Groupte Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Serial Status', 'url':'serial_status_list'},{'name':'Update SerialStatus'}]
        return context
    
class SerialStatusDeleteView(DeleteView):
    model = SerialStatus
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('serial_status_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)
