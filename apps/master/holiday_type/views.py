from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import HolidaysType
from .forms import HolidaysTypeForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
_menu_slug='holiday-type'
class HolidayTypeListView(ListView):
    model = HolidaysType
    template_name = 'master/holiday_type/index.html'
    context_object_name = 'holiday_types'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = HolidaysType.objects.all().order_by('id')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Holiday Type'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Holiday Type', 'url':'holiday_type_list'}]
        context['new_url'] = 'holiday_type_create'
        context['can_add'] = has_permission(self.request.user, 'holiday_type', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'holiday_type', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'holiday_type', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class GroupDetailView(DetailView):
    model = HolidaysType
    template_name = 'master/holiday_type/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
# 
class HolidaysTypeCreateView(CreateView):
    model = HolidaysType
    form_class = HolidaysTypeForm
    template_name = 'master/holiday_type/forms.html'
    success_url = reverse_lazy('holiday_type_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(HolidaysTypeCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Holiday Type'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Holiday Type', 'url':'holiday_type_list'},{'name':'Create Holiday Type', 'url':'holiday_type_create'}]
        return context
    
class HolidaysTypeUpdateView(UpdateView):
    model = HolidaysType
    form_class = HolidaysTypeForm
    template_name = 'master/holiday_type/forms.html'
    success_url = reverse_lazy('holiday_type_list')
    
    @permission_required(_menu_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Holiday Type'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Holiday Type', 'url':'holiday_type_list'},{'name':'Update Holiday Type'}]
        return context
    
class HolidaysTypeDeleteView(DeleteView):
    model = HolidaysType
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('holiday_type_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Delete Successfully")
        return super().form_valid(form)