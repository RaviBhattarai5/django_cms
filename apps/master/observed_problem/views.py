from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import ObservedProblem
from .forms import ObservedProblemForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

MENU_SLUG = "observed-problem"


class ObservedProblemListView(ListView):
    model = ObservedProblem
    template_name = "master/observed_problem/index.html"
    context_object_name = "observed_problems"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ObservedProblem.objects.all().order_by("id")
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Observed Problem"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Observed Problem", "url": "observed_problem_list"},
        ]
        context["new_url"] = "observed_problem_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class ObservedProblemDetailView(DetailView):
#     model = ObservedProblem
#     template_name = 'master/observed_problem/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class ObservedProblemCreateView(CreateView):
    model = ObservedProblem
    form_class = ObservedProblemForm
    template_name = "master/observed_problem/form.html"
    success_url = reverse_lazy("observed_problem_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(ObservedProblemCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Observed Problem"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Observed Problem", "url": "observed_problem_list"},
            {"name": "Create Observed Problem", "url": "observed_problem_create"},
        ]
        return context


class ObservedProblemUpdateView(UpdateView):
    model = ObservedProblem
    form_class = ObservedProblemForm
    template_name = "master/observed_problem/form.html"
    success_url = reverse_lazy("observed_problem_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Observed Problem"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Observed Problem", "url": "observed_problem_list"},
            {"name": "Update Observed Problem"},
        ]
        return context


class ObservedProblemDeleteView(DeleteView):
    model = ObservedProblem
    template_name = "master/observed_problem/confirm_delete.html"
    success_url = reverse_lazy("observed_problem_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Deleted Successfully")
        return super().form_valid(form)
