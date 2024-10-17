from django.urls import path
from .views import *
urlpatterns = [
    path('', LeadSourceListView.as_view(), name='lead_source_list'),
    path('create/', LeadSourceCreateView.as_view(), name='lead_source_create'),
    path('<int:pk>/', LeadSourceDetailView.as_view(), name='lead_source_detail'),
    path('<int:pk>/update/', LeadSourceUpdateView.as_view(), name='lead_source_update'),
    path('<int:pk>/delete/', LeadSourceDeleteView.as_view(), name='lead_source_delete'),
]
