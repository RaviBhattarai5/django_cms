from django.urls import path
from .views import *

urlpatterns = [
    path('',FmsStageListView.as_view(), name='fms_stage_list'),
    path('create/', FmsStageCreateView.as_view(), name='fms_stage_create'),
    # path('<int:pk>/', FmsStageDetailView.as_view(), name='fms_stage_detail'),
    path('<int:pk>/update/', FmsStageUpdateView.as_view(), name='fms_stage_update'),
    path('<int:pk>/delete/', FmsStageDeleteView.as_view(), name='fms_stage_delete'),
]