from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import HolidayInArea
from .forms import HolidayInAreaForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone
_menu_slug='holiday-in-area'

class HolidayListView(ListView):
    model = HolidayInArea
    template_name = 'master/holiday_in_area/index.html'
    context_object_name = 'holiday_in_areas'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # def get_queryset(self):
    #     queryset = Holidays.objects.all().order_by('id')
    #     title = self.request.GET.get('holiday_type')
    #     if title:
    #         queryset = queryset.filter(title__icontains=title) 
    #     return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Holidays'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Holiday', 'url':'holiday_in_list'}]
        context['new_url'] = 'holiday_in_area_create'
        context['can_add'] = has_permission(self.request.user, 'holiday_in_area', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'holiday_in_area', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'holiday_in_area', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class HolidayCreateView(CreateView):
    model = HolidayInArea
    form_class = HolidayInAreaForm
    template_name = 'master/holiday_in_area/forms.html'
    success_url = reverse_lazy('holiday_in_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(HolidayCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_bate = timezone.now()  
        messages.success(self.request, 'Created Successfully')

        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Groupe '
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'holiday_in_list'},{'name':'Create Holidays', 'url':'holiday_in_area_create'}]
        return context
    
class HolidayUpdateView(UpdateView):
    model = HolidayInArea
    form_class = HolidayInAreaForm
    template_name = 'master/holiday_in_area/forms.html'
    success_url = reverse_lazy('holiday_in_list')
    
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
        context['page_title'] = 'Holidays'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'holiday_in_list'},{'name':'Update Holidays'}]
        return context
    
class HolidayDeleteView(DeleteView):
    model = HolidayInArea
    success_url = reverse_lazy('holiday_in_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        holiday_in_area = self.get_object()
        holiday_in_area.deleted_by = self.request.user  
        holiday_in_area.deleted_date = timezone.now()   
        holiday_in_area.is_deleted = True               
        holiday_in_area.save()

        messages.success(self.request, 'Group deleted successfully')
        return redirect(self.success_url)
