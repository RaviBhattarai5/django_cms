from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FmsStage
from .forms import FmsStageForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Menu_Slug='fms-stage'
class FmsStageListView(ListView):
    model = FmsStage
    template_name = 'master/fms_stage/index.html'
    context_object_name = 'fms_stages'
    paginate_by = 50
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = FmsStage.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'FMS Stage'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS_Stage', 'url':'fms_stage_list'}]
        context['new_url'] = 'fms_stage_create'
        context['can_add'] = has_permission(self.request.user, 'fms_stage', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'fms_stage', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'fms_stage', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class FmsStageDetailView(DetailView):
    model = FmsStage
    template_name = 'master/fms_stage/detail.html'
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class FmsStageCreateView(CreateView):
    model = FmsStage
    form_class = FmsStageForm
    template_name = 'master/fms_stage/form.html'
    success_url = reverse_lazy('fms_stage_list')
    
    @permission_required(_Menu_Slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(FmsStageCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create FMS Stage'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS_Stage', 'url':'fms_stage_list'},{'name':'Create FMS stages', 'url':'fms_stage_create'}]
        return context
    
class FmsStageUpdateView(UpdateView):
    model = FmsStage
    form_class = FmsStageForm
    template_name = 'master/fms_stage/form.html'
    success_url = reverse_lazy('fms_stage_list')
    
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
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FMS stage', 'url':'fms_stage_list'},{'name':'Update FMS stage'}]
        return context
    
class FmsStageDeleteView(DeleteView):
    model = FmsStage
    template_name = 'master/fms_stage/confirm_delete.html'
    success_url = reverse_lazy('fms_stage_list')
    
    @permission_required(_Menu_Slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        FMS_stage = FmsStage.objects.get(pk=self.kwargs['pk'])
        FMS_stage.deleted_by = self.request.user  
        FMS_stage.deleted_date = timezone.now()   
        FMS_stage.disable = True  
        FMS_stage.save()
        messages.success(self.request, 'Deleted Successfully')
        return redirect(self.success_url)
    
    def form_valid(self, form):
        messages.success(self.request, "Delete Successfully")
        return super().form_valid(form)
    

