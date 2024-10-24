from django.urls import path
from .views import *

urlpatterns = [
    path('',FmsStatusListView.as_view(), name='fms_status_list'),
    path('create/', FmsStatusCreateView.as_view(), name='fms_status_create'),
    # path('<int:pk>/', FmsStatusDetailView.as_view(), name='fms_status_detail'),
    path('<int:pk>/update/', FmsStatusUpdateView.as_view(), name='fms_status_update'),
    path('<int:pk>/delete/', FmsStatusDeleteView.as_view(), name='fms_status_delete'),
]