from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FmsContact
from .forms import FmsContactForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Menu_Slug='FmsContacts'
class FmsContactListView(ListView):
    model = FmsContact
    template_name = 'master/fms_contact/index.html'
    context_object_name = 'fms_contacts'
    paginate_by = 50
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = FmsContact.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'FmsContacts'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FmsContacts', 'url':'fms_contact_list'}]
        context['new_url'] = 'fms_contact_create'
        context['can_add'] = has_permission(self.request.user, 'FmsContacts', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'FmsContacts', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'FmsContacts', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class FmsContactDetailView(DetailView):
    model = FmsContact
    template_name = 'master/fms_contact/detail.html'
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class FmsContactCreateView(CreateView):
    model = FmsContact
    form_class = FmsContactForm
    template_name = 'master/fms_contact/form.html'
    success_url = reverse_lazy('fms_contact_list')
    
    @permission_required(_Menu_Slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(FmsContactCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create FmsContacts'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FmsContacts', 'url':'fms_contact_list'},{'name':'Create FmsContacts', 'url':'fms_contact_create'}]
        return context
    
class FmsContactUpdateView(UpdateView):
    model = FmsContact
    form_class = FmsContactForm
    template_name = 'master/fms_contact/form.html'
    success_url = reverse_lazy('fms_contact_list')
    
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
        context['page_title'] = 'Update FmsContacts'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'FmsContacts', 'url':'fms_contact_list'},{'name':'Update FmsContacts'}]
        return context
    
class FmsContactDeleteView(DeleteView):
    model = FmsContact
    template_name = 'master/fms_contact/confirm_delete.html'
    success_url = reverse_lazy('fms_contact_list')
    
    @permission_required(_Menu_Slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     FmsContacts = FmsContact.objects.get(pk=self.kwargs['pk'])
    #     FmsContacts.deleted_by = self.request.user  
    #     FmsContacts.deleted_date = timezone.now()   
    #     FmsContacts.disable = True  
    #     FmsContacts.save()
    #     messages.success(self.request, 'Deleted Successfully')
    #     return redirect(self.success_url)
    
    def form_valid(self, form):
        messages.success(self.request, "Delete Successfully")
        return super().form_valid(form)
    

