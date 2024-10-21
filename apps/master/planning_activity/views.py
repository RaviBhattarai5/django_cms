from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import PlanningActivity
from .forms import PlanningActivityForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "planning-activity"


class PlanningActivityListView(ListView):
    model = PlanningActivity
    template_name = "master/planning_activity/index.html"
    context_object_name = "planning_activities"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = PlanningActivity.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Planning Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity", "url": "planning_activity_list"},
        ]
        context["new_url"] = "planning_activity_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class PlanningActivityDetailView(DetailView):
#     model = PlanningActivity
#     template_name = 'master/planning_activity/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class PlanningActivityCreateView(CreateView):
    model = PlanningActivity
    form_class = PlanningActivityForm
    template_name = "master/planning_activity/form.html"
    success_url = reverse_lazy("planning_activity_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(PlanningActivityCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Planning Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity", "url": "planning_activity_list"},
            {"name": "Create Planning Activity", "url": "planning_activity_create"},
        ]
        return context


class PlanningActivityUpdateView(UpdateView):
    model = PlanningActivity
    form_class = PlanningActivityForm
    template_name = "master/planning_activity/form.html"
    success_url = reverse_lazy("planning_activity_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Planning Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity", "url": "planning_activity_list"},
            {"name": "Update Planning Activity"},
        ]
        return context


class PlanningActivityDeleteView(DeleteView):
    model = PlanningActivity
    template_name = "master/planning_activity/confirm_delete.html"
    success_url = reverse_lazy("planning_activity_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
