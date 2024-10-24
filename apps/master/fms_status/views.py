from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FmsStatus
from .forms import FmsStatusForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Menu_Slug='fms-stage'
class FmsStatusListView(ListView):
    model = FmsStatus
    template_name = 'master/fms_status/index.html'
    context_object_name = 'fms_status'
    paginate_by = 50
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = FmsStatus.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'FMS Stage'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS_Stage', 'url':'fms_status_list'}]
        context['new_url'] = 'fms_status_create'
        context['can_add'] = has_permission(self.request.user, 'fms_stage', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'fms_stage', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'fms_stage', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class FmsStatusDetailView(DetailView):
    model = FmsStatus
    template_name = 'master/fms_status/detail.html'
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class FmsStatusCreateView(CreateView):
    model = FmsStatus
    form_class = FmsStatusForm
    template_name = 'master/fms_status/form.html'
    success_url = reverse_lazy('fms_status_list')
    
    @permission_required(_Menu_Slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(FmsStatusCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create FMS Stage'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS_Stage', 'url':'fms_status_list'},{'name':'Create FMS stages', 'url':'fms_stage_create'}]
        return context
    
class FmsStatusUpdateView(UpdateView):
    model = FmsStatus
    form_class = FmsStatusForm
    template_name = 'master/fms_status/form.html'
    success_url = reverse_lazy('fms_status_list')
    
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
        context['page_title'] = 'Update FMS stage'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS stage', 'url':'fms_status_list'},{'name':'Update FMS stage'}]
        return context
    
class FmsStatusDeleteView(DeleteView):
    model = FmsStatus
    template_name = 'master/fms_status/confirm_delete.html'
    success_url = reverse_lazy('fms_status_list')
    
    @permission_required(_Menu_Slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def form_valid(self, form):
        messages.success(self.request, "Delete Successfully")
        return super().form_valid(form)
    # def post(self, request, *args, **kwargs):
    #     FMS_stage = FmsStatus.objects.get(pk=self.kwargs['pk'])
    #     FMS_stage.deleted_by = self.request.user  
    #     FMS_stage.deleted_date = timezone.now()   
    #     FMS_stage.disable = True  
    #     FMS_stage.save()
    #     messages.success(self.request, 'Deleted Successfully')
    #     return redirect(self.success_url)
    

    

