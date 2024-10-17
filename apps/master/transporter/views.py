from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Transporter
from .forms import TransporterForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone

_menu_slug='master_group'
class TransporterListView(ListView):
    model = Transporter
    template_name = 'master/transporter/index.html'
    context_object_name = 'transporters'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Transporter.objects.all().order_by('id')
        title = self.request.GET.get('transporter_name')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Transporter'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter', 'url':'transporter_list'}]
        context['new_url'] = 'transporter_create'
        context['can_add'] = has_permission(self.request.user, 'group', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'group', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'group', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class TransporterDetailView(DetailView):
    model = Transporter
    template_name = 'master/transporter/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class TransporterCreateView(CreateView):
    model = Transporter
    form_class = TransporterForm
    template_name = 'master/transporter/forms.html'
    success_url = reverse_lazy('transporter_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(TransporterCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.createdBy = self.request.user  
        form.instance.createdDate = timezone.now()  
        messages.success(self.request, 'Created Successfully')

        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Groupe '
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter', 'url':'transporter_list'},{'name':'Create Group', 'url':'transporter_create'}]
        return context
    
class TransporterUpdateView(UpdateView):
    model = Transporter
    form_class = TransporterForm
    template_name = 'master/transporter/forms.html'
    success_url = reverse_lazy('transporter_list')
    
    @permission_required(_menu_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updatedBy = self.request.user  
        form.instance.updatedDate = timezone.now()   
        messages.success(self.request, 'Updated Successfully')

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Transporter'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'transporter_list'},{'name':'Update Transporter'}]
        return context
    
class TransporterDeleteView(DeleteView):
    model = Transporter
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('transporter_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        group = self.get_object()
        group.deleted_by = self.request.user  
        group.deleted_date = timezone.now()   
        group.is_deleted = True               
        group.save()

        messages.success(self.request, 'Deleted successfully')
        return redirect(self.success_url)
