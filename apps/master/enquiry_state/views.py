from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import EnquiryState
from .forms import EnquiryStateForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "enquiry-state"


class EnquiryStateListView(ListView):
    model = EnquiryState
    template_name = "master/enquiry_state/index.html"
    context_object_name = "enquiry_states"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EnquiryState.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "EnquiryState"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry State", "url": "enquiry_state_list"},
        ]
        context["new_url"] = "enquiry_state_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class EnquiryStateDetailView(DetailView):
#     model = EnquiryState
#     template_name = 'master/enquiry_state/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class EnquiryStateCreateView(CreateView):
    model = EnquiryState
    form_class = EnquiryStateForm
    template_name = "master/enquiry_state/form.html"
    success_url = reverse_lazy("enquiry_state_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(EnquiryStateCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Enquiry State"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry State", "url": "enquiry_state_list"},
            {"name": "Create Enquiry State", "url": "enquiry_state_create"},
        ]
        return context


class EnquiryStateUpdateView(UpdateView):
    model = EnquiryState
    form_class = EnquiryStateForm
    template_name = "master/enquiry_state/form.html"
    success_url = reverse_lazy("enquiry_state_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Enquiry State"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Enquiry State", "url": "enquiry_state_list"},
            {"name": "Update Enquiry State"},
        ]
        return context


class EnquiryStateDeleteView(DeleteView):
    model = EnquiryState
    template_name = "master/enquiry_state/confirm_delete.html"
    success_url = reverse_lazy("enquiry_state_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
