from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import PlanningActivityCategory
from .forms import PlanningActivityCategoryForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "planning-activity-category"


class PlanningActivityCategoryListView(ListView):
    model = PlanningActivityCategory
    template_name = "master/planning_activity_category/index.html"
    context_object_name = "planning_activity_categorys"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = PlanningActivityCategory.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Planning Activity Category"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity Category", "url": "planning_activity_category_list"},
        ]
        context["new_url"] = "planning_activity_category_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class PlanningActivityCategoryDetailView(DetailView):
#     model = PlanningActivityCategory
#     template_name = 'master/planning_activity_category/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class PlanningActivityCategoryCreateView(CreateView):
    model = PlanningActivityCategory
    form_class = PlanningActivityCategoryForm
    template_name = "master/planning_activity_category/form.html"
    success_url = reverse_lazy("planning_activity_category_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(PlanningActivityCategoryCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Planning Activity Category"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity Category", "url": "planning_activity_category_list"},
            {"name": "Create Planning Activity Category", "url": "planning_activity_category_create"},
        ]
        return context


class PlanningActivityCategoryUpdateView(UpdateView):
    model = PlanningActivityCategory
    form_class = PlanningActivityCategoryForm
    template_name = "master/planning_activity_category/form.html"
    success_url = reverse_lazy("planning_activity_category_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Planning Activity Category"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Planning Activity Category", "url": "planning_activity_category_list"},
            {"name": "Update Planning Activity Category"},
        ]
        return context


class PlanningActivityCategoryDeleteView(DeleteView):
    model = PlanningActivityCategory
    template_name = "master/planning_activity_category/confirm_delete.html"
    success_url = reverse_lazy("planning_activity_category_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
