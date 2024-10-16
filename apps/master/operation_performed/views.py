from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import OperationPerformed
from .forms import OperationPerformedForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "operation-performed"


class OperationPerformedListView(ListView):
    model = OperationPerformed
    template_name = "master/operation_performed/index.html"
    context_object_name = "operation_performeds"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = OperationPerformed.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Operation Performed"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Operation Performed", "url": "operation_performed_list"},
        ]
        context["new_url"] = "operation_performed_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class OperationPerformedDetailView(DetailView):
#     model = OperationPerformed
#     template_name = 'master/operation_performed/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class OperationPerformedCreateView(CreateView):
    model = OperationPerformed
    form_class = OperationPerformedForm
    template_name = "master/operation_performed/form.html"
    success_url = reverse_lazy("operation_performed_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(OperationPerformedCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Operation Performed"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Operation Performed", "url": "operation_performed_list"},
            {"name": "Create Operation Performed", "url": "operation_performed_create"},
        ]
        return context


class OperationPerformedUpdateView(UpdateView):
    model = OperationPerformed
    form_class = OperationPerformedForm
    template_name = "master/operation_performed/form.html"
    success_url = reverse_lazy("operation_performed_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Operation Performed"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Operation Performed", "url": "operation_performed_list"},
            {"name": "Update Operation Performed"},
        ]
        return context


class OperationPerformedDeleteView(DeleteView):
    model = OperationPerformed
    template_name = "master/operation_performed/confirm_delete.html"
    success_url = reverse_lazy("operation_performed_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
