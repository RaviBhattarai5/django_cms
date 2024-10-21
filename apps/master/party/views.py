from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Party
from .forms import PartyForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
from django.shortcuts import redirect

MENU_SLUG = "party"


class PartyListView(ListView):
    model = Party
    template_name = "master/party/index.html"
    context_object_name = "parties"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Party.objects.filter(deleted_by = None).order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Party"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Party", "url": "party_list"},
        ]
        context["new_url"] = "party_create"
        context["can_add"] = has_permission(self.request.user, "menu", "Create")
        context["can_edit"] = has_permission(self.request.user, "menu", "Edit")
        context["can_delete"] = has_permission(self.request.user, "menu", "Delete")

        context = arrange_pagination(context)
        return context


# class PartyDetailView(DetailView):
#     model = Party
#     template_name = 'master/party/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class PartyCreateView(CreateView):
    model = Party
    form_class = PartyForm
    template_name = "master/party/form.html"
    success_url = reverse_lazy("party_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(PartyCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        print('create')
        try: 
            form.instance.created_by = self.request.user
            messages.success(self.request, "Created Successfully")
        except Exception as e:
            messages.error(self.request, str(e))
            
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Party"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Party", "url": "party_list"},
            {"name": "Create Party", "url": "party_create"},
        ]
        return context


class PartyUpdateView(UpdateView):
    model = Party
    form_class = PartyForm
    template_name = "master/party/form.html"
    success_url = reverse_lazy("party_list")

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
        context["page_title"] = "Update Party Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "Party", "url": "party_list"},
            {"name": "Update Party"},
        ]
        return context


class PartyDeleteView(DeleteView):
    model = Party
    template_name = "master/party/confirm_delete.html"
    success_url = reverse_lazy("party_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        party = self.get_object()
        party.deleted_by = self.request.user  
        party.deleted_at = timezone.now() 
        party.save()
        messages.success(self.request, 'Deleted successfully')
        return redirect(self.success_url)
