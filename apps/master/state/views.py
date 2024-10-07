from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import State
from .form import StateForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
_State_slug='state'
class StateListView(ListView):
    model = State
    template_name = 'master/state/index.html'
    context_object_name = 'states'
    paginate_by = 50
    
    @permission_required(_State_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = State.objects.all().order_by('id')
        title = self.request.GET.get('stateName')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'State'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'State', 'url':'state_list'}]
        context['new_url'] = 'state_create'
        context['can_add'] = has_permission(self.request.user, 'state', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'state', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'state', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class StateDetailView(DetailView):
    model = State
    template_name = 'master/state/detail.html'
    
    @permission_required(_State_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    template_name = 'master/state/form.html'
    success_url = reverse_lazy('state_list')
    
    @permission_required(_State_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(StateCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create State'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'State', 'url':'state_list'},{'name':'Create State', 'url':'state_create'}]
        return context
    
class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    template_name = 'master/state/form.html'
    success_url = reverse_lazy('state_list')
    
    @permission_required(_State_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update State'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'State', 'url':'state_list'},{'name':'Update State'}]
        return context
    
class StateDeleteView(DeleteView):
    model = State
    template_name = 'master/state/confirm_delete.html'
    success_url = reverse_lazy('state_list')
    
    @permission_required(_State_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)