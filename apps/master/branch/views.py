from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MasterBranch
from .froms import MasterBranchForm

from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_branch_slug='master_branch'
class BranchListView(ListView):
    model = MasterBranch
    template_name = 'master/branch/index.html'
    context_object_name = 'branches'
    paginate_by = 50
    
    @permission_required(_branch_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = MasterBranch.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Branch'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Branch', 'url':'branch_list'}]
        context['new_url'] = 'branch_create'
        context['can_add'] = has_permission(self.request.user, 'state', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'state', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'state', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class BranchDetailView(DetailView):
    model = MasterBranch
    template_name = 'master/branch/detail.html'
    
    @permission_required(_branch_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class BranchCreateView(CreateView):
    model = MasterBranch
    form_class = MasterBranchForm
    template_name = 'master/branch/form.html'
    success_url = reverse_lazy('branch_list')
    
    @permission_required(_branch_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(BranchCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Branch'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Branch', 'url':'branch_list'},{'name':'Create Branch', 'url':'branch_create'}]
        return context
    
class BranchUpdateView(UpdateView):
    model = MasterBranch
    form_class = MasterBranchForm
    template_name = 'master/branch/form.html'
    success_url = reverse_lazy('branch_list')
    
    @permission_required(_branch_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update State'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Branch', 'url':'branch_list'},{'name':'Update Branch'}]
        return context
    
class BranchDeleteView(DeleteView):
    model = MasterBranch
    template_name = 'master/branch/confirm_delete.html'
    success_url = reverse_lazy('branch_list')
    
    @permission_required(_branch_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)