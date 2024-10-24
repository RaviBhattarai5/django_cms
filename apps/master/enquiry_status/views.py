from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import EnquiryStatus
from .forms import EnquiryStatusForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "enquiry-status"


class EnquiryStatusListView(ListView):
    model = EnquiryStatus
    template_name = "master/enquiry_status/index.html"
    context_object_name = "enquiry_status"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EnquiryStatus.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Enquiry Status"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry Status", "url": "enquire_status_list"},
        ]
        context["new_url"] = "enquire_status_create"
        context["can_add"] = has_permission(self.request.user, "enquire_status", "Create")
        context["can_edit"] = has_permission(self.request.user, "enquire_status", "Edit")
        context["can_delete"] = has_permission(self.request.user, "enquire_status", "Delete")

        context = arrange_pagination(context)
        return context


# class EnquiryStatusDetailView(DetailView):
#     model = EnquiryStatus
#     template_name = 'master/enquiry_status/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class EnquiryStatusCreateView(CreateView):
    model = EnquiryStatus
    form_class = EnquiryStatusForm
    template_name = "master/enquiry_status/form.html"
    success_url = reverse_lazy("enquire_status_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(EnquiryStatusCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Enquiry Status"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry Status", "url": "enquire_status_list"},
            {"name": "Create Enquiry Status", "url": "enquire_status_create"},
        ]
        return context


class EnquiryStatusUpdateView(UpdateView):
    model = EnquiryStatus
    form_class = EnquiryStatusForm
    template_name = "master/enquiry_status/form.html"
    success_url = reverse_lazy("enquire_status_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Enquiry Status"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry Status", "url": "enquire_status_list"},
            {"name": "Update Enquiry Status"},
        ]
        return context


class EnquiryStatusDeleteView(DeleteView):
    model = EnquiryStatus
    template_name = "master/enquiry_status/confirm_delete.html"
    success_url = reverse_lazy("enquire_status_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
