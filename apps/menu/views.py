from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Menu
from .forms import MenuForm
from django.contrib import messages

class MenuListView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    context_object_name = 'menus'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Menu.objects.select_related('parent').all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'menu_list'}]
        context['new_url'] = 'menu_create'
        
        paginator = context['paginator']
        page_obj = context['page_obj']
        current_page = page_obj.number
        total_pages = paginator.num_pages
        start_page = max(current_page - 1, 1)
        end_page = min(current_page + 1, total_pages)
        if current_page == 1:
            end_page = min(3, total_pages)
        elif current_page == total_pages:
            start_page = max(total_pages - 2, 1)
        context['page_range'] = range(start_page, end_page + 1)
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