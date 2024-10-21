# views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserForm
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required
_users_slug='users'
class UserListView(ListView):
    model = User
    template_name = 'administrator/users/index.html'
    context_object_name = 'users'
    paginate_by = 50
  
    @permission_required(_users_slug, 'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.exclude(username__icontains='superadmin').all().order_by('id')
        username = self.request.GET.get('username')
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'User Management'
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': 'dashboard'},
            {'name': 'Users', 'url': 'user_list'}
        ]
        context['new_url'] = 'user_create'
        context['can_add'] = has_permission(self.request.user, 'users', 'Create')
        context['can_edit'] = has_permission(self.request.user, 'users', 'Edit')
        context['can_delete'] = has_permission(self.request.user, 'users', 'Delete')
        context = arrange_pagination(context)
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'administrator/users/detail.html'

    @permission_required(_users_slug, 'Browse')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'administrator/users/form.html'
    success_url = reverse_lazy('user_list')

    @permission_required(_users_slug, 'Create')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Hash the password
        user.is_active = True  # Ensure the user is active
        user.save()
        messages.success(self.request, 'User created successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create User'
        context['breadcrumbs'] = [
            {'name': 'Dashboard', 'url': 'dashboard'},
            {'name': 'Users', 'url': 'user_list'},
            {'name': 'Create User', 'url': 'user_create'}
        ]
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'administrator/users/form.html'
    success_url = reverse_lazy('user_list')

    @permission_required(_users_slug, 'Edit')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data['password']:
            user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'User updated successfully.')
        return super().form_valid(form)

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'Update User'
    context['breadcrumbs'] = [
        {'name': 'Dashboard', 'url': reverse('dashboard')},
        {'name': 'Users', 'url': reverse('user_list')},  # use named pattern instead of '/users/'
        {'name': 'Update User', 'url': reverse('user_update', kwargs={'pk': self.object.pk})}  # provide `pk`
    ]
    context['is_update'] = True
    return context



class UserDeleteView(DeleteView):
    model = User
    template_name = 'administrator/users/confirm_delete.html'
    success_url = reverse_lazy('user_list')

    @permission_required('users', 'Delete')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'User deleted successfully.')
        return super().form_valid(form)
