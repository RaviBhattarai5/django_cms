from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import City
from .forms import CityForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
from django.shortcuts import redirect

MENU_SLUG = "city"


class CityListView(ListView):
    model = City
    template_name = "master/city/index.html"
    context_object_name = "cities"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = City.objects.filter(deleted_by = None).order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(title__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "City"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "City", "url": "city_list"},
        ]
        context["new_url"] = "city_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class CityDetailView(DetailView):
#     model = City
#     template_name = 'master/city/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = "master/city/form.html"
    success_url = reverse_lazy("city_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(CityCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create City"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "City", "url": "city_list"},
            {"name": "Create City", "url": "city_create"},
        ]
        return context


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = "master/city/form.html"
    success_url = reverse_lazy("city_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.updated_at = timezone.now()
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update City Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "City", "url": "city_list"},
            {"name": "Update City"},
        ]
        return context


class CityDeleteView(DeleteView):
    model = City
    template_name = "master/city/confirm_delete.html"
    success_url = reverse_lazy("city_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        city = self.get_object()
        city.deleted_by = self.request.user  
        city.deleted_at = timezone.now() 
        city.save()
        messages.success(self.request, 'Deleted successfully')
        return redirect(self.success_url)
