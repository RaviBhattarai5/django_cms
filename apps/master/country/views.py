from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Country
from .form import CountryForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "master_country"


class CountryListView(ListView):
    model = Country
    template_name = "master/country/index.html"
    context_object_name = "master_country"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Country.objects.all().order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(title__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Country"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Country", "url": "country_list"},
        ]
        context["new_url"] = "country_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class CountryDetailView(DetailView):
#     model = Country
#     template_name = 'master/country/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = "master/country/form.html"
    success_url = reverse_lazy("")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(CountryCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Country"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Action Taken", "url": "country_list"},
            {"name": "Create Country", "url": "country_create"},
        ]
        return context


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = "master/country/form.html"
    success_url = reverse_lazy("country_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Country Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Action Taken", "url": "country_list"},
            {"name": "Update Master Action Taken"},
        ]
        return context


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "master/country/confirm_delete.html"
    success_url = reverse_lazy("country_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
