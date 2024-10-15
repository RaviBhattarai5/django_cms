from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]