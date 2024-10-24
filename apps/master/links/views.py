from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Link
from .forms import LinkForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.utils import timezone

_Menu_Slug='links'
class LinkListView(ListView):
    model = Link
    template_name = 'master/links/index.html'
    context_object_name = 'links'
    paginate_by = 50
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Link.objects.all().order_by('id')
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Links'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'links', 'url':'link_list'}]
        context['new_url'] = 'link_create'
        context['can_add'] = has_permission(self.request.user, 'links', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'links', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'links', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class LinkDetailView(DetailView):
    model = Link
    template_name = 'master/links/detail.html'
    
    @permission_required(_Menu_Slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'master/links/form.html'
    success_url = reverse_lazy('link_list')
    
    @permission_required(_Menu_Slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(LinkCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        form.instance.created_date = timezone.now()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Links'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'links', 'url':'link_list'},{'name':'Create Links', 'url':'link_create'}]
        return context
    
class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = 'master/links/form.html'
    success_url = reverse_lazy('link_list')
    
    @permission_required(_Menu_Slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        form.instance.updated_date = timezone.now() 
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Links'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Links', 'url':'link_list'},{'name':'Update Links'}]
        return context
    
class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'master/links/confirm_delete.html'
    success_url = reverse_lazy('link_list')
    
    @permission_required(_Menu_Slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     links = Link.objects.get(pk=self.kwargs['pk'])
    #     links.deleted_by = self.request.user  
    #     links.deleted_date = timezone.now()   
    #     links.disable = True  
    #     links.save()
    #     messages.success(self.request, 'Deleted Successfully')
    #     return redirect(self.success_url)
    
    def form_valid(self, form):
        messages.success(self.request, "Delete Successfully")
        return super().form_valid(form)
    

