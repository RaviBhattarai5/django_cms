from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Products
from .forms import ProductForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Product_slug='product'
class ProductListView(ListView):
    model = Products
    template_name = 'master/product/index.html'
    context_object_name = 'products'
    paginate_by = 50
    
    @permission_required(_Product_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Products.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Product'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Product', 'url':'product_list'}]
        context['new_url'] = 'product_create'
        context['can_add'] = has_permission(self.request.user, 'products', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'products', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'products', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class ProductDetailView(DetailView):
    model = Products
    template_name = 'master/product/detail.html'
    
    @permission_required(_Product_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'master/product/form.html'
    success_url = reverse_lazy('product_list')
    
    @permission_required(_Product_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Product'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Product', 'url':'product_list'},{'name':'Create Product', 'url':'product_create'}]
        return context
    
class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'master/product/form.html'
    success_url = reverse_lazy('product_list')
    
    @permission_required(_Product_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        form.instance.updated_date = timezone.now() 
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Product'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Product', 'url':'product_list'},{'name':'Update Product'}]
        return context
    
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'master/product/confirm_delete.html'
    success_url = reverse_lazy('product_list')
    
    @permission_required(_Product_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        product = Products.objects.get(pk=self.kwargs['pk'])
        product.deleted_by = self.request.user  
        product.deleted_date = timezone.now()   
        product.disable = True  
        product.save()
        messages.success(self.request, 'Deleted Successfully')
        return redirect(self.success_url)

