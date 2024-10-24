from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import LeadSource
from .forms import LeadSourceForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Menu_Slug='lead-source'

class LeadSourceListView(ListView):
    model = LeadSource
    template_name = 'master/lead_source/index.html'
    context_object_name = 'lead_sources'
    paginate_by = 50
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = LeadSource.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'LeadSource'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Lead Source', 'url':'lead_source_list'}]
        context['new_url'] = 'lead_source_create'
        context['can_add'] = has_permission(self.request.user, 'lead_source', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'lead_source', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'lead_source', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class LeadSourceDetailView(DetailView):
    model = LeadSource
    template_name = 'master/lead_source/detail.html'
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class LeadSourceCreateView(CreateView):
    model = LeadSource
    form_class = LeadSourceForm
    template_name = 'master/lead_source/form.html'
    success_url = reverse_lazy('lead_source_list')
    
    @permission_required(_Menu_Slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(LeadSourceCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Lead Source'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Lead Source', 'url':'lead_source_list'},{'name':'Create Lead Source', 'url':'lead_source_create'}]
        return context
    
class LeadSourceUpdateView(UpdateView):
    model = LeadSource
    form_class = LeadSourceForm
    template_name = 'master/lead_source/form.html'
    success_url = reverse_lazy('lead_source_list')
    
    @permission_required(_Menu_Slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        form.instance.updated_date = timezone.now() 
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Lead Source'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Lead Source', 'url':'lead_source_list'},{'name':'Update Lead Source'}]
        return context
    
class LeadSourceDeleteView(DeleteView):
    model = LeadSource
    template_name = 'master/lead_source/confirm_delete.html'
    success_url = reverse_lazy('lead_source_list')
    
    @permission_required(_Menu_Slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
       messages.success(self.request, 'Delete Successfully ')
       return super().form_valid(form)
   
    
