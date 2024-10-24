from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Menu
from .forms import MenuForm
from django.contrib import messages
from utils.common import arrange_pagination
from permissions.permissions import has_permission
from decorators.decorators import permission_required

class MenuListView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    context_object_name = 'menus'
    paginate_by = 50
    
    @permission_required('menu','Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Menu.objects.select_related('parent').all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'}]
        context['new_url'] = 'menu_create'
        context['can_add'] = has_permission(self.request.user, 'menu', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'menu', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'menu', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/detail.html'
    
    @permission_required('menu','Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu_list')
    
    @permission_required('menu','Create')
    def dispatch(self, *args, **kwargs):
        return super(MenuCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'},{'name':'Create Menu', 'url':'menu_create'}]
        return context
    
class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu_list')
    
    @permission_required('menu','Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'},{'name':'Update Menu'}]
        return context
    
class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('menu_list')
    
    @permission_required('menu','Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)