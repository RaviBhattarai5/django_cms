from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductGroupListView.as_view(), name='product_group_list'),
    path('create/', ProductGroupCreateView.as_view(), name='product_group_create'),
    path('<int:pk>/', ProductGroupDetailView.as_view(), name='product_group_detail'),
    path('<int:pk>/update/', ProductGroupUpdateView.as_view(), name='product_group_update'),
    path('<int:pk>/delete/', ProductGroupDeleteView.as_view(), name='product_group_delete'),
]
