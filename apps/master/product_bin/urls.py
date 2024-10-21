from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductBinListView.as_view(), name='product_bin_list'),
    path('create/', ProductBinCreateView.as_view(), name='product_bin_create'),
    path('<int:pk>/', ProductBinDetailView.as_view(), name='product_bin_detail'),
    path('<int:pk>/update/', ProductBinUpdateView.as_view(), name='product_bin_update'),
    path('<int:pk>/delete/', ProductBinDeleteView.as_view(), name='product_bin_delete'),
]
