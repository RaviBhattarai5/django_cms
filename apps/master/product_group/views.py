from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ProductGroup
from .forms import ProductGroupForm

from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_ProductGroup_slug='master_product_group'
class ProductGroupListView(ListView):
    model = ProductGroup
    template_name = 'master/product_group/index.html'
    context_object_name = 'product_groups'
    paginate_by = 50
    
    @permission_required(_ProductGroup_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = ProductGroup.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ProductGroup'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductGroup', 'url':'product_group_list'}]
        context['new_url'] = 'product_group_create'
        context['can_add'] = has_permission(self.request.user, 'ProductGroup', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'ProductGroup', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'ProductGroup', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class ProductGroupDetailView(DetailView):
    model = ProductGroup
    template_name = 'master/product_group/detail.html'
    
    @permission_required(_ProductGroup_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductGroupCreateView(CreateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'master/product_group/form.html'
    success_url = reverse_lazy('product_group_list')
    
    @permission_required(_ProductGroup_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(ProductGroupCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create ProductGroup'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductGroup', 'url':'product_group_list'},{'name':'Create ProductGroup', 'url':'product_group_create'}]
        return context
    
class ProductGroupUpdateView(UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'master/product_group/form.html'
    success_url = reverse_lazy('product_group_list')
    
    @permission_required(_ProductGroup_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update ProductGroup'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductGroup', 'url':'product_group_list'},{'name':'Update ProductGroup'}]
        return context
    
class ProductGroupDeleteView(DeleteView):
    model = ProductGroup
    template_name = 'master/product_group/confirm_delete.html'
    success_url = reverse_lazy('product_group_list')
    
    @permission_required(_ProductGroup_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)