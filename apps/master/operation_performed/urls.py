from django.urls import path
from .views import *
urlpatterns = [
    path('', OperationPerformedListView.as_view(), name='operation_performed_list'),
    path('create/', OperationPerformedCreateView.as_view(), name='operation_performed_create'),
    # path('<int:pk>/', OperationPerformedDetailView.as_view(), name='operation_performed_detail'),
    path('<int:pk>/update/', OperationPerformedUpdateView.as_view(), name='operation_performed_update'),
    path('<int:pk>/delete/', OperationPerformedDeleteView.as_view(), name='operation_performed_delete'),
]
