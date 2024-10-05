from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import MasterActionTaken
from .forms import MasterActionTakenForm
from django.contrib import messages
from utils.common import arrange_pagination
from permissions.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "master-action-taken"


class MasterActionTakenListView(ListView):
    model = MasterActionTaken
    template_name = "master/master_action_taken/index.html"
    context_object_name = "master_action_takens"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = MasterActionTaken.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "MasterActionTaken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Action Taken", "url": "master_action_taken_list"},
        ]
        context["new_url"] = "master_action_taken_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class MasterActionTakenDetailView(DetailView):
#     model = MasterActionTaken
#     template_name = 'master/master_action_taken/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class MasterActionTakenCreateView(CreateView):
    model = MasterActionTaken
    form_class = MasterActionTakenForm
    template_name = "master/master_action_taken/form.html"
    success_url = reverse_lazy("master_action_taken_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(MasterActionTakenCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Master Action Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Action Taken", "url": "master_action_taken_list"},
            {"name": "Create Master Action Taken", "url": "master_action_taken_create"},
        ]
        return context


class MasterActionTakenUpdateView(UpdateView):
    model = MasterActionTaken
    form_class = MasterActionTakenForm
    template_name = "master/master_action_taken/form.html"
    success_url = reverse_lazy("master_action_taken_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Master Action Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Master Action Taken", "url": "master_action_taken_list"},
            {"name": "Update Master Action Taken"},
        ]
        return context


class MasterActionTakenDeleteView(DeleteView):
    model = MasterActionTaken
    template_name = "master/master_action_taken/confirm_delete.html"
    success_url = reverse_lazy("master_action_taken_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
