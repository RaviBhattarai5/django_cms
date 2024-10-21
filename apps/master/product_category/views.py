from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ProdutCategory
from .forms import ProdutCategoryForm

from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_ProductCategory_slug='product_category'

class ProductCategoryListView(ListView):
    model = ProdutCategory
    template_name = 'master/product_category/index.html'
    context_object_name = 'product_categories'
    paginate_by = 50
    
    @permission_required(_ProductCategory_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = ProdutCategory.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'ProductCategory'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductCategory', 'url':'product_category_list'}]
        context['new_url'] = 'product_category_create'
        context['can_add'] = has_permission(self.request.user, 'products', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'products', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'products', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class ProductCategoryDetailView(DetailView):
    model = ProdutCategory
    template_name = 'master/product_category/detail.html'
    
    @permission_required(_ProductCategory_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductCategoryCreateView(CreateView):
    model = ProdutCategory
    form_class = ProdutCategoryForm
    template_name = 'master/product_category/form.html'
    success_url = reverse_lazy('product_category_list')
    
    @permission_required(_ProductCategory_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create ProductCategory'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductCategory', 'url':'product_category_list'},{'name':'Create ProductCategory'}]
        return context
    
class ProductCategoryUpdateView(UpdateView):
    model = ProdutCategory
    form_class = ProdutCategoryForm
    template_name = 'master/product_category/form.html'
    success_url = reverse_lazy('product_category_list')
    
    @permission_required(_ProductCategory_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update ProductCategory'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'ProductCategory', 'url':'product_category_list'},{'name':'Update ProductCategory'}]
        return context
    
class ProductCategoryDeleteView(DeleteView):
    model = ProdutCategory
    template_name = 'master/product_category/confirm_delete.html'
    success_url = reverse_lazy('product_category_list')
    
    @permission_required(_ProductCategory_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)