from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MasterGroup
from .forms import MasterGroupForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
_menu_slug='master_group'
class GroupListView(ListView):
    model = MasterGroup
    template_name = 'master/group/index.html'
    context_object_name = 'groups'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = MasterGroup.objects.all().order_by('id')
        title = self.request.GET.get('groupName')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Group'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Group', 'url':'group_list'}]
        context['new_url'] = 'group_create'
        context['can_add'] = has_permission(self.request.user, 'group', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'group', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'group', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class GroupDetailView(DetailView):
    model = MasterGroup
    template_name = 'master/group/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class GroupCreateView(CreateView):
    model = MasterGroup
    form_class = MasterGroupForm
    template_name = 'master/group/forms.html'
    success_url = reverse_lazy('group_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(GroupCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.createdBy = self.request.user  
        form.instance.createdDate = timezone.now()  
        messages.success(self.request, 'Created Successfully')

        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Groupe '
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'group_list'},{'name':'Create Group', 'url':'group_create'}]
        return context
    
class GroupUpdateView(UpdateView):
    model = MasterGroup
    form_class = MasterGroupForm
    template_name = 'master/group/forms.html'
    success_url = reverse_lazy('group_list')
    
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
        context['page_title'] = 'Groupte Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'group_list'},{'name':'Update Group'}]
        return context
    
class GroupDeleteView(DeleteView):
    model = MasterGroup
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('group_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        group = self.get_object()
        group.deleted_by = self.request.user  
        group.deleted_date = timezone.now()   
        group.is_deleted = True               
        group.save()

        messages.success(self.request, 'Group deleted successfully')
        return redirect(self.success_url)
