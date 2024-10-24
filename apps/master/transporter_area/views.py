from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TransporterArea
from .forms import TransporterAreaForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone


_Product_slug='transporter-area'
class TransporterAreaListView(ListView):
    model = TransporterArea
    template_name = 'master/transporter_area/index.html'
    context_object_name = 'transporter_areas'
    paginate_by = 50
    
    @permission_required(_Product_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = TransporterArea.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Transporter Area'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter Area', 'url':'transporter_area_list'}]
        context['new_url'] = 'transporter_area_create'
        context['can_add'] = has_permission(self.request.user, 'transporter_area', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'transporter_area', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'transporter_area', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class TransporterAreaDetailView(DetailView):
    model = TransporterArea
    template_name = 'master/transporter_area/detail.html'
    
    @permission_required(_Product_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class TransporterAreaCreateView(CreateView):
    model = TransporterArea
    form_class = TransporterAreaForm
    template_name = 'master/transporter_area/form.html'
    success_url = reverse_lazy('transporter_area_list')
    
    @permission_required(_Product_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(TransporterAreaCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Transporter Area'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter Area', 'url':'transporter_area_list'},{'name':'Create Transporter Area', 'url':'transporter_area_create'}]
        return context
    
class TransporterAreaUpdateView(UpdateView):
    model = TransporterArea
    form_class = TransporterAreaForm
    template_name = 'master/transporter_area/form.html'
    success_url = reverse_lazy('transporter_area_list')
    
    @permission_required(_Product_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        form.instance.updated_date = timezone.now() 
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Transporter Area'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter Area', 'url':'transporter_area_list'},{'name':'Update Transporter Area'}]
        return context
    
class TransporterAreaDeleteView(DeleteView):
    model = TransporterArea
    template_name = 'master/transporter_area/confirm_delete.html'
    success_url = reverse_lazy('transporter_area_list')
    
    @permission_required(_Product_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request,"Successfully Deleted" )
        return super().form_valid(form)
    
