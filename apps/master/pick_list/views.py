from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PickList
from .forms import PickListForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_menu_slug='pick_list'
class PickListView(ListView):
    model = PickList
    template_name = 'master/pick_list/index.html'
    context_object_name = 'picklists'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = PickList.objects.all().order_by('id')
        title = self.request.GET.get('pick_list_name')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pick List'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Pick List', 'url':'pick_list'}]
        context['new_url'] = 'pick_list_create'
        context['can_add'] = has_permission(self.request.user, 'pick_list', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'pick_list', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'pick_list', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
#! DETAILVIEW
class PickListDetailView(DetailView):
    model = PickList
    template_name = 'master/pick_list/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
#! CreateView
class PickListCreateView(CreateView):
    model = PickList
    form_class = PickListForm
    template_name = 'master/pick_list/forms.html'
    success_url = reverse_lazy('pick_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(PickListCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pick List'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Pick List', 'url':'pick_list'},{'name':'Create Pick List', 'url':'pick_list_create'}]
        return context
    
class PickListUpdateView(UpdateView):
    model = PickList
    form_class = PickListForm
    template_name = 'master/pick_list/forms.html'
    success_url = reverse_lazy('pick_list')
    
    @permission_required(_menu_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form): 
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pick List'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Menu', 'url':'pick_list'},{'name':'Update PickList',  'url':'pick_list_update'}]
        return context
    
class PickListDeleteView(DeleteView):
    model = PickList
    success_url = reverse_lazy('pick_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'delete Succesfully')
        return super().form_valid(form)
    
