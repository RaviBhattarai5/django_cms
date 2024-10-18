from django.urls import path
from .views import *

urlpatterns = [
    path('',FmsContactListView.as_view(), name='fms_contact_list'),
    path('create/', FmsContactCreateView.as_view(), name='fms_contact_create'),
    # path('<int:pk>/', FmsContactDetailView.as_view(), name='fms_contact_detail'),
    path('<int:pk>/update/', FmsContactUpdateView.as_view(), name='fms_contact_update'),
    path('<int:pk>/delete/', FmsContactDeleteView.as_view(), name='fms_contact_delete'),
]