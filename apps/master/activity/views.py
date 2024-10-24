from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Activity
from .forms import ActivityForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "activity"


class ActivityListView(ListView):
    model = Activity
    template_name = "master/activity/index.html"
    context_object_name = "activities"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Activity.objects.all().order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(activity_name__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Activity", "url": "activity_list"},
        ]
        context["new_url"] = "activity_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class ActivityDetailView(DetailView):
#     model = Activity
#     template_name = 'master/activity/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "master/activity/form.html"
    success_url = reverse_lazy("activity_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(ActivityCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Activity", "url": "activity_list"},
            {"name": "Create Activity", "url": "activity_create"},
        ]
        return context


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = "master/activity/form.html"
    success_url = reverse_lazy("activity_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Activity"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Activity", "url": "activity_list"},
            {"name": "Update Activity"},
        ]
        return context


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = "master/activity/confirm_delete.html"
    success_url = reverse_lazy("activity_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
