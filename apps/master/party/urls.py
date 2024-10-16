from django.urls import path
from .views import *

urlpatterns = [
    path('',PartyListView.as_view(), name='party_list'),
    path('create/', PartyCreateView.as_view(), name='party_create'),
    # path('<int:pk>/', PartyDetailView.as_view(), name='party_detail'),
    path('<int:pk>/update/', PartyUpdateView.as_view(), name='party_update'),
    path('<int:pk>/delete/', PartyDeleteView.as_view(), name='party_delete'),
]