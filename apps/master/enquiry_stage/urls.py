from django.urls import path
from .views import *

urlpatterns = [
    path("", EnquiryStageListView.as_view(), name="enquiry_stage_list"),
    path("create/", EnquiryStageCreateView.as_view(), name="enquiry_stage_create"),
    # path('<int:pk>/', EnquiryStageDetailView.as_view(), name='enquiry_stage_detail'),
    path("<int:pk>/update/", EnquiryStageUpdateView.as_view(), name="enquiry_stage_update"),
    path("<int:pk>/delete/", EnquiryStageDeleteView.as_view(), name="enquiry_stage_delete"),
]
