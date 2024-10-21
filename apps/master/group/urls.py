from django.urls import path
from .views import *
urlpatterns = [
    path('', GroupListView.as_view(), name='group_list'),
    path('create/', GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
]
