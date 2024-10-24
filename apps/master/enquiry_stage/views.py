from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import EnquiryStage
from .forms import EnquiryStageForm
from django.contrib import messages
from utils.common import arrange_pagination
from utils.permissions import has_permission
from decorators.decorators import permission_required

from django.utils import timezone
from django.shortcuts import redirect

MENU_SLUG = "enquiry-stage"


class EnquiryStageListView(ListView):
    model = EnquiryStage
    template_name = "master/enquiry_stage/index.html"
    context_object_name = "enquire_stages"
    paginate_by = 50

    @permission_required(MENU_SLUG, "Browse")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = EnquiryStage.objects.filter(deleted_by = None).order_by("id")
    #     name = self.request.GET.get("name")
    #     if name:
    #         queryset = queryset.filter(title__icontains=name)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "EnquiryStage"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "EnquiryStage", "url": "enquiry_stage_list"},
        ]
        context["new_url"] = "enquiry_stage_create"
        context["can_add"] = has_permission(self.request.user, "enquiry_stage", "Create")
        context["can_edit"] = has_permission(self.request.user, "enquiry_stage", "Edit")
        context["can_delete"] = has_permission(self.request.user, "enquiry_stage", "Delete")

        context = arrange_pagination(context)
        return context


# class EnquiryStageDetailView(DetailView):
#     model = EnquiryStage
#     template_name = 'master/enquiry_stage/detail.html'

#     @permission_required(MENU_SLUG ,'Browse')
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)


class EnquiryStageCreateView(CreateView):
    model = EnquiryStage
    form_class = EnquiryStageForm
    template_name = "master/enquiry_stage/form.html"
    success_url = reverse_lazy("enquiry_stage_list")

    @permission_required(MENU_SLUG, "Create")
    def dispatch(self, *args, **kwargs):
        return super(EnquiryStageCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Created Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create EnquiryStage"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "EnquiryStage", "url": "enquiry_stage_list"},
            {"name": "Create EnquiryStage", "url": "city_create"},
        ]
        return context


class EnquiryStageUpdateView(UpdateView):
    model = EnquiryStage
    form_class = EnquiryStageForm
    template_name = "master/enquiry_stage/form.html"
    success_url = reverse_lazy("enquiry_stage_list")

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
        context["page_title"] = "Update EnquiryStage Taken"
        context["breadcrumbs"] = [
            {"name": "Dashboard", "url": "dashboard"},
            {"name": "EnquiryStage", "url": "enquiry_stage_list"},
            {"name": "Update EnquiryStage"},
        ]
        return context


class EnquiryStageDeleteView(DeleteView):
    model = EnquiryStage
    template_name = "master/enquiry_stage/confirm_delete.html"
    success_url = reverse_lazy("enquiry_stage_list")

    @permission_required(MENU_SLUG, "Delete")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     city = self.get_object()
    #     city.deleted_by = self.request.user  
    #     city.deleted_at = timezone.now() 
    #     city.save()
    #     messages.success(self.request, 'Deleted successfully')
    #     return redirect(self.success_url)


    def form_valid(self, form):
        messages.success(self.request, 'Delete Successfully ')
        return super().form_valid(form)
    