from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EccTransaction
from .forms import EccTransactionForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

_menu_slug=''
class TcpEccChargeListView(ListView):
    model = EccTransaction
    template_name = 'master/tpl_ecc_charge/index.html'
    context_object_name = 'tpl_ecc_charges'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'TPL ECC Charge'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'TPL ECC Charge', 'url':'tpl_ecc_charge_list'}]
        context['new_url'] = 'tpl_ecc_charge_create'
        context['can_add'] = has_permission(self.request.user, 'tpl_ecc_charge', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'tpl_ecc_charge', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'tpl_ecc_charge', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class TcpEccChargeDetailView(DetailView):
    model = EccTransaction
    template_name = 'master/tpl_ecc_charge/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class TcpEccChargeCreateView(CreateView):
    model = EccTransaction
    form_class = EccTransactionForm
    template_name = 'master/tpl_ecc_charge/form.html'
    success_url = reverse_lazy('tpl_ecc_charge_list')
    
    @permission_required(_menu_slug,'Create')
    def dispatch(self, *args, **kwargs):
        return super(TcpEccChargeCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create TPL ECC Charge'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'TPL ECC Charge', 'url':'tpl_ecc_charge_list'},{'name':'Create TPL ECC Charge', 'url':'tpl_ecc_charge_create'}]
        return context
    
class TcpEccChargeUpdateView(UpdateView):
    model = EccTransaction
    form_class = EccTransactionForm
    template_name = 'master/tpl_ecc_charge/form.html'
    success_url = reverse_lazy('tpl_ecc_charge_list')
    
    @permission_required(_menu_slug,'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update TPL ECC Charge'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'TPL ECC Charge', 'url':'tpl_ecc_charge_list'},{'name':'Update TPL ECC Charge'}]
        return context
    

class TcpEccChargeDeleteView(DeleteView):
    model = EccTransaction
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('tpl_ecc_charge_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)