from django.urls import path
from .views import *
urlpatterns = [
    path('', TransporterListView.as_view(), name='transporter_list'),
    path('create/', TransporterCreateView.as_view(), name='transporter_create'),
    path('<int:pk>/', TransporterDetailView.as_view(), name='transporter_detail'),
    path('<int:pk>/update/', TransporterUpdateView.as_view(), name='transporter_update'),
    path('<int:pk>/delete/', TransporterDeleteView.as_view(), name='transporter_delete'),
]
