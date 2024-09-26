from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
from utils.common import arrange_pagination
from apps.users.models import UserRole

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = User.objects.exclude(username__icontains='superadmin').prefetch_related('userrole_set__role').all().order_by('id')
        username = self.request.GET.get('username')
        if username:
            queryset = queryset.filter(username__icontains=username) 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'User'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'User', 'url':'user_list'}]
        context['new_url'] = 'user_create'
        
        context = arrange_pagination(context)
        return context
    
class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'
    
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('user_list')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Hash the password
        user.is_active = True  # Ensure the user is active
        user.save()
        messages.success(self.request, 'Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create User'
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': 'dashboard'},
            {'name': 'User', 'url': 'user_list'},
            {'name': 'Create User', 'url': 'user_create'}
        ]
        return context
    
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('user_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.get_object()
        return kwargs
    
    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data['password']:
            user.set_password(form.cleaned_data['password'])
        user.save()
        
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update User'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'User', 'url':'user_list'},{'name':'Update User'}]
        context['is_update'] = True
        return context
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/confirm_delete.html'
    success_url = reverse_lazy('user_list')
    def form_valid(self, form):
        messages.success(self.request, 'Deleted Successfully')
        return super().form_valid(form)
