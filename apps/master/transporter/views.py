from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
from django.forms import modelformset_factory
from django.utils import timezone
from django.db import transaction

from .models import Transporter
from .forms import TransporterForm, EccTransactionForm
from apps.master.tpl_ecc_charge.models import EccTransaction

_menu_slug = 'transporter'
_menu_slug='transporter'
class TransporterListView(ListView):
    model = Transporter
    template_name = 'master/transporter/index.html'
    context_object_name = 'transporters'
    paginate_by = 50
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Transporter.objects.all().order_by('id')
        title = self.request.GET.get('transporter_name')
        if title:
            queryset = queryset.filter(title__icontains=title) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Transporter'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter', 'url':'transporter_list'}]
        context['new_url'] = 'transporter_create'
        context['can_add'] = has_permission(self.request.user, 'group', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'group', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'group', 'Delete')
        
        context = arrange_pagination(context)
        return context
    
class TransporterDetailView(DetailView):
    model = Transporter
    template_name = 'master/transporter/detail.html'
    
    @permission_required(_menu_slug,'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    
# class TransporterCreateView(CreateView):
#     model = Transporter
#     form_class = TransporterForm
#     template_name = 'master/transporter/forms.html'
#     success_url = reverse_lazy('transporter_list')
    
#     @permission_required(_menu_slug,'Create')
#     def dispatch(self, *args, **kwargs):
#         return super(TransporterCreateView, self).dispatch(*args, **kwargs)
    
#     def form_valid(self, form):
#         form.instance.createdBy = self.request.user  
#         form.instance.createdDate = timezone.now()  
#         messages.success(self.request, 'Created Successfully')

#         return super().form_valid(form)
    
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Groupe '
#         context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Transporter', 'url':'transporter_list'},{'name':'Create Group', 'url':'transporter_create'}]
#         return context


class TransporterCreateView(View):
    model = Transporter
    form_class = TransporterForm
    template_name = 'master/transporter/forms.html'
    success_url = reverse_lazy('transporter_list')
    
    def get(self, request, *args, **kwargs):
        transporter_form = self.form_class()
        EccTransactionFormSet = modelformset_factory(EccTransaction, form=EccTransactionForm, extra=3)
        formset = EccTransactionFormSet(queryset=EccTransaction.objects.none())
        
        return render(request, self.template_name, {
            'transporter_form': transporter_form,
            'formset': formset,
            'page_title': 'Create Transporter',
            'breadcrumbs': [
                {'name': 'Dashboard', 'url': 'dashboard'},
                {'name': 'Transporter', 'url': 'transporter_list'},
                {'name': 'Create Transporter', 'url': 'transporter_create'}
            ]
        })

    def post(self, request, *args, **kwargs):
        transporter_form = self.form_class(request.POST)
        EccTransactionFormSet = modelformset_factory(EccTransaction, form=EccTransactionForm, extra=3)
        formset = EccTransactionFormSet(request.POST)

        if transporter_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    transporter = transporter_form.save(commit=False)
                    transporter.created_by = request.user
                    transporter.created_date = timezone.now()
                    transporter.save()

                    # Save the EccTransaction formset
                    ecc_transactions = formset.save(commit=False)
                    for ecc_transaction in ecc_transactions:
                        ecc_transaction.transporter = transporter
                        ecc_transaction.created_by = request.user
                        ecc_transaction.save()

                messages.success(request, 'Transporter and ECC Transactions created successfully!')
                return redirect(self.success_url)
            except Exception as e:
                return render(request, self.template_name, {
                    'transporter_form': transporter_form,
                    'formset': formset,
                    'error': f'An error occurred: {str(e)}',
                })

        return render(request, self.template_name, {
            'transporter_form': transporter_form,
            'formset': formset,
            'error': 'Please correct the errors below.',
        })
    


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
# from .models import Transporter, EccTransaction
from .forms import TransporterForm, EccTransactionForm
from django.urls import reverse
from django.forms import modelformset_factory
from django.db import transaction

# Ensure you have the correct permission slug defined in _menu_slug
@permission_required(_menu_slug, 'Edit', raise_exception=True)
def transporter_update_view(request, pk):
    # Get the Transporter instance by primary key
    transporter = get_object_or_404(Transporter, pk=pk)
    
    # Set up a ModelFormSet for EccTransaction; set extra=0 so no additional forms are created
    EccTransactionFormSet = modelformset_factory(EccTransaction, form=EccTransactionForm, extra=3)

    if request.method == 'POST':
        # Process the submitted forms
        transporter_form = TransporterForm(request.POST, instance=transporter)
        formset = EccTransactionFormSet(request.POST, queryset=EccTransaction.objects.filter(transporter=transporter))

        # Validate both the Transporter form and the EccTransaction formset
        if transporter_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    # Save Transporter
                    transporter_form.save()
                    
                    # Save EccTransaction instances
                    ecc_transactions = formset.save(commit=False)
                    for ecc_transaction in ecc_transactions:
                        ecc_transaction.transporter = transporter  # Associate with the current transporter
                        ecc_transaction.save()

                # Show success message
                messages.success(request, 'Transporter and ECC Transactions updated successfully!')
                return redirect('transporter_list')  # Redirect to list page or any other view
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            # Print errors for debugging
            print("Formset errors:", formset.errors)
    else:
        # Display the forms for the initial GET request
        transporter_form = TransporterForm(instance=transporter)
        formset = EccTransactionFormSet(queryset=EccTransaction.objects.filter(transporter=transporter))

    # Render the forms in the template
    return render(request, 'master/transporter/forms.html', {
        'transporter_form': transporter_form,
        'formset': formset,
        'page_title': 'Update Transporter',
        'breadcrumbs': [
            {'name': 'Update Transporter', 'url': reverse('transporter_update', kwargs={'pk': transporter.pk})},
        ],
    })

class TransporterDeleteView(DeleteView):
    model = Transporter
    template_name = 'menu/confirm_delete.html'
    success_url = reverse_lazy('transporter_list')
    
    @permission_required(_menu_slug,'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Successfully Deleted")
        return super().form_valid(form)
    
