from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ProductBin
from .froms import ProductBinForm

from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
_ProductBin_slug='master_ProductBin'
class ProductBinListView(ListView):
    model = ProductBin
    template_name = 'master/product_bin/index.html'
    context_object_name = 'product_bins'
    paginate_by = 50
    
    @permission_required(_ProductBin_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = ProductBin.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ProductBin'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductBin', 'url':'product_bin_list'}]
        context['new_url'] = 'product_bin_create'
        context['can_add'] = has_permission(self.request.user, 'ProductBin', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'ProductBin', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'ProductBin', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class ProductBinDetailView(DetailView):
    model = ProductBin
    template_name = 'master/product_bin/detail.html'
    
    @permission_required(_ProductBin_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductBinCreateView(CreateView):
    model = ProductBin
    form_class = ProductBinForm
    template_name = 'master/product_bin/form.html'
    success_url = reverse_lazy('product_bin_list')
    
    @permission_required(_ProductBin_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(ProductBinCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create ProductBin'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductBin', 'url':'product_bin_list'},{'name':'Create ProductBin', 'url':'product_bin_create'}]
        return context
    
class ProductBinUpdateView(UpdateView):
    model = ProductBin
    form_class = ProductBinForm
    template_name = 'master/product_bin/form.html'
    success_url = reverse_lazy('product_bin_list')
    
    @permission_required(_ProductBin_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update ProductBin'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductBin', 'url':'product_bin_list'},{'name':'Update ProductBin'}]
        return context
    
class ProductBinDeleteView(DeleteView):
    model = ProductBin
    template_name = 'master/product_bin/confirm_delete.html'
    success_url = reverse_lazy('product_bin_list')
    
    @permission_required(_ProductBin_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)