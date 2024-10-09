from django.urls import path
from .views import *
urlpatterns = [
    path('', SerialStatusListView.as_view(), name='serial_status_list'),
    path('create/', SerialStatusCreateView.as_view(), name='serial_status_create'),
    path('<int:pk>/', SerialStatusDetailView.as_view(), name='serial_status_detail'),
    path('<int:pk>/update/', SerialStatusUpdateView.as_view(), name='serial_status_update'),
    path('<int:pk>/delete/', SerialStatusDeleteView.as_view(), name='serial_status_delete'),
]
