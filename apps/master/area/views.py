from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Area
from .forms import AreaForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
from django.shortcuts import redirect

MENU_SLUG = "area"


class AreaListView(ListView):
    model = Area
    template_name = "master/area/index.html"
    context_object_name = "areas"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Area.objects.filter(deleted_by = None).order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Area"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Area", "url": "area_list"},
        ]
        context["new_url"] = "area_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class AreaDetailView(DetailView):
#     model = Area
#     template_name = 'master/area/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = "master/area/form.html"
    success_url = reverse_lazy("area_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(AreaCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Area"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Area", "url": "area_list"},
            {"name": "Create Area", "url": "area_create"},
        ]
        return context


class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "master/area/form.html"
    success_url = reverse_lazy("area_list")

    @permission_required(MENU_SLUG, "Edit")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.updated_at = timezone.now()
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Area Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Area", "url": "area_list"},
            {"name": "Update Area"},
        ]
        return context


class AreaDeleteView(DeleteView):
    model = Area
    template_name = "master/area/confirm_delete.html"
    success_url = reverse_lazy("area_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        area = self.get_object()
        area.deleted_by = self.request.user  
        area.deleted_at = timezone.now() 
        area.save()
        messages.success(self.request, 'Deleted successfully')
        return redirect(self.success_url)
