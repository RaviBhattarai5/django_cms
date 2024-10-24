from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import ECCMaster
from .forms import ECCMasterForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "ecc"

class ECCListView(ListView):
    model = ECCMaster
    template_name = "master/ecc/index.html"
    context_object_name = "eccs"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ECCMaster.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "ECC Master"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "ECC Master", "url": "ecc_list"},
        ]
        context["new_url"] = "ecc_create"
        context["can_add"] = has_permission(self.request.user, "ecc", "Create")
        context["can_edit"] = has_permission(self.request.user, "ecc", "Edit")
        context["can_delete"] = has_permission(self.request.user, "ecc", "Delete")

        context = arrange_pagination(context)
        return context


# class ECCDetailView(DetailView):
#     model = ECCMaster
#     template_name = 'master/ecc/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class ECCCreateView(CreateView):
    model = ECCMaster
    form_class = ECCMasterForm
    template_name = "master/ecc/form.html"
    success_url = reverse_lazy("ecc_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(ECCCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create ECC Master"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "ECC Master", "url": "ecc_list"},
            {"name": "Create Ecc Master", "url": "ecc_create"},
        ]
        return context


class ECCUpdateView(UpdateView):
    model = ECCMaster
    form_class = ECCMasterForm
    template_name = "master/ecc/form.html"
    success_url = reverse_lazy("ecc_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update ECC Master"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "ECC Master", "url": "ecc_list"},
            {"name": "Update ECC Master"},
        ]
        return context


class ECCDeleteView(DeleteView):
    model = ECCMaster
    template_name = "master/ecc/confirm_delete.html"
    success_url = reverse_lazy("ecc_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
