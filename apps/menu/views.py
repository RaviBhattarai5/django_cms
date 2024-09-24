from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Menu
from .forms import MenuForm
from django.contrib import messages
from utils.common import arrange_pagination

class MenuListView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    context_object_name = 'items'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = Menu.objects.select_related('parent').all()
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'}]
        context['new_url'] = 'menu_create'
        
        context = arrange_pagination(context)
        return context
    
class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/detail.html'
    
class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parents'] = Menu.objects.all()
        context['page_title'] = 'Create Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'},{'name':'Create Menu', 'url':'menu_create'}]
        return context
    
class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/form.html'
    success_url = reverse_lazy('menu_list')
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('menu_list')
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)