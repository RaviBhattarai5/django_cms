from django.urls import path
from .views import TransporterListView, TransporterDetailView, TransporterCreateView, transporter_update_view, TransporterDeleteView

urlpatterns = [
    path('', TransporterListView.as_view(), name='transporter_list'),
    path('<int:pk>/update/', transporter_update_view, name='transporter_update'),
    # path('<int:pk>/update/', TransporterUpdateView.as_view(), name='transporter_update'),

    path('<int:pk>/', TransporterDetailView.as_view(), name='transporter_detail'),
    path('create/', TransporterCreateView.as_view(), name='transporter_create'),
    path('<int:pk>/delete/', TransporterDeleteView.as_view(), name='transporter_delete'),
]
