from django.urls import path
from apps.administrator.permission_type.views import PermissionTypeListView, PermissionTypeDetailView, PermissionTypeCreateView, PermissionTypeUpdateView, PermissionTypeDeleteView
urlpatterns = [
    path('', PermissionTypeListView.as_view(), name='permission_type_list'),
    path('create/', PermissionTypeCreateView.as_view(), name='permission_type_create'),
    path('<int:pk>/', PermissionTypeDetailView.as_view(), name='permission_type_detail'),
    path('<int:pk>/update/', PermissionTypeUpdateView.as_view(), name='permission_type_update'),
    path('<int:pk>/delete/', PermissionTypeDeleteView.as_view(), name='permission_type_delete'),
]
