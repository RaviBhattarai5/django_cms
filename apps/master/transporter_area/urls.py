from django.urls import path
from .views import *
urlpatterns = [
    path('', TransporterAreaListView.as_view(), name='transporter_area_list'),
    path('create/', TransporterAreaCreateView.as_view(), name='transporter_area_create'),
    path('<int:pk>/', TransporterAreaDetailView.as_view(), name='transporter_area_detail'),
    path('<int:pk>/update/', TransporterAreaUpdateView.as_view(), name='transporter_area_update'),
    path('<int:pk>/delete/', TransporterAreaDeleteView.as_view(), name='transporter_area_delete'),
]
