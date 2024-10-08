from django.urls import path
from .views import *
urlpatterns = [
    path('', ProductCategoryListView.as_view(), name='product_category_list'),
    path('create/', ProductCategoryCreateView.as_view(), name='product_category_create'),
    path('<int:pk>/', ProductCategoryDetailView.as_view(), name='product_category_detail'),
    path('<int:pk>/update/', ProductCategoryUpdateView.as_view(), name='product_category_update'),
    path('<int:pk>/delete/', ProductCategoryDeleteView.as_view(), name='product_category_delete'),
]
